"""
CSV validation and processing utilities
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging
from typing import Optional, Dict, List, Tuple

logger = logging.getLogger(__name__)

class CSVValidator:
    """CSV file validation and processing utility"""
    
    @staticmethod
    def validate_csv_structure(file_path: Path, expected_columns: List[str]) -> Tuple[bool, str]:
        """
        Validate CSV file structure and content
        
        Args:
            file_path: Path to CSV file
            expected_columns: List of expected column names
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            if not file_path.exists():
                return False, f"File not found: {file_path}"
            
            # Check file size
            if file_path.stat().st_size == 0:
                return False, "File is empty"
            
            # Try to read CSV
            df = pd.read_csv(file_path, nrows=5)  # Read first 5 rows for validation
            
            # Check if file has any data
            if df.empty:
                return False, "CSV file contains no data"
            
            # Validate columns if specified
            if expected_columns:
                missing_cols = set(expected_columns) - set(df.columns)
                if missing_cols:
                    return False, f"Missing required columns: {missing_cols}"
            
            return True, "File structure is valid"
            
        except pd.errors.EmptyDataError:
            return False, "CSV file is empty or corrupted"
        except pd.errors.ParserError as e:
            return False, f"CSV parsing error: {str(e)}"
        except Exception as e:
            return False, f"Unexpected error: {str(e)}"
    
    @staticmethod
    def clean_csv_data(df: pd.DataFrame, numeric_columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Clean CSV data by handling missing values and data types
        
        Args:
            df: DataFrame to clean
            numeric_columns: List of columns that should be numeric
            
        Returns:
            Cleaned DataFrame
        """
        df_cleaned = df.copy()
        
        # Remove completely empty rows
        df_cleaned = df_cleaned.dropna(how='all')
        
        # Remove placeholder values
        placeholder_values = ['xx', 'XX', 'N/A', 'n/a', 'NULL', 'null', '']
        for col in df_cleaned.columns:
            if df_cleaned[col].dtype == 'object':
                df_cleaned = df_cleaned[~df_cleaned[col].isin(placeholder_values)]
        
        # Convert numeric columns
        if numeric_columns:
            for col in numeric_columns:
                if col in df_cleaned.columns:
                    # Handle decimal comma notation
                    if df_cleaned[col].dtype == 'object':
                        df_cleaned[col] = df_cleaned[col].astype(str).str.replace(',', '.')
                    
                    df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')
        
        # Log cleaning results
        original_rows = len(df)
        cleaned_rows = len(df_cleaned)
        logger.info(f"Data cleaning: {original_rows} -> {cleaned_rows} rows ({original_rows - cleaned_rows} removed)")
        
        return df_cleaned
    
    @staticmethod
    def get_data_quality_report(df: pd.DataFrame) -> Dict:
        """
        Generate a data quality report for the DataFrame
        
        Args:
            df: DataFrame to analyze
            
        Returns:
            Dictionary with data quality metrics
        """
        if df.empty:
            return {"error": "DataFrame is empty"}
        
        report = {
            "total_rows": len(df),
            "total_columns": len(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
            "missing_percentage": (df.isnull().sum() / len(df) * 100).round(2).to_dict(),
            "duplicated_rows": df.duplicated().sum(),
            "memory_usage_mb": df.memory_usage(deep=True).sum() / 1024 / 1024,
            "data_types": df.dtypes.to_dict()
        }
        
        # Add column-specific statistics
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        if len(numeric_columns) > 0:
            report["numeric_stats"] = df[numeric_columns].describe().to_dict()
        
        categorical_columns = df.select_dtypes(include=['object']).columns
        if len(categorical_columns) > 0:
            report["categorical_stats"] = {}
            for col in categorical_columns:
                report["categorical_stats"][col] = {
                    "unique_values": df[col].nunique(),
                    "most_common": df[col].mode().iloc[0] if not df[col].mode().empty else None
                }
        
        return report

class DataIntegrityChecker:
    """Check data integrity and business logic validation"""
    
    @staticmethod
    def validate_happiness_data(df: pd.DataFrame) -> List[str]:
        """Validate World Happiness Report data"""
        issues = []
        
        # Check happiness score range
        if 'Happiness_score' in df.columns:
            invalid_scores = df[(df['Happiness_score'] < 0) | (df['Happiness_score'] > 10)]
            if not invalid_scores.empty:
                issues.append(f"Found {len(invalid_scores)} rows with invalid happiness scores (should be 0-10)")
        
        # Check GDP values
        if 'GDP_per_capita' in df.columns:
            invalid_gdp = df[df['GDP_per_capita'] < 0]
            if not invalid_gdp.empty:
                issues.append(f"Found {len(invalid_gdp)} rows with negative GDP values")
        
        # Check country names
        if 'Country' in df.columns:
            empty_countries = df[df['Country'].isnull() | (df['Country'] == '')]
            if not empty_countries.empty:
                issues.append(f"Found {len(empty_countries)} rows with missing country names")
        
        return issues
    
    @staticmethod
    def validate_university_data(df: pd.DataFrame) -> List[str]:
        """Validate university enrollment data"""
        issues = []
        
        # Check year range
        if 'Year' in df.columns:
            current_year = pd.Timestamp.now().year
            invalid_years = df[(df['Year'] < 2000) | (df['Year'] > current_year + 1)]
            if not invalid_years.empty:
                issues.append(f"Found {len(invalid_years)} rows with invalid years")
        
        # Check enrollment numbers
        enrollment_cols = ['Applications', 'Admitted', 'Enrolled']
        for col in enrollment_cols:
            if col in df.columns:
                negative_values = df[df[col] < 0]
                if not negative_values.empty:
                    issues.append(f"Found {len(negative_values)} rows with negative {col}")
        
        # Check logical consistency (Enrolled <= Admitted <= Applications)
        if all(col in df.columns for col in enrollment_cols):
            logical_errors = df[
                (df['Enrolled'] > df['Admitted']) | 
                (df['Admitted'] > df['Applications'])
            ]
            if not logical_errors.empty:
                issues.append(f"Found {len(logical_errors)} rows with illogical enrollment progression")
        
        # Check percentage ranges
        percentage_cols = ['Retention Rate (%)', 'Student Satisfaction (%)']
        for col in percentage_cols:
            if col in df.columns:
                invalid_pct = df[(df[col] < 0) | (df[col] > 100)]
                if not invalid_pct.empty:
                    issues.append(f"Found {len(invalid_pct)} rows with invalid {col} (should be 0-100)")
        
        return issues

def validate_data_files(data_dir: Path) -> Dict[str, Dict]:
    """
    Validate all data files in the directory
    
    Args:
        data_dir: Path to data directory
        
    Returns:
        Dictionary with validation results for each file
    """
    results = {}
    
    # Define expected structures
    file_configs = {
        "2022.csv": {
            "expected_columns": ['RANK', 'Country', 'Happiness_score', 'GDP_per_capita'],
            "numeric_columns": ['RANK', 'Happiness_score', 'GDP_per_capita'],
            "integrity_checker": DataIntegrityChecker.validate_happiness_data
        },
        "university_data.csv": {
            "expected_columns": ['Year', 'Term', 'Applications', 'Admitted', 'Enrolled'],
            "numeric_columns": ['Year', 'Applications', 'Admitted', 'Enrolled'],
            "integrity_checker": DataIntegrityChecker.validate_university_data
        }
    }
    
    for filename, config in file_configs.items():
        file_path = data_dir / filename
        
        # Structure validation
        is_valid, message = CSVValidator.validate_csv_structure(
            file_path, 
            config.get("expected_columns", [])
        )
        
        results[filename] = {
            "file_exists": file_path.exists(),
            "structure_valid": is_valid,
            "validation_message": message
        }
        
        if is_valid and file_path.exists():
            try:
                # Load and clean data
                df = pd.read_csv(file_path)
                df_cleaned = CSVValidator.clean_csv_data(df, config.get("numeric_columns"))
                
                # Quality report
                quality_report = CSVValidator.get_data_quality_report(df_cleaned)
                results[filename]["quality_report"] = quality_report
                
                # Integrity check
                if "integrity_checker" in config:
                    integrity_issues = config["integrity_checker"](df_cleaned)
                    results[filename]["integrity_issues"] = integrity_issues
                
            except Exception as e:
                results[filename]["error"] = f"Error processing file: {str(e)}"
    
    return results