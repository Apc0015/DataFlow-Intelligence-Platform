"""
Simple test script to validate the modular application structure
"""

import sys
from pathlib import Path

# Add src to path
src_dir = Path(__file__).parent / "src"
sys.path.append(str(src_dir))

def test_imports():
    """Test that all modules can be imported successfully"""
    print("Testing imports...")
    
    try:
        from utils.styles import load_custom_css, get_color_palette
        print("✅ Styles module imported successfully")
        
        # Test color palette
        colors = get_color_palette()
        assert 'primary' in colors
        print("✅ Color palette working")
        
    except Exception as e:
        print(f"❌ Styles module error: {e}")
        return False
    
    try:
        from utils.data_handler import DataHandler
        print("✅ Data handler module imported successfully")
        
        # Test data generation
        happiness_data = DataHandler.load_happiness_data()
        assert not happiness_data.empty
        print(f"✅ Happiness data loaded: {len(happiness_data)} records")
        
        university_data = DataHandler.load_university_data()  
        assert not university_data.empty
        print(f"✅ University data loaded: {len(university_data)} records")
        
        airport_data = DataHandler.load_airport_data("JFK")
        assert not airport_data.empty
        print(f"✅ Airport data generated: {len(airport_data)} records")
        
    except Exception as e:
        print(f"❌ Data handler error: {e}")
        return False
    
    try:
        from utils.csv_validator import CSVValidator, validate_data_files
        print("✅ CSV validator module imported successfully")
        
        # Test data validation
        data_dir = Path(__file__).parent / "data" / "raw"
        if data_dir.exists():
            validation_results = validate_data_files(data_dir)
            print(f"✅ Data validation completed for {len(validation_results)} files")
        
    except Exception as e:
        print(f"❌ CSV validator error: {e}")
        return False
    
    try:
        from components.portfolio_overview import render_portfolio_overview
        from components.transportation_analytics import render_transportation_analytics
        print("✅ Component modules imported successfully")
        
    except Exception as e:
        print(f"❌ Component import error: {e}")
        return False
    
    return True

def test_data_integrity():
    """Test data integrity and validation"""
    print("\nTesting data integrity...")
    
    try:
        from utils.data_handler import DataHandler
        from utils.csv_validator import DataIntegrityChecker
        
        # Test happiness data integrity
        happiness_data = DataHandler.load_happiness_data()
        happiness_issues = DataIntegrityChecker.validate_happiness_data(happiness_data)
        
        if happiness_issues:
            print(f"⚠️  Happiness data issues: {len(happiness_issues)}")
            for issue in happiness_issues[:3]:  # Show first 3 issues
                print(f"   - {issue}")
        else:
            print("✅ Happiness data integrity validated")
        
        # Test university data integrity
        university_data = DataHandler.load_university_data()
        university_issues = DataIntegrityChecker.validate_university_data(university_data)
        
        if university_issues:
            print(f"⚠️  University data issues: {len(university_issues)}")
            for issue in university_issues[:3]:
                print(f"   - {issue}")
        else:
            print("✅ University data integrity validated")
        
        return True
        
    except Exception as e:
        print(f"❌ Data integrity test error: {e}")
        return False

def test_file_structure():
    """Test that all required files exist"""
    print("\nTesting file structure...")
    
    base_dir = Path(__file__).parent
    required_files = [
        "src/app.py",
        "src/utils/styles.py", 
        "src/utils/data_handler.py",
        "src/utils/csv_validator.py",
        "src/components/portfolio_overview.py",
        "src/components/transportation_analytics.py",
        "requirements.txt",
        "README.md"
    ]
    
    all_exist = True
    for file_path in required_files:
        full_path = base_dir / file_path
        if full_path.exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ Missing: {file_path}")
            all_exist = False
    
    return all_exist

def main():
    """Run all tests"""
    print("🧪 Running Flight Route Dashboard Tests\n")
    print("=" * 50)
    
    tests_passed = 0
    total_tests = 3
    
    # Test 1: File structure
    if test_file_structure():
        tests_passed += 1
    
    # Test 2: Module imports
    if test_imports():
        tests_passed += 1
    
    # Test 3: Data integrity
    if test_data_integrity():
        tests_passed += 1
    
    # Results
    print("\n" + "=" * 50)
    print(f"Test Results: {tests_passed}/{total_tests} passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! The application is ready to run.")
        print("\nTo start the application, run:")
        print("streamlit run src/app.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return tests_passed == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)