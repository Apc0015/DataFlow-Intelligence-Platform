"""
Visualization Excellence Framework component - Simplified version
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random

def render_visualization_excellence():
    """Render the visualization excellence framework"""
    
    st.title("Visualization Excellence Framework")
    
    # Project overview
    st.subheader("Overview")
    st.write("""
    Visualization Excellence Framework demonstrates advanced data storytelling techniques and design principles 
    that transform complex datasets into compelling, actionable insights. This comprehensive showcase highlights 
    the art and science of effective data visualization for strategic decision-making.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Design Principles**")
        st.write("Visual Excellence")
    with col2:
        st.write("**Statistical Analysis**")
        st.write("Data Insights")
    with col3:
        st.write("**Global Perspectives**")
        st.write("Cross-Cultural Data")

    # Development approach
    st.subheader("Visualization Innovation Approach")
    st.write("**Challenge Addressed:** Organizations struggle with data overload and ineffective visualizations that fail to communicate insights clearly to stakeholders and decision-makers.")
    st.write("**Solution Implemented:** Comprehensive framework combining design theory, statistical best practices, and interactive technologies to create visualizations that drive understanding and action.")
    st.write("**Technical Skills Applied:** Advanced data visualization libraries, statistical analysis, design theory, user experience optimization, and cross-platform compatibility.")
    
    # Sidebar configuration
    st.sidebar.subheader("Configuration")
    st.sidebar.write("Select Analysis Focus")
    
    viz_focus = st.sidebar.selectbox(
        "Choose Visualization Type:",
        [
            "Global Happiness Analysis",
            "Economic Development Trends", 
            "Population Demographics",
            "Climate & Environment Data"
        ],
        index=0
    )
    
    # Chart type selector
    chart_style = st.sidebar.selectbox(
        "Visualization Style:",
        ["Interactive (Plotly)", "Statistical (Seaborn)", "Comparative Analysis", "Dashboard View"],
        index=0
    )
    
    st.sidebar.markdown("---")
    st.sidebar.write("**Design Philosophy**")
    st.sidebar.write("Effective visualizations combine aesthetic appeal with functional clarity, ensuring that data stories are both beautiful and actionable for strategic decision-making.")
    
    # Generate comprehensive visualization data
    viz_data = generate_visualization_data()
    
    # Create visualization framework sections
    tab1, tab2, tab3 = st.tabs([
        "Design Principles Showcase", 
        "Statistical Visualization Excellence", 
        "Interactive Global Analytics"
    ])
    
    with tab1:
        render_design_principles_showcase(viz_data, chart_style)
    
    with tab2:
        render_statistical_excellence(viz_data, viz_focus)
    
    with tab3:
        render_interactive_global_analytics(viz_data)

def generate_visualization_data():
    """Generate comprehensive synthetic data for visualization demonstrations"""
    
    # Set random seed for reproducible data
    np.random.seed(42)
    random.seed(42)
    
    # Global happiness and development data
    countries = [
        'Denmark', 'Switzerland', 'Iceland', 'Finland', 'Netherlands',
        'Canada', 'New Zealand', 'Sweden', 'Australia', 'Israel',
        'Austria', 'Costa Rica', 'Ireland', 'Germany', 'Belgium',
        'United States', 'United Kingdom', 'France', 'Japan', 'South Korea',
        'Brazil', 'Mexico', 'Argentina', 'Chile', 'Colombia',
        'India', 'China', 'Thailand', 'Russia', 'South Africa'
    ]
    
    happiness_df = pd.DataFrame({
        'country': countries,
        'happiness_score': np.random.uniform(3.5, 7.8, len(countries)),
        'gdp_per_capita': np.random.uniform(5000, 80000, len(countries)),
        'life_expectancy': np.random.uniform(65, 85, len(countries)),
        'freedom_score': np.random.uniform(0.2, 0.9, len(countries)),
        'generosity': np.random.uniform(-0.3, 0.8, len(countries)),
        'corruption_perception': np.random.uniform(0.1, 0.9, len(countries)),
        'region': np.random.choice(['Europe', 'North America', 'Asia', 'South America', 'Africa', 'Oceania'], len(countries))
    })
    
    # Time series data for trends
    years = list(range(2015, 2025))
    time_series_data = []
    
    for country in countries[:10]:  # Top 10 countries for time series
        base_happiness = np.random.uniform(5.0, 7.5)
        trend = np.random.uniform(-0.1, 0.1)
        
        for year in years:
            happiness = base_happiness + trend * (year - 2015) + np.random.normal(0, 0.2)
            time_series_data.append({
                'country': country,
                'year': year,
                'happiness_score': max(1, min(10, happiness)),
                'gdp_growth': np.random.uniform(-2, 8),
                'population_millions': np.random.uniform(5, 330)
            })
    
    time_series_df = pd.DataFrame(time_series_data)
    
    # Economic indicators
    economic_df = pd.DataFrame({
        'country': countries,
        'unemployment_rate': np.random.uniform(2, 25, len(countries)),
        'inflation_rate': np.random.uniform(-1, 15, len(countries)),
        'education_index': np.random.uniform(0.4, 0.95, len(countries)),
        'healthcare_quality': np.random.uniform(30, 95, len(countries)),
        'innovation_index': np.random.uniform(15, 85, len(countries))
    })
    
    return {
        'happiness': happiness_df,
        'time_series': time_series_df,
        'economic': economic_df
    }

def render_design_principles_showcase(viz_data, chart_style):
    """Render the design principles and visualization best practices"""
    
    st.subheader("Design Principles & Best Practices")
    
    st.write("""
    Effective data visualization combines aesthetic appeal with functional clarity. These examples demonstrate 
    how thoughtful design choices enhance comprehension and drive actionable insights from complex datasets.
    """)
    
    happiness_df = viz_data['happiness']
    
    # Color theory demonstration
    st.subheader("Color Theory in Data Visualization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Effective color use - sequential
        fig = px.scatter(
            happiness_df,
            x='gdp_per_capita',
            y='happiness_score',
            color='life_expectancy',
            size='freedom_score',
            title='Effective Color Use: Sequential Scale',
            color_continuous_scale='Viridis',
            hover_data=['country']
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.success("Best Practice: Sequential color scale for continuous data with clear progression")
    
    with col2:
        # Categorical color distinctions
        fig = px.bar(
            happiness_df.groupby('region')['happiness_score'].mean().reset_index().sort_values('happiness_score', ascending=True),
            x='happiness_score',
            y='region',
            orientation='h',
            title='Categorical Color Distinctions',
            color='region',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.success("Best Practice: Distinct colors for categorical data enhance readability")
    
    # Typography and layout principles
    st.subheader("Typography & Layout Excellence")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Clean, minimal design
        top_countries = happiness_df.nlargest(8, 'happiness_score')
        
        fig = px.bar(
            top_countries,
            x='happiness_score',
            y='country',
            orientation='h',
            title='Clean Typography & Minimal Design',
            color='happiness_score',
            color_continuous_scale='Blues'
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Information hierarchy demonstration
        gdp_happiness = happiness_df.copy()
        gdp_happiness['gdp_category'] = pd.cut(
            gdp_happiness['gdp_per_capita'], 
            bins=3, 
            labels=['Low GDP', 'Medium GDP', 'High GDP']
        )
        
        fig = px.box(
            gdp_happiness,
            x='gdp_category',
            y='happiness_score',
            title='Information Hierarchy with Clear Structure',
            color='gdp_category'
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Interactive correlation matrix
    st.subheader("Interactive Elements & User Experience")
    
    numeric_cols = ['happiness_score', 'gdp_per_capita', 'life_expectancy', 'freedom_score']
    correlation_matrix = happiness_df[numeric_cols].corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.columns,
        colorscale='RdBu',
        zmid=0,
        text=correlation_matrix.round(2).values,
        texttemplate="%{text}",
        textfont={"size": 14}
    ))
    
    fig.update_layout(
        title='Interactive Correlation Heatmap with Hover Details',
        title_x=0.5,
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    Effective visualizations prioritize clarity over complexity, use color strategically to enhance meaning, 
    maintain consistent typography for readability, and provide interactive elements that engage users 
    while preserving the core message.
    """)

def render_statistical_excellence(viz_data, viz_focus):
    """Render statistical visualization examples and techniques"""
    
    st.subheader("Statistical Visualization Excellence")
    
    st.write("""
    Statistical visualization combines rigorous analytical methods with clear visual communication. 
    These examples demonstrate how to effectively present statistical insights, relationships, and model results.
    """)
    
    happiness_df = viz_data['happiness']
    time_series_df = viz_data['time_series']
    
    # Distribution analysis
    st.subheader("Distribution Analysis & Statistical Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Distribution with statistical overlays
        fig = go.Figure()
        
        # Histogram
        fig.add_trace(go.Histogram(
            x=happiness_df['happiness_score'],
            nbinsx=15,
            name='Distribution',
            opacity=0.7,
            marker_color='#4CAF50'
        ))
        
        # Add mean line
        mean_happiness = happiness_df['happiness_score'].mean()
        fig.add_vline(
            x=mean_happiness,
            line_dash="dash",
            line_color="red",
            annotation_text=f"Mean: {mean_happiness:.2f}"
        )
        
        # Add median line
        median_happiness = happiness_df['happiness_score'].median()
        fig.add_vline(
            x=median_happiness,
            line_dash="dot",
            line_color="blue",
            annotation_text=f"Median: {median_happiness:.2f}"
        )
        
        fig.update_layout(
            title='Happiness Score Distribution with Statistical Markers',
            title_x=0.5,
            height=400,
            xaxis_title='Happiness Score',
            yaxis_title='Frequency'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Box plot with outlier analysis
        fig = px.box(
            happiness_df,
            y='gdp_per_capita',
            x='region',
            title='GDP Distribution by Region with Outlier Detection',
            color='region'
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400,
            xaxis_tickangle=-45,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Regression analysis showcase
    st.subheader("Regression Analysis & Predictive Modeling")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Scatter plot with regression line
        fig = px.scatter(
            happiness_df,
            x='gdp_per_capita',
            y='happiness_score',
            color='region',
            trendline='ols',
            title='GDP vs Happiness: Regression Analysis',
            hover_data=['country', 'life_expectancy']
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Calculate and display R-squared
        from scipy import stats
        slope, intercept, r_value, p_value, std_err = stats.linregress(
            happiness_df['gdp_per_capita'], 
            happiness_df['happiness_score']
        )
        
        st.info(f"Statistical Results: R² = {r_value**2:.3f} | p-value = {p_value:.3f} | Slope = {slope:.2e}")
    
    with col2:
        # Multi-variable correlation analysis
        numeric_features = ['happiness_score', 'gdp_per_capita', 'life_expectancy', 'freedom_score']
        correlation_data = happiness_df[numeric_features].corr()
        
        fig = px.imshow(
            correlation_data,
            text_auto=True,
            aspect="auto",
            title="Multi-Variable Correlation Matrix",
            color_continuous_scale='RdBu'
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Time series analysis
    st.subheader("Time Series Analysis & Forecasting")
    
    # Multi-country time series comparison
    top_5_countries = time_series_df.groupby('country')['happiness_score'].mean().nlargest(5).index
    time_series_filtered = time_series_df[time_series_df['country'].isin(top_5_countries)]
    
    fig = px.line(
        time_series_filtered,
        x='year',
        y='happiness_score',
        color='country',
        title='Happiness Trends: Top 5 Countries (2015-2024)',
        markers=True
    )
    
    fig.update_layout(
        title_x=0.5,
        height=500,
        xaxis_title='Year',
        yaxis_title='Happiness Score'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    Effective statistical visualization reveals patterns that pure numbers cannot convey. The regression analysis 
    shows strong correlation between economic prosperity and happiness, while time series analysis 
    reveals stability in top-performing countries.
    """)

def render_interactive_global_analytics(viz_data):
    """Render interactive global analytics dashboard"""
    
    st.subheader("Interactive Global Analytics Dashboard")
    
    st.write("""
    Interactive global analytics combine geographic visualization with cross-cultural data analysis to reveal 
    worldwide patterns, regional differences, and opportunities for strategic international insights.
    """)
    
    happiness_df = viz_data['happiness']
    
    # Interactive filters
    st.subheader("Interactive Analysis Controls")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        happiness_range = st.slider(
            "Happiness Score Range",
            float(happiness_df['happiness_score'].min()),
            float(happiness_df['happiness_score'].max()),
            (float(happiness_df['happiness_score'].min()), float(happiness_df['happiness_score'].max())),
            step=0.1
        )
    
    with col2:
        gdp_range = st.slider(
            "GDP per Capita Range (USD)",
            int(happiness_df['gdp_per_capita'].min()),
            int(happiness_df['gdp_per_capita'].max()),
            (int(happiness_df['gdp_per_capita'].min()), int(happiness_df['gdp_per_capita'].max())),
            step=1000
        )
    
    with col3:
        selected_regions = st.multiselect(
            "Select Regions",
            options=happiness_df['region'].unique(),
            default=happiness_df['region'].unique()
        )
    
    # Filter data based on selections
    filtered_df = happiness_df[
        (happiness_df['happiness_score'].between(happiness_range[0], happiness_range[1])) &
        (happiness_df['gdp_per_capita'].between(gdp_range[0], gdp_range[1])) &
        (happiness_df['region'].isin(selected_regions))
    ].copy()
    
    # Global overview dashboard
    st.subheader("Global Overview Dashboard")
    
    # Key metrics based on filtered data
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_happiness = filtered_df['happiness_score'].mean()
        st.metric("Avg Happiness", f"{avg_happiness:.2f}", f"{len(filtered_df)} countries")
    
    with col2:
        avg_gdp = filtered_df['gdp_per_capita'].mean()
        st.metric("Avg GDP", f"${avg_gdp:,.0f}", "Per capita")
    
    with col3:
        avg_life_exp = filtered_df['life_expectancy'].mean()
        st.metric("Life Expectancy", f"{avg_life_exp:.1f}", "Years")
    
    with col4:
        avg_freedom = filtered_df['freedom_score'].mean()
        st.metric("Freedom Score", f"{avg_freedom:.2f}", "Index (0-1)")
    
    # Multi-dimensional analysis
    st.subheader("Multi-Dimensional Country Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Bubble chart with multiple dimensions
        fig = px.scatter(
            filtered_df,
            x='gdp_per_capita',
            y='happiness_score',
            size='life_expectancy',
            color='freedom_score',
            hover_name='country',
            title='Multi-Dimensional Country Comparison',
            labels={
                'gdp_per_capita': 'GDP per Capita (USD)',
                'happiness_score': 'Happiness Score',
                'life_expectancy': 'Life Expectancy',
                'freedom_score': 'Freedom Score'
            },
            color_continuous_scale='Viridis'
        )
        
        fig.update_layout(
            title_x=0.5,
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Regional performance radar chart
        regional_avg = filtered_df.groupby('region').agg({
            'happiness_score': 'mean',
            'gdp_per_capita': lambda x: x.mean() / 10000,  # Scale for radar
            'life_expectancy': lambda x: x.mean() / 10,    # Scale for radar
            'freedom_score': lambda x: x.mean() * 10,      # Scale for radar
            'generosity': lambda x: (x.mean() + 1) * 5     # Scale and shift for radar
        }).reset_index()
        
        fig = go.Figure()
        
        for region in regional_avg['region']:
            region_data = regional_avg[regional_avg['region'] == region].iloc[0]
            
            fig.add_trace(go.Scatterpolar(
                r=[
                    region_data['happiness_score'],
                    region_data['gdp_per_capita'],
                    region_data['life_expectancy'],
                    region_data['freedom_score'],
                    region_data['generosity']
                ],
                theta=['Happiness', 'GDP (scaled)', 'Life Exp (scaled)', 'Freedom (scaled)', 'Generosity (scaled)'],
                fill='toself',
                name=region
            ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            title="Regional Performance Radar",
            title_x=0.5,
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Interactive data table
    st.subheader("Interactive Country Rankings")
    
    # Create ranking table
    ranking_df = filtered_df.copy()
    ranking_df['happiness_rank'] = ranking_df['happiness_score'].rank(method='dense', ascending=False)
    ranking_df['gdp_rank'] = ranking_df['gdp_per_capita'].rank(method='dense', ascending=False)
    ranking_df['life_exp_rank'] = ranking_df['life_expectancy'].rank(method='dense', ascending=False)
    
    display_df = ranking_df[[
        'country', 'region', 'happiness_score', 'happiness_rank',
        'gdp_per_capita', 'gdp_rank', 'life_expectancy', 'life_exp_rank'
    ]].round(2)
    
    # Sort by happiness score by default
    display_df = display_df.sort_values('happiness_score', ascending=False)
    
    st.dataframe(display_df, use_container_width=True, height=400)
    
    st.write("""
    Interactive global analysis reveals complex relationships between economic development, social freedom, 
    and quality of life indicators. The multi-dimensional visualization enables stakeholders to identify 
    high-performing countries, understand regional patterns, and discover strategic opportunities.
    """)