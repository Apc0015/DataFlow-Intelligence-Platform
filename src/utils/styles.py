"""
Enhanced styling for the DataFlow Intelligence Platform
"""

import streamlit as st

def load_custom_css():
    """Load simple CSS styling"""
    st.markdown("""
<style>
    .main {
        font-family: Arial, sans-serif;
        background: #ffffff;
        color: #333333;
    }
    
    .block-container {
        background: #ffffff;
        color: #333333;
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: none;
    }
    
    .main-header {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #333333;
    }
    
    .sub-header {
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 1rem;
        margin-bottom: 1rem;
        color: #333333;
    }
    
    .content-card {
        background: #f9f9f9;
        color: #333333;
        padding: 1.5rem;
        border: 1px solid #dddddd;
        margin: 1rem 0;
    }
    
    .metric-card {
        background: #f9f9f9;
        color: #333333;
        padding: 1rem;
        text-align: center;
        margin: 1rem 0;
        border: 1px solid #dddddd;
    }
    
    .info-box {
        background: #f0f0f0;
        color: #333333;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 3px solid #666666;
    }
    
    .simple-button {
        background: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-decoration: none;
        display: inline-block;
        margin: 5px;
        border: none;
        cursor: pointer;
    }
    
    
    
    .content-section {
        margin: 1rem 0;
        background: white;
        color: #333333;
    }
    
    
</style>
""", unsafe_allow_html=True)

def get_color_palette():
    """Return simple color palette"""
    return {
        'primary': '#4CAF50',
        'background': '#ffffff',
        'text': '#333333',
        'border': '#dddddd'
    }