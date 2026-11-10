"""
Automated test suite for DataFlow Intelligence Platform.
Covers data transformations, CSV validation, integrity checks,
pipeline components, analytics metrics, and platform utilities.
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
import pytest

# Ensure src is on Python path
REPO_ROOT = Path(__file__).parent.parent
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from utils.data_handler import DataHandler
from utils.csv_validator import CSVValidator, DataIntegrityChecker, validate_data_files
from utils.styles import get_color_palette, load_custom_css
from components.education_intelligence_simple import generate_education_data
from components.visualization_excellence_simple import generate_visualization_data


# ============================================================================
# 1. DataHandler & Ingestion Pipeline Tests
# ============================================================================

class TestDataHandler:
    """Tests for raw and synthetic data loading and extraction pipelines."""

    def test_load_happiness_data_from_csv(self):
        """Verify happiness dataset loads raw CSV with correct row count and columns."""
        df = DataHandler.load_happiness_data()
        assert isinstance(df, pd.DataFrame)
        assert not df.empty
        assert len(df) == 146
        expected_cols = [
            'RANK', 'Country', 'Happiness_score', 'Whisker_high', 'Whisker_low',
            'Dystopia_residual', 'GDP_per_capita', 'Social_support',
            'Healthy_life_expectancy', 'Freedom', 'Generosity', 'Corruption'
        ]
        assert list(df.columns) == expected_cols
        # Verify placeholder 'xx' rows are filtered out
        assert 'xx' not in df['Country'].values

    def test_load_happiness_data_numeric_conversion(self):
        """Verify happiness scores and ranks are properly converted to numeric values."""
        df = DataHandler.load_happiness_data()
        assert pd.api.types.is_numeric_dtype(df['RANK'])
        # Comma decimals in CSV should result in numeric or cleanly convertible values
        assert df['RANK'].min() == 1
        assert df['RANK'].max() == 146

    def test_load_university_data_from_csv(self):
        """Verify university enrollment metrics load correctly from raw CSV."""
        df = DataHandler.load_university_data()
        assert isinstance(df, pd.DataFrame)
        assert not df.empty
        assert len(df) == 20
        required_cols = ['Year', 'Term', 'Applications', 'Admitted', 'Enrolled']
        for col in required_cols:
            assert col in df.columns

    def test_load_airport_data_valid_hubs(self):
        """Verify flight route generation for supported East Coast aviation hubs."""
        hubs = ["JFK", "ATL", "MIA", "BOS", "PHL"]
        for hub in hubs:
            df = DataHandler.load_airport_data(hub)
            assert isinstance(df, pd.DataFrame)
            assert not df.empty, f"Expected flight data for hub {hub}"
            assert (df['source_airport'] == hub).all()
            expected_fields = [
                'source_airport', 'destination_airport', 'destination_name',
                'destination_lat', 'destination_lon', 'airline',
                'flight_hour', 'domestic', 'region', 'distance'
            ]
            for field in expected_fields:
                assert field in df.columns
            # Flight hours should be in realistic bounds [5, 23]
            assert df['flight_hour'].between(5, 23).all()
            # Distances should be strictly positive
            assert (df['distance'] > 0).all()

    def test_load_airport_data_invalid_hub(self):
        """Verify non-supported airport code returns an empty DataFrame gracefully."""
        df = DataHandler.load_airport_data("INVALID_HUB")
        assert isinstance(df, pd.DataFrame)
        assert df.empty

    def test_synthetic_happiness_fallback(self):
        """Verify synthetic happiness data generation schema and rankings."""
        df = DataHandler._generate_synthetic_happiness_data()
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
        assert 'Happiness_score' in df.columns
        assert 'Country' in df.columns
        assert 'Region' in df.columns
        assert df['Happiness_score'].between(2.0, 8.0).all()
        # Verify rank ordering matches descending happiness score
        assert df['RANK'].iloc[0] == 1
        assert df['Happiness_score'].is_monotonic_decreasing

    def test_synthetic_university_fallback(self):
        """Verify synthetic university data generation follows academic calendar logic."""
        df = DataHandler._generate_synthetic_university_data()
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 20  # 10 years * 2 terms
        assert set(df['Term'].unique()) == {"Spring", "Fall"}
        # Fall term applications should generally exceed Spring due to seasonal admissions
        fall_apps = df[df['Term'] == 'Fall']['Applications'].mean()
        spring_apps = df[df['Term'] == 'Spring']['Applications'].mean()
        assert fall_apps > spring_apps

    def test_validate_data_helper(self):
        """Verify DataHandler.validate_data handles matching, missing, and empty frames."""
        sample_df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        assert DataHandler.validate_data(sample_df, ['a', 'b']) is True
        assert DataHandler.validate_data(sample_df, ['a', 'c']) is False
        assert DataHandler.validate_data(pd.DataFrame(), ['a']) is False
        assert DataHandler.validate_data(None, ['a']) is False

    def test_get_data_info_helper(self):
        """Verify DataHandler.get_data_info provides summary statistics or handles empty data."""
        sample_df = pd.DataFrame({'metric': [10, 20, 30], 'label': ['x', 'y', 'z']})
        info = DataHandler.get_data_info(sample_df)
        assert info['shape'] == (3, 2)
        assert 'metric' in info['columns']
        assert 'memory_usage' in info
        # Empty DataFrame handling
        empty_info = DataHandler.get_data_info(pd.DataFrame())
        assert "error" in empty_info


# ============================================================================
# 2. CSV Validator & Data Integrity Tests
# ============================================================================

class TestCSVValidator:
    """Tests for CSV structural validation, sanitization, and data quality reports."""

    def test_validate_csv_structure_existing_files(self, tmp_path):
        """Verify validate_csv_structure on legitimate CSVs and missing files."""
        # Test on actual raw files
        raw_happiness = REPO_ROOT / "data" / "raw" / "2022.csv"
        is_valid, msg = CSVValidator.validate_csv_structure(
            raw_happiness, ['RANK', 'Country', 'Happiness score']
        )
        assert is_valid is True

        # Test on nonexistent path
        fake_path = tmp_path / "nonexistent.csv"
        is_valid, msg = CSVValidator.validate_csv_structure(fake_path, ['a'])
        assert is_valid is False
        assert "not found" in msg.lower()

        # Test on zero-byte file
        empty_file = tmp_path / "empty.csv"
        empty_file.write_text("")
        is_valid, msg = CSVValidator.validate_csv_structure(empty_file, ['a'])
        assert is_valid is False
        assert "empty" in msg.lower()

        # Test missing required column
        dummy_file = tmp_path / "dummy.csv"
        dummy_file.write_text("col_a,col_b\n1,2\n3,4\n")
        is_valid, msg = CSVValidator.validate_csv_structure(dummy_file, ['col_c'])
        assert is_valid is False
        assert "Missing required columns" in msg

    def test_clean_csv_data_placeholders_and_decimals(self):
        """Verify clean_csv_data drops placeholders and normalizes comma-decimals."""
        dirty_df = pd.DataFrame({
            'id': ['1', '2', '3', 'xx', '5'],
            'score': ['7,82', 'N/A', '6,50', '5,10', 'NULL'],
            'name': ['Alpha', 'Beta', 'Gamma', 'xx', 'Epsilon']
        })
        cleaned = CSVValidator.clean_csv_data(dirty_df, numeric_columns=['score'])
        # Placeholder rows ('xx', 'N/A', 'NULL') should be dropped
        assert 'xx' not in cleaned['name'].values
        assert 'N/A' not in cleaned['score'].values
        assert 'NULL' not in cleaned['score'].values
        # Numeric conversion of comma-decimal: '7,82' -> 7.82
        assert pd.api.types.is_numeric_dtype(cleaned['score'])
        assert 7.82 in cleaned['score'].values

    def test_get_data_quality_report(self):
        """Verify get_data_quality_report computes complete audit statistics."""
        df = pd.DataFrame({
            'num': [1.0, 2.5, np.nan, 4.0],
            'cat': ['A', 'B', 'A', 'C']
        })
        report = CSVValidator.get_data_quality_report(df)
        assert report['total_rows'] == 4
        assert report['total_columns'] == 2
        assert report['missing_values']['num'] == 1
        assert report['duplicated_rows'] == 0
        assert 'numeric_stats' in report
        assert 'categorical_stats' in report
        assert report['categorical_stats']['cat']['most_common'] == 'A'

    def test_get_data_quality_report_empty(self):
        """Verify get_data_quality_report returns error on empty DataFrame."""
        report = CSVValidator.get_data_quality_report(pd.DataFrame())
        assert "error" in report


class TestDataIntegrityChecker:
    """Tests for domain business-rule validation across datasets."""

    def test_validate_happiness_data_valid(self):
        """Verify that standard happiness data generates 0 integrity issues."""
        df = pd.DataFrame({
            'Happiness_score': [7.5, 6.2, 5.1],
            'GDP_per_capita': [1.8, 1.2, 0.9],
            'Country': ['Finland', 'Costa Rica', 'Ghana']
        })
        issues = DataIntegrityChecker.validate_happiness_data(df)
        assert issues == []

    def test_validate_happiness_data_out_of_bounds(self):
        """Verify detection of invalid happiness ranges, negative GDP, and empty countries."""
        invalid_df = pd.DataFrame({
            'Happiness_score': [-1.0, 11.5, 5.0],
            'GDP_per_capita': [-0.5, 1.2, 1.0],
            'Country': ['', 'CountryB', None]
        })
        issues = DataIntegrityChecker.validate_happiness_data(invalid_df)
        assert len(issues) == 3
        assert any("invalid happiness scores" in i for i in issues)
        assert any("negative GDP" in i for i in issues)
        assert any("missing country names" in i for i in issues)

    def test_validate_university_data_valid(self):
        """Verify standard university enrollment data passes all integrity checks."""
        df = pd.DataFrame({
            'Year': [2021, 2022],
            'Applications': [3000, 3200],
            'Admitted': [1800, 1900],
            'Enrolled': [750, 800],
            'Retention Rate (%)': [88, 90],
            'Student Satisfaction (%)': [82, 85]
        })
        issues = DataIntegrityChecker.validate_university_data(df)
        assert issues == []

    def test_validate_university_data_illogical_funnel(self):
        """Verify detection of enrollment funnel violations (e.g. Enrolled > Admitted)."""
        broken_df = pd.DataFrame({
            'Year': [2022],
            'Applications': [1000],
            'Admitted': [800],
            'Enrolled': [900],  # Cannot enroll more than admitted
            'Retention Rate (%)': [120],  # Invalid percentage > 100
            'Student Satisfaction (%)': [-5]  # Invalid negative percentage
        })
        issues = DataIntegrityChecker.validate_university_data(broken_df)
        assert len(issues) >= 2
        assert any("illogical enrollment progression" in i for i in issues)
        assert any("invalid Retention Rate (%)" in i for i in issues)

    def test_validate_data_files_pipeline(self):
        """Verify end-to-end data directory validation on data/raw."""
        data_dir = REPO_ROOT / "data" / "raw"
        results = validate_data_files(data_dir)
        assert "2022.csv" in results
        assert "university_data.csv" in results
        assert results["2022.csv"]["structure_valid"] is True
        assert results["university_data.csv"]["structure_valid"] is True


# ============================================================================
# 3. Domain Analytics & Pipeline Metrics Tests
# ============================================================================

class TestDomainPipelinesAndMetrics:
    """Tests for multi-domain analytics modules and calculated metrics."""

    def test_education_data_generation_pipeline(self):
        """Verify education analytics data pipeline returns valid structures and cohorts."""
        data = generate_education_data()
        assert isinstance(data, dict)
        assert set(data.keys()) == {'students', 'enrollment', 'programs'}

        # Verify student cohort data
        students = data['students']
        assert len(students) == 2500
        assert students['gpa'].between(0.0, 4.0).all()
        assert set(students['retention_status'].unique()).issubset({'Retained', 'At Risk', 'Graduated'})
        assert students['satisfaction_score'].between(1, 5).all()

        # Verify enrollment trend data
        enrollment = data['enrollment']
        assert len(enrollment) == 6
        assert (enrollment['new_students'] <= enrollment['total_enrollment']).all()
        assert enrollment['graduation_rate'].between(0, 100).all()
        assert enrollment['retention_rate'].between(0, 100).all()

        # Verify academic program benchmarks
        programs = data['programs']
        assert len(programs) == 6
        assert programs['avg_gpa'].between(2.0, 4.0).all()
        assert programs['completion_rate'].between(0, 100).all()
        assert programs['employment_rate'].between(0, 100).all()

    def test_visualization_data_generation_pipeline(self):
        """Verify visualization framework data pipeline returns valid analytical datasets."""
        viz_data = generate_visualization_data()
        assert isinstance(viz_data, dict)
        assert 'happiness' in viz_data
        assert 'time_series' in viz_data
        assert 'economic' in viz_data

        # Happiness dataset
        happiness = viz_data['happiness']
        assert len(happiness) == 30
        assert happiness['happiness_score'].between(1.0, 10.0).all()
        assert (happiness['gdp_per_capita'] > 0).all()

        # Time series dataset (10 countries x 10 years = 100 records)
        ts = viz_data['time_series']
        assert len(ts) == 100
        assert ts['year'].min() == 2015
        assert ts['year'].max() == 2024

        # Economic indicators
        economic = viz_data['economic']
        assert len(economic) == 30
        assert (economic['unemployment_rate'] >= 0).all()
        assert economic['education_index'].between(0.0, 1.0).all()


# ============================================================================
# 4. Styling & Platform Utilities Tests
# ============================================================================

class TestPlatformUtilities:
    """Tests for platform theme colors, design tokens, and CSS loaders."""

    def test_get_color_palette(self):
        """Verify color palette dictionary contains foundational UI tokens."""
        palette = get_color_palette()
        assert isinstance(palette, dict)
        assert 'primary' in palette
        assert 'background' in palette
        assert 'text' in palette
        assert 'border' in palette
        for color in palette.values():
            assert color.startswith("#")

    def test_load_custom_css_execution(self):
        """Verify custom CSS helper executes without throwing exceptions."""
        try:
            load_custom_css()
        except Exception as e:
            pytest.fail(f"load_custom_css() raised an exception: {e}")
