"""
Data handling utilities for the DataFlow Intelligence Platform
"""

import pandas as pd
import numpy as np
import streamlit as st
from pathlib import Path
from typing import Optional, Dict, Any
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "raw"

class DataHandler:
    """Centralized data handling class"""
    
    @staticmethod
    @st.cache_data
    def load_happiness_data() -> pd.DataFrame:
        """Load World Happiness Report data with error handling"""
        try:
            file_path = DATA_DIR / "2022.csv"
            if file_path.exists():
                df = pd.read_csv(file_path, decimal=',')
                # Clean up column names
                df.columns = ['RANK', 'Country', 'Happiness_score', 'Whisker_high', 'Whisker_low', 
                             'Dystopia_residual', 'GDP_per_capita', 'Social_support', 
                             'Healthy_life_expectancy', 'Freedom', 'Generosity', 'Corruption']
                # Remove placeholder rows
                df = df[df['Country'] != 'xx']
                df['RANK'] = pd.to_numeric(df['RANK'], errors='coerce')
                logger.info(f"Loaded happiness data: {len(df)} records")
                return df
            else:
                logger.warning("Happiness data file not found, generating synthetic data")
                return DataHandler._generate_synthetic_happiness_data()
        except Exception as e:
            logger.error(f"Error loading happiness data: {e}")
            return DataHandler._generate_synthetic_happiness_data()
    
    @staticmethod
    @st.cache_data
    def load_university_data() -> pd.DataFrame:
        """Load university data with error handling"""
        try:
            file_path = DATA_DIR / "university_data.csv"
            if file_path.exists():
                df = pd.read_csv(file_path)
                logger.info(f"Loaded university data: {len(df)} records")
                return df
            else:
                logger.warning("University data file not found, generating synthetic data")
                return DataHandler._generate_synthetic_university_data()
        except Exception as e:
            logger.error(f"Error loading university data: {e}")
            return DataHandler._generate_synthetic_university_data()
    
    @staticmethod
    @st.cache_data
    def load_airport_data(airport_code: str) -> pd.DataFrame:
        """Generate synthetic airport data for the given airport code"""
        try:
            return DataHandler._generate_airport_data(airport_code)
        except Exception as e:
            logger.error(f"Error generating airport data: {e}")
            return pd.DataFrame()
    
    @staticmethod
    def _generate_synthetic_happiness_data() -> pd.DataFrame:
        """Generate synthetic happiness data for demonstration"""
        np.random.seed(42)
        
        countries_by_region = {
            'Europe': ['Finland', 'Denmark', 'Iceland', 'Switzerland', 'Netherlands',
                      'Luxembourg', 'Sweden', 'Norway', 'Austria', 'Ireland',
                      'Germany', 'Czechia', 'Belgium', 'Slovenia', 'United Kingdom',
                      'France', 'Estonia', 'Spain', 'Italy'],
            'North America': ['Canada', 'United States'],
            'Latin America': ['Costa Rica', 'Uruguay', 'Brazil', 'Chile', 'Mexico',
                             'Argentina', 'Panama', 'Colombia'],
            'Asia & Pacific': ['New Zealand', 'Australia', 'Israel', 'Singapore',
                              'Japan', 'South Korea', 'Thailand', 'Malaysia',
                              'China', 'Vietnam', 'Indonesia'],
            'Middle East': ['United Arab Emirates', 'Saudi Arabia', 'Bahrain',
                           'Kuwait', 'Jordan', 'Lebanon'],
            'Africa': ['Mauritius', 'South Africa', 'Morocco', 'Ghana', 'Kenya',
                      'Nigeria', 'Ethiopia', 'Rwanda', 'Zimbabwe'],
            'Former Soviet States': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine']
        }
        
        data = []
        rank = 1
        
        for region, countries in countries_by_region.items():
            # Set base happiness scores by region
            region_base_happiness = {
                'Europe': 7.0,
                'North America': 6.8,
                'Latin America': 6.2,
                'Asia & Pacific': 5.8,
                'Middle East': 5.5,
                'Africa': 4.5,
                'Former Soviet States': 5.0
            }
            
            region_base_gdp = {
                'Europe': 1.6,
                'North America': 1.7,
                'Latin America': 1.0,
                'Asia & Pacific': 1.3,
                'Middle East': 1.4,
                'Africa': 0.7,
                'Former Soviet States': 1.1
            }
            
            for country in countries:
                base_happiness = region_base_happiness[region]
                base_gdp = region_base_gdp[region]
                
                # Add country-specific variations
                happiness = base_happiness + np.random.uniform(-0.8, 0.8)
                gdp = base_gdp + np.random.uniform(-0.3, 0.3)
                
                # Ensure reasonable bounds
                happiness = max(2.0, min(8.0, happiness))
                gdp = max(0.3, min(2.0, gdp))
                
                row = {
                    'RANK': rank,
                    'Country': country,
                    'Happiness_score': round(happiness, 3),
                    'GDP_per_capita': round(gdp, 3),
                    'Social_support': round(np.random.uniform(0.5, 1.5), 3),
                    'Healthy_life_expectancy': round(np.random.uniform(0.5, 1.5), 3),
                    'Freedom': round(np.random.uniform(0.3, 1.2), 3),
                    'Generosity': round(np.random.uniform(-0.2, 0.5), 3),
                    'Corruption': round(np.random.uniform(0, 0.5), 3),
                    'Region': region
                }
                data.append(row)
                rank += 1
        
        df = pd.DataFrame(data)
        # Sort by happiness score for realistic ranking
        df = df.sort_values('Happiness_score', ascending=False).reset_index(drop=True)
        df['RANK'] = range(1, len(df) + 1)
        
        return df
    
    @staticmethod
    def _generate_synthetic_university_data() -> pd.DataFrame:
        """Generate synthetic university data"""
        np.random.seed(42)
        
        years = range(2015, 2025)
        terms = ["Spring", "Fall"]
        data = []
        
        for year in years:
            for term in terms:
                # Simulate growth over time
                base_apps = 2500 + (year - 2015) * 120
                base_retention = 85 + min((year - 2015) * 0.8, 8)
                base_satisfaction = 78 + min((year - 2015) * 1.2, 12)
                
                # Fall terms typically have more applications
                if term == "Fall":
                    base_apps = int(base_apps * 1.3)
                
                row = {
                    "Year": year,
                    "Term": term,
                    "Applications": base_apps + np.random.randint(-100, 100),
                    "Admitted": int(base_apps * 0.65) + np.random.randint(-50, 50),
                    "Enrolled": int(base_apps * 0.28) + np.random.randint(-30, 30),
                    "Retention Rate (%)": max(75, base_retention + np.random.randint(-3, 3)),
                    "Student Satisfaction (%)": max(70, base_satisfaction + np.random.randint(-4, 4)),
                    "Engineering Enrolled": int(base_apps * 0.28 * 0.35) + np.random.randint(-8, 8),
                    "Business Enrolled": int(base_apps * 0.28 * 0.28) + np.random.randint(-6, 6),
                    "Arts Enrolled": int(base_apps * 0.28 * 0.22) + np.random.randint(-5, 5),
                    "Science Enrolled": int(base_apps * 0.28 * 0.15) + np.random.randint(-4, 4)
                }
                data.append(row)
        
        return pd.DataFrame(data)
    
    @staticmethod
    def _generate_airport_data(airport_code: str) -> pd.DataFrame:
        """Generate synthetic airport flight data"""
        np.random.seed(hash(airport_code) % 1000)  # Consistent data per airport
        
        # Airport coordinates
        airport_coordinates = {
            "JFK": {"lat": 40.6413, "lon": -73.7781, "name": "John F. Kennedy International"},
            "ATL": {"lat": 33.6407, "lon": -84.4277, "name": "Hartsfield-Jackson Atlanta International"},
            "MIA": {"lat": 25.7932, "lon": -80.2906, "name": "Miami International"},
            "BOS": {"lat": 42.3656, "lon": -71.0096, "name": "Boston Logan International"},
            "PHL": {"lat": 39.8729, "lon": -75.2437, "name": "Philadelphia International"}
        }
        
        # Destination airports with realistic data
        destinations = {
            # Domestic destinations
            "LAX": {"name": "Los Angeles International", "lat": 33.9416, "lon": -118.4085, "domestic": True, "region": "West Coast"},
            "ORD": {"name": "Chicago O'Hare International", "lat": 41.9786, "lon": -87.9048, "domestic": True, "region": "Midwest"},
            "DFW": {"name": "Dallas/Fort Worth International", "lat": 32.8968, "lon": -97.0380, "domestic": True, "region": "South"},
            "DEN": {"name": "Denver International", "lat": 39.8561, "lon": -104.6737, "domestic": True, "region": "Mountain"},
            "SFO": {"name": "San Francisco International", "lat": 37.6213, "lon": -122.3790, "domestic": True, "region": "West Coast"},
            "SEA": {"name": "Seattle-Tacoma International", "lat": 47.4502, "lon": -122.3088, "domestic": True, "region": "Northwest"},
            "MCO": {"name": "Orlando International", "lat": 28.4312, "lon": -81.3081, "domestic": True, "region": "Southeast"},
            # International destinations
            "LHR": {"name": "London Heathrow", "lat": 51.4700, "lon": -0.4543, "domestic": False, "region": "Europe"},
            "CDG": {"name": "Paris Charles de Gaulle", "lat": 49.0097, "lon": 2.5479, "domestic": False, "region": "Europe"},
            "FRA": {"name": "Frankfurt Airport", "lat": 50.0379, "lon": 8.5622, "domestic": False, "region": "Europe"},
            "NRT": {"name": "Tokyo Narita International", "lat": 35.7647, "lon": 140.3864, "domestic": False, "region": "Asia"},
            "HKG": {"name": "Hong Kong International", "lat": 22.3080, "lon": 113.9185, "domestic": False, "region": "Asia"},
            "SYD": {"name": "Sydney Airport", "lat": -33.9399, "lon": 151.1753, "domestic": False, "region": "Oceania"},
            "GRU": {"name": "São Paulo/Guarulhos International", "lat": -23.4356, "lon": -46.4731, "domestic": False, "region": "South America"},
        }
        
        airlines = [
            "American Airlines", "Delta Air Lines", "United Airlines", 
            "Southwest Airlines", "JetBlue Airways", "British Airways", 
            "Lufthansa", "Air France", "Emirates", "Qatar Airways"
        ]
        
        if airport_code not in airport_coordinates:
            return pd.DataFrame()
        
        source_info = airport_coordinates[airport_code]
        flights = []
        
        for dest_code, dest_info in destinations.items():
            # Calculate distance and determine flight frequency
            distance = np.sqrt((source_info["lat"] - dest_info["lat"])**2 + 
                             (source_info["lon"] - dest_info["lon"])**2)
            
            # More flights to domestic destinations and closer airports
            base_flights = 15 if dest_info["domestic"] else 8
            distance_factor = max(0.3, 1 / (distance * 0.01 + 0.5))
            num_flights = int(base_flights * distance_factor)
            num_flights = max(2, min(25, num_flights))
            
            for _ in range(num_flights):
                # Realistic airline distribution
                if dest_info["domestic"]:
                    airline = np.random.choice(airlines[:5], p=[0.3, 0.25, 0.2, 0.15, 0.1])
                else:
                    airline = np.random.choice(airlines, p=[0.15, 0.15, 0.15, 0.05, 0.05, 0.1, 0.1, 0.1, 0.08, 0.07])
                
                flight = {
                    "source_airport": airport_code,
                    "destination_airport": dest_code,
                    "destination_name": dest_info["name"],
                    "destination_lat": dest_info["lat"],
                    "destination_lon": dest_info["lon"],
                    "airline": airline,
                    "flight_hour": np.random.randint(5, 23),  # Realistic flight hours
                    "domestic": dest_info["domestic"],
                    "region": dest_info["region"],
                    "distance": distance * 69  # Convert to approximate miles
                }
                flights.append(flight)
        
        return pd.DataFrame(flights)

    @staticmethod
    def validate_data(df: pd.DataFrame, required_columns: list) -> bool:
        """Validate that DataFrame has required columns"""
        if df is None or df.empty:
            return False
        
        missing_columns = set(required_columns) - set(df.columns)
        if missing_columns:
            logger.warning(f"Missing columns: {missing_columns}")
            return False
        
        return True

    @staticmethod
    def get_data_info(df: pd.DataFrame) -> Dict[str, Any]:
        """Get basic information about the dataset"""
        if df is None or df.empty:
            return {"error": "No data available"}
        
        return {
            "shape": df.shape,
            "columns": df.columns.tolist(),
            "dtypes": df.dtypes.to_dict(),
            "null_counts": df.isnull().sum().to_dict(),
            "memory_usage": df.memory_usage(deep=True).sum()
        }