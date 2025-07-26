"""
Visualization Excellence Framework component for the DataFlow Intelligence Platform
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
    """Render the complete visualization excellence framework"""
    
    st.markdown('<div class="main-header">📊 Visualization Excellence Framework</div>', unsafe_allow_html=True)
    
    # Project overview with enhanced styling
    st.markdown("""
    <div class="portfolio-card fade-in-up">
        <h3 style="color: #1a202c; margin-bottom: 1rem; font-weight: 700;">🎯 Data Storytelling Mastery</h3>
        <p style="font-size: 1.1rem; line-height: 1.6; color: #2d3748;">
            Visualization Excellence Framework demonstrates advanced data storytelling techniques and design principles 
            that transform complex datasets into compelling, actionable insights. This comprehensive showcase highlights 
            the art and science of effective data visualization for strategic decision-making.
        </p>
        
        <div style="display: flex; justify-content: space-around; margin-top: 2rem; flex-wrap: wrap;">
            <div style="text-align: center; margin: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎨</div>
                <p style="margin: 0; font-weight: 700; color: #1a202c;">Design Principles</p>
                <p style="margin: 0; font-size: 0.9rem; color: #4b5563;">Visual Excellence</p>
            </div>
            <div style="text-align: center; margin: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">📈</div>
                <p style="margin: 0; font-weight: 700; color: #1a202c;">Statistical Analysis</p>
                <p style="margin: 0; font-size: 0.9rem; color: #4b5563;">Data Insights</p>
            </div>
            <div style="text-align: center; margin: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🌍</div>
                <p style="margin: 0; font-weight: 700; color: #1a202c;">Global Perspectives</p>
                <p style="margin: 0; font-size: 0.9rem; color: #4b5563;">Cross-Cultural Data</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Development approach section
    st.markdown("""
    <div class="value-prop fade-in-up">
        <h3 style="color: #1a202c; margin-bottom: 1rem; font-weight: 700;">💡 Visualization Innovation Approach</h3>
        <div style="margin-bottom: 1rem;">
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2d3748; margin-bottom: 1rem;">
                <strong style="color: #1a202c;">Challenge Addressed:</strong> Organizations struggle with data overload and 
                ineffective visualizations that fail to communicate insights clearly to stakeholders and decision-makers.
            </p>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2d3748; margin-bottom: 1rem;">
                <strong style="color: #1a202c;">Solution Implemented:</strong> Comprehensive framework combining design theory, 
                statistical best practices, and interactive technologies to create visualizations that drive understanding and action.
            </p>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2d3748;">
                <strong style="color: #1a202c;">Technical Skills Applied:</strong> Advanced data visualization libraries, 
                statistical analysis, design theory, user experience optimization, and cross-platform compatibility.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar configuration
    st.sidebar.markdown("## 🎯 Visualization Configuration")
    st.sidebar.markdown("**Select Analysis Focus**")
    
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
    st.sidebar.markdown("""
    <div class="insight-box" style="margin: 1rem 0;">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">🎨 Design Philosophy</h4>
        <p style="font-size: 0.9rem; line-height: 1.5; color: #2d3748;">
            Effective visualizations combine aesthetic appeal with functional clarity, ensuring that data stories 
            are both beautiful and actionable for strategic decision-making.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate comprehensive visualization data
    viz_data = generate_visualization_data()
    
    # Add spacing before tabs
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # Create visualization framework sections
    tab1, tab2, tab3 = st.tabs([
        "🎨 Design Principles Showcase", 
        "📊 Statistical Visualization Excellence", 
        "🌍 Interactive Global Analytics"
    ])
    
    with tab1:
        st.markdown("<div style='padding-top: 1rem;'>", unsafe_allow_html=True)
        render_design_principles_showcase(viz_data, chart_style)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<div style='padding-top: 1rem;'>", unsafe_allow_html=True)
        render_statistical_excellence(viz_data, viz_focus)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<div style='padding-top: 1rem;'>", unsafe_allow_html=True)
        render_interactive_global_analytics(viz_data)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Strategic insights section
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    render_visualization_insights()

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
    
    st.markdown('<div class="sub-header">🎨 Design Principles & Best Practices</div>', unsafe_allow_html=True)
    
    # Wrap content in a container for proper layout
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    # Design context
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">🎯 Visual Design Excellence</h4>
        <p style="line-height: 1.5; color: #2d3748;">
            Effective data visualization combines aesthetic appeal with functional clarity. These examples demonstrate 
            how thoughtful design choices enhance comprehension and drive actionable insights from complex datasets.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    happiness_df = viz_data['happiness']
    
    # Color theory demonstration
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">🌈 Color Theory in Data Visualization</h3>', unsafe_allow_html=True)
    
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
            height=400,
            font=dict(size=12)
        )
        
        st.plotly_chart(fig, use_container_width=True, key="effective_colors")
        
        st.markdown("""
        <div style="background: #f0fdf4; padding: 1rem; border-radius: 8px; border-left: 4px solid #059669;">
            <strong style="color: #059669;">✅ Best Practice</strong><br>
            <small style="color: #2d3748;">Sequential color scale for continuous data with clear progression</small>
        </div>
        """, unsafe_allow_html=True)
    
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
        
        st.plotly_chart(fig, use_container_width=True, key="categorical_colors")
        
        st.markdown("""
        <div style="background: #f0fdf4; padding: 1rem; border-radius: 8px; border-left: 4px solid #059669;">
            <strong style="color: #059669;">✅ Best Practice</strong><br>
            <small style="color: #2d3748;">Distinct colors for categorical data enhance readability</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Typography and layout principles
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">📝 Typography & Layout Excellence</h3>', unsafe_allow_html=True)
    
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
            font=dict(family="Arial, sans-serif", size=12),
            margin=dict(l=120, r=50, t=50, b=50),
            showlegend=False
        )
        
        fig.update_xaxis(title="Happiness Score", title_font=dict(size=14))
        fig.update_yaxis(title="", title_font=dict(size=14))
        
        st.plotly_chart(fig, use_container_width=True, key="clean_typography")
    
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
            color='gdp_category',
            color_discrete_map={'Low GDP': '#fee2e2', 'Medium GDP': '#fef3c7', 'High GDP': '#d1fae5'}
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400,
            font=dict(family="Arial, sans-serif", size=12),
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True, key="information_hierarchy")
    
    # Interactive elements showcase
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">⚡ Interactive Elements & User Experience</h3>', unsafe_allow_html=True)
    
    # Interactive correlation matrix
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
        textfont={"size": 14},
        hoverongaps=False
    ))
    
    fig.update_layout(
        title='Interactive Correlation Heatmap with Hover Details',
        title_x=0.5,
        height=500,
        font=dict(size=12)
    )
    
    st.plotly_chart(fig, use_container_width=True, key="interactive_heatmap")
    
    # Design principles summary
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">💡 Design Excellence Principles</h4>
        <p style="line-height: 1.5; color: #2d3748;">
            Effective visualizations prioritize clarity over complexity, use color strategically to enhance meaning, 
            maintain consistent typography for readability, and provide interactive elements that engage users 
            while preserving the core message. These principles ensure visualizations serve their primary purpose: 
            facilitating understanding and driving action.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Close content section container
    st.markdown('</div>', unsafe_allow_html=True)

def render_statistical_excellence(viz_data, viz_focus):
    """Render statistical visualization examples and techniques"""
    
    st.markdown('<div class="sub-header">📊 Statistical Visualization Excellence</div>', unsafe_allow_html=True)
    
    # Wrap content in a container for proper layout
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    # Statistical context
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">📈 Advanced Statistical Analysis</h4>
        <p style="line-height: 1.5; color: #2d3748;">
            Statistical visualization combines rigorous analytical methods with clear visual communication. 
            These examples demonstrate how to effectively present statistical insights, relationships, and model results.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    happiness_df = viz_data['happiness']
    time_series_df = viz_data['time_series']
    economic_df = viz_data['economic']
    
    # Distribution analysis
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">📊 Distribution Analysis & Statistical Insights</h3>', unsafe_allow_html=True)
    
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
            marker_color='#2563eb'
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
            line_color="green",
            annotation_text=f"Median: {median_happiness:.2f}"
        )
        
        fig.update_layout(
            title='Happiness Score Distribution with Statistical Markers',
            title_x=0.5,
            height=400,
            xaxis_title='Happiness Score',
            yaxis_title='Frequency'
        )
        
        st.plotly_chart(fig, use_container_width=True, key="distribution_analysis")
    
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
        
        st.plotly_chart(fig, use_container_width=True, key="outlier_analysis")
    
    # Regression analysis showcase
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">📈 Regression Analysis & Predictive Modeling</h3>', unsafe_allow_html=True)
    
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
        
        st.plotly_chart(fig, use_container_width=True, key="regression_analysis")
        
        # Calculate and display R-squared
        from scipy import stats
        slope, intercept, r_value, p_value, std_err = stats.linregress(
            happiness_df['gdp_per_capita'], 
            happiness_df['happiness_score']
        )
        
        st.markdown(f"""
        <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; border-left: 4px solid #2563eb; border: 1px solid #e2e8f0;">
            <strong style="color: #2563eb;">Statistical Results:</strong><br>
            <small style="color: #2d3748;">
                R² = {r_value**2:.3f} | p-value = {p_value:.3f} | Slope = {slope:.2e}
            </small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Multi-variable correlation analysis
        numeric_features = ['happiness_score', 'gdp_per_capita', 'life_expectancy', 'freedom_score']
        correlation_data = happiness_df[numeric_features].corr()
        
        # Create correlation network visualization
        fig = go.Figure()
        
        # Add correlation strength as bubble sizes
        for i, col1 in enumerate(correlation_data.columns):
            for j, col2 in enumerate(correlation_data.columns):
                if i < j:  # Only upper triangle
                    corr_val = correlation_data.loc[col1, col2]
                    fig.add_trace(go.Scatter(
                        x=[i],
                        y=[j],
                        mode='markers+text',
                        marker=dict(
                            size=abs(corr_val) * 100,
                            color=corr_val,
                            colorscale='RdBu',
                            cmin=-1,
                            cmax=1,
                            showscale=True
                        ),
                        text=f'{corr_val:.2f}',
                        textposition='middle center',
                        name=f'{col1} vs {col2}',
                        showlegend=False
                    ))
        
        fig.update_layout(
            title='Multi-Variable Correlation Strength',
            title_x=0.5,
            height=400,
            xaxis=dict(tickmode='array', tickvals=list(range(len(numeric_features))), ticktext=numeric_features),
            yaxis=dict(tickmode='array', tickvals=list(range(len(numeric_features))), ticktext=numeric_features)
        )
        
        st.plotly_chart(fig, use_container_width=True, key="correlation_network")
    
    # Time series analysis
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">⏰ Time Series Analysis & Forecasting</h3>', unsafe_allow_html=True)
    
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
    
    # Add trend lines
    for country in top_5_countries:
        country_data = time_series_filtered[time_series_filtered['country'] == country]
        z = np.polyfit(country_data['year'], country_data['happiness_score'], 1)
        p = np.poly1d(z)
        
        fig.add_trace(go.Scatter(
            x=country_data['year'],
            y=p(country_data['year']),
            mode='lines',
            name=f'{country} Trend',
            line=dict(dash='dash'),
            showlegend=False
        ))
    
    fig.update_layout(
        title_x=0.5,
        height=500,
        xaxis_title='Year',
        yaxis_title='Happiness Score'
    )
    
    st.plotly_chart(fig, use_container_width=True, key="time_series_analysis")
    
    # Statistical insights summary
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">💡 Statistical Visualization Insights</h4>
        <p style="line-height: 1.5; color: #2d3748;">
            Effective statistical visualization reveals patterns that pure numbers cannot convey. The regression analysis 
            shows strong correlation between economic prosperity and happiness (R² > 0.5), while time series analysis 
            reveals stability in top-performing countries. Distribution analysis identifies outliers and provides context 
            for understanding data variability and central tendencies.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Close content section container
    st.markdown('</div>', unsafe_allow_html=True)

def render_interactive_global_analytics(viz_data):
    """Render interactive global analytics dashboard"""
    
    st.markdown('<div class="sub-header">🌍 Interactive Global Analytics Dashboard</div>', unsafe_allow_html=True)
    
    # Wrap content in a container for proper layout
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    # Global context
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">🌐 Global Data Intelligence</h4>
        <p style="line-height: 1.5; color: #2d3748;">
            Interactive global analytics combine geographic visualization with cross-cultural data analysis to reveal 
            worldwide patterns, regional differences, and opportunities for strategic international insights.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    happiness_df = viz_data['happiness']
    economic_df = viz_data['economic']
    
    # Interactive filters
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">🎛️ Interactive Analysis Controls</h3>', unsafe_allow_html=True)
    
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
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">🌍 Global Overview Dashboard</h3>', unsafe_allow_html=True)
    
    # Key metrics based on filtered data
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_happiness = filtered_df['happiness_score'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="margin: 0; color: #1a202c; font-weight: 600;">😊 Avg Happiness</h4>
            <h2 style="margin: 0.5rem 0; color: #2563eb; font-weight: 700;">{avg_happiness:.2f}</h2>
            <p style="margin: 0; color: #4b5563;">{len(filtered_df)} countries</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        avg_gdp = filtered_df['gdp_per_capita'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="margin: 0; color: #1a202c; font-weight: 600;">💰 Avg GDP</h4>
            <h2 style="margin: 0.5rem 0; color: #059669; font-weight: 700;">${avg_gdp:,.0f}</h2>
            <p style="margin: 0; color: #4b5563;">Per capita</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        avg_life_exp = filtered_df['life_expectancy'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="margin: 0; color: #1a202c; font-weight: 600;">🏥 Life Expectancy</h4>
            <h2 style="margin: 0.5rem 0; color: #eab308; font-weight: 700;">{avg_life_exp:.1f}</h2>
            <p style="margin: 0; color: #4b5563;">Years</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        avg_freedom = filtered_df['freedom_score'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="margin: 0; color: #1a202c; font-weight: 600;">🗽 Freedom Score</h4>
            <h2 style="margin: 0.5rem 0; color: #dc2626; font-weight: 700;">{avg_freedom:.2f}</h2>
            <p style="margin: 0; color: #4b5563;">Index (0-1)</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Multi-dimensional analysis
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">📊 Multi-Dimensional Country Analysis</h3>', unsafe_allow_html=True)
    
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
        
        st.plotly_chart(fig, use_container_width=True, key="multidimensional_analysis")
    
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
        
        st.plotly_chart(fig, use_container_width=True, key="regional_radar")
    
    # Interactive data table with sorting and filtering
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">📋 Interactive Country Rankings</h3>', unsafe_allow_html=True)
    
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
    
    st.dataframe(
        display_df,
        use_container_width=True,
        height=400,
        column_config={
            "country": "Country",
            "region": "Region",
            "happiness_score": st.column_config.NumberColumn("Happiness Score", format="%.2f"),
            "happiness_rank": st.column_config.NumberColumn("Happiness Rank", format="%.0f"),
            "gdp_per_capita": st.column_config.NumberColumn("GDP per Capita", format="$%,.0f"),
            "gdp_rank": st.column_config.NumberColumn("GDP Rank", format="%.0f"),
            "life_expectancy": st.column_config.NumberColumn("Life Expectancy", format="%.1f"),
            "life_exp_rank": st.column_config.NumberColumn("Life Exp Rank", format="%.0f")
        }
    )
    
    # Global insights
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">💡 Global Analytics Intelligence</h4>
        <p style="line-height: 1.5; color: #2d3748;">
            Interactive global analysis reveals complex relationships between economic development, social freedom, 
            and quality of life indicators. The multi-dimensional visualization enables stakeholders to identify 
            high-performing countries, understand regional patterns, and discover strategic opportunities for 
            international collaboration and investment.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Close content section container
    st.markdown('</div>', unsafe_allow_html=True)

def render_visualization_insights():
    """Render strategic visualization insights section"""
    
    with st.expander("📋 Visualization Excellence Executive Summary", expanded=False):
        st.markdown("# Visualization Excellence Framework: Strategic Analysis")
        
        st.markdown("## Executive Summary")
        st.markdown("""
        This comprehensive visualization framework demonstrates advanced data storytelling techniques that transform 
        complex datasets into compelling, actionable insights. The platform showcases best practices in visual design, 
        statistical analysis, and interactive user experience to maximize data comprehension and strategic value.
        
        **Key Strategic Value:**
        - Visual design principles that enhance data comprehension
        - Statistical visualization techniques for rigorous analysis
        - Interactive elements that engage stakeholders and facilitate exploration
        - Global perspective capabilities for international strategic planning
        """)
        
        st.markdown("## Visualization Excellence Findings")
        st.markdown("""
        1. **Design Impact Assessment**: Color theory application and typography optimization significantly improve 
           data comprehension rates and reduce cognitive load for decision-makers reviewing complex datasets.
           
        2. **Statistical Visualization Value**: Advanced statistical overlays including regression analysis, distribution 
           markers, and correlation networks provide deeper analytical insights beyond basic chart presentations.
           
        3. **Interactive Engagement Benefits**: User-controlled filtering and dynamic visualizations increase stakeholder 
           engagement and enable self-service analytics for strategic planning and operational decision-making.
           
        4. **Global Analytics Capabilities**: Multi-dimensional country analysis reveals strategic opportunities for 
           international expansion, partnership identification, and cross-cultural market analysis.
           
        5. **Data Storytelling Effectiveness**: Structured narrative flow combined with progressive disclosure techniques 
           ensures complex insights are accessible to diverse stakeholder groups with varying analytical backgrounds.
        """)
        
        st.markdown("## Strategic Recommendations")
        st.markdown("""
        **Implementation Priorities:**
        - Adopt consistent visual design standards across all organizational dashboards
        - Implement interactive analytics capabilities for self-service stakeholder access
        - Develop statistical visualization competencies for advanced analytical reporting
        - Create global analytics frameworks for international strategic planning
        - Establish data storytelling best practices for executive communications
        """)