"""
DataFlow Intelligence Platform - Main Application
A comprehensive analytics solution for multi-domain data analysis
"""

import streamlit as st
import sys
from pathlib import Path

# Add the src directory to the Python path
src_dir = Path(__file__).parent
sys.path.append(str(src_dir))

# Import components and utilities
from utils.styles import load_custom_css
from components.portfolio_overview import render_portfolio_overview
from components.transportation_analytics_simple import render_transportation_analytics
from components.education_intelligence_simple import render_education_intelligence
from components.visualization_excellence_simple import render_visualization_excellence

# Configure Streamlit page
st.set_page_config(
    page_title="DataFlow Intelligence Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Main application function"""
    
    # Load custom CSS
    load_custom_css()
    
    # Navigation sidebar
    st.sidebar.title("DataFlow Intelligence Platform")
    st.sidebar.write("Advanced Analytics Suite")
    
    # Navigation options
    navigation_options = [
        "Portfolio Overview", 
        "Transportation Analytics", 
        "Education Intelligence", 
        "Visualization Excellence"
    ]
    
    page = st.sidebar.radio(
        "Select Module:",
        navigation_options,
        index=0
    )
    
    # Add navigation help
    st.sidebar.markdown("---")
    st.sidebar.subheader("Platform Guide")
    st.sidebar.write("**Portfolio:** Project overview and capabilities")
    st.sidebar.write("**Transportation:** Aviation route analytics")
    st.sidebar.write("**Education:** Institutional performance metrics")
    st.sidebar.write("**Visualization:** Data storytelling best practices")
    
    # Render selected page
    try:
        if page == "Portfolio Overview":
            render_portfolio_overview()
            
        elif page == "Transportation Analytics":
            render_transportation_analytics()
            
        elif page == "Education Intelligence":
            render_education_intelligence()
            
        elif page == "Visualization Excellence":
            render_visualization_excellence()
            
    except Exception as e:
        st.error(f"An error occurred while loading the page: {str(e)}")
        st.info("Please try refreshing the page or selecting a different module.")
        
        # Show error details in development
        if st.checkbox("Show error details (for debugging)"):
            st.exception(e)


# Add footer
def render_footer():
    """Render application footer"""
    st.markdown("---")
    st.write("© 2024 DataFlow Intelligence Platform | Created by Ayush Chhoker")
    st.write("[GitHub](https://github.com/Apc0015) | [LinkedIn](https://www.linkedin.com/in/apc15/)")

if __name__ == "__main__":
    main()
    render_footer()