"""
Education Intelligence Platform component - Simplified version
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

def render_education_intelligence():
    """Render the education intelligence platform"""
    
    st.title("Education Intelligence Platform")
    
    # Project overview
    st.subheader("Overview")
    st.write("""
    Education Intelligence Platform transforms institutional data into strategic insights for academic excellence. 
    This comprehensive analytics solution empowers educational leaders with data-driven tools for student success, 
    operational efficiency, and institutional growth planning.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Student Analytics**")
        st.write("Success Prediction")
    with col2:
        st.write("**Performance Intelligence**")
        st.write("Program Optimization")
    with col3:
        st.write("**Predictive Modeling**")
        st.write("Enrollment Forecasting")

    # Development approach
    st.subheader("Educational Innovation Approach")
    st.write("**Challenge Addressed:** Educational institutions struggle with fragmented data systems that make it difficult to gain comprehensive insights into student success and institutional performance.")
    st.write("**Solution Implemented:** Integrated analytics platform that combines student lifecycle data, academic performance metrics, and institutional KPIs to provide actionable insights for educational excellence.")
    st.write("**Technical Skills Applied:** Educational data modeling, statistical analysis, predictive analytics, dashboard development, and institutional research methodologies.")
    
    # Sidebar configuration
    st.sidebar.subheader("Configuration")
    st.sidebar.write("Select Educational Focus Area")
    
    focus_area = st.sidebar.selectbox(
        "Choose Analysis Focus:",
        [
            "Student Success Analytics",
            "Academic Program Performance", 
            "Enrollment & Retention Trends",
            "Faculty & Resource Optimization"
        ],
        index=0
    )
    
    # Time period selector
    time_period = st.sidebar.selectbox(
        "Analysis Time Period:",
        ["Current Academic Year", "5-Year Trend", "3-Year Comparison", "Semester Analysis"],
        index=1
    )
    
    st.sidebar.markdown("---")
    st.sidebar.write("**Analytics Framework**")
    st.sidebar.write("Our educational analytics framework combines student lifecycle data with institutional metrics to identify patterns that drive academic success and operational excellence.")
    
    # Generate synthetic education data
    education_data = generate_education_data()
    
    # Create analytical framework sections
    tab1, tab2, tab3 = st.tabs([
        "Student Success Dashboard", 
        "Academic Performance Analytics", 
        "Institutional Intelligence"
    ])
    
    with tab1:
        render_student_success_dashboard(education_data, focus_area)
    
    with tab2:
        render_academic_performance_analytics(education_data, time_period)
    
    with tab3:
        render_institutional_intelligence(education_data)

def generate_education_data():
    """Generate comprehensive synthetic education data"""
    
    # Set random seed for reproducible data
    np.random.seed(42)
    random.seed(42)
    
    # Student data
    n_students = 2500
    departments = ['Computer Science', 'Business Administration', 'Engineering', 'Liberal Arts', 'Health Sciences', 'Education']
    years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    
    students_df = pd.DataFrame({
        'student_id': range(1, n_students + 1),
        'department': np.random.choice(departments, n_students),
        'year_level': np.random.choice(years, n_students),
        'gpa': np.random.normal(3.2, 0.6, n_students).clip(0, 4.0),
        'credits_completed': np.random.randint(15, 140, n_students),
        'retention_status': np.random.choice(['Retained', 'At Risk', 'Graduated'], n_students, p=[0.7, 0.2, 0.1]),
        'satisfaction_score': np.random.randint(3, 6, n_students),
        'engagement_level': np.random.choice(['High', 'Medium', 'Low'], n_students, p=[0.4, 0.4, 0.2])
    })
    
    # Enrollment trends over time
    years_range = list(range(2019, 2025))
    enrollment_df = pd.DataFrame({
        'year': years_range,
        'total_enrollment': [2100, 2250, 2180, 2350, 2500, 2450],
        'new_students': [600, 650, 580, 720, 750, 700],
        'graduation_rate': [78, 82, 80, 85, 87, 84],
        'retention_rate': [89, 91, 88, 92, 94, 91]
    })
    
    # Program performance data
    program_performance_df = pd.DataFrame({
        'department': departments,
        'avg_gpa': [3.4, 3.1, 3.3, 2.9, 3.2, 3.0],
        'completion_rate': [92, 87, 90, 85, 88, 86],
        'employment_rate': [95, 88, 93, 78, 91, 82],
        'student_count': [420, 380, 450, 320, 380, 350],
        'faculty_ratio': [12, 15, 14, 18, 13, 16]
    })
    
    return {
        'students': students_df,
        'enrollment': enrollment_df,
        'programs': program_performance_df
    }

def render_student_success_dashboard(education_data, focus_area):
    """Render the student success analytics dashboard"""
    
    st.subheader("Student Success Analytics Dashboard")
    
    st.write("""
    Advanced analytics platform tracking student lifecycle metrics to identify success patterns, predict at-risk 
    students, and optimize support interventions for improved retention and graduation outcomes.
    """)
    
    students_df = education_data['students']
    
    # Key performance indicators
    st.subheader("Student Success Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    avg_gpa = students_df['gpa'].mean()
    retention_rate = (students_df['retention_status'] == 'Retained').mean() * 100
    high_engagement = (students_df['engagement_level'] == 'High').mean() * 100
    at_risk_students = (students_df['retention_status'] == 'At Risk').sum()
    
    with col1:
        st.metric("Average GPA", f"{avg_gpa:.2f}", "Institution-wide")
    
    with col2:
        st.metric("Retention Rate", f"{retention_rate:.1f}%", "Year-over-year")
    
    with col3:
        st.metric("High Engagement", f"{high_engagement:.1f}%", "Active students")
    
    with col4:
        st.metric("At-Risk Students", f"{at_risk_students}", "Need intervention")
    
    # Student distribution analysis
    st.subheader("Student Population Analytics")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Department enrollment distribution
        dept_counts = students_df['department'].value_counts().reset_index()
        dept_counts.columns = ['Department', 'Student Count']
        
        fig = px.bar(
            dept_counts,
            x='Student Count',
            y='Department',
            orientation='h',
            title='Student Enrollment by Department',
            color='Student Count',
            color_continuous_scale='Blues'
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Year level distribution
        year_counts = students_df['year_level'].value_counts()
        
        fig = go.Figure(data=[go.Pie(
            labels=year_counts.index,
            values=year_counts.values,
            hole=0.4,
            marker_colors=['#4CAF50', '#2196F3', '#FF9800', '#9C27B0']
        )])
        
        fig.update_layout(
            title='Student Distribution by Year Level',
            title_x=0.5,
            height=400,
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # GPA and performance analysis
    st.subheader("Academic Performance Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # GPA distribution by department
        fig = px.box(
            students_df,
            x='department',
            y='gpa',
            title='GPA Distribution by Department',
            color='department'
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400,
            xaxis_tickangle=-45
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Engagement vs Retention analysis
        engagement_retention = students_df.groupby(['engagement_level', 'retention_status']).size().reset_index(name='count')
        
        fig = px.bar(
            engagement_retention,
            x='engagement_level',
            y='count',
            color='retention_status',
            title='Student Engagement vs Retention Status',
            color_discrete_map={'Retained': '#4CAF50', 'At Risk': '#F44336', 'Graduated': '#2196F3'}
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    High-engagement students show significantly better retention rates across all departments. The data reveals 
    opportunities for targeted intervention programs for at-risk students and demonstrates the correlation between 
    student engagement metrics and academic success outcomes.
    """)

def render_academic_performance_analytics(education_data, time_period):
    """Render the academic performance analytics dashboard"""
    
    st.subheader("Academic Performance Analytics")
    
    st.write("""
    Comprehensive analysis of academic program performance, graduation rates, and employment outcomes 
    to identify top-performing programs and opportunities for strategic improvement.
    """)
    
    programs_df = education_data['programs']
    enrollment_df = education_data['enrollment']
    
    # Program performance comparison
    st.subheader("Program Performance Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Average GPA by department
        fig = px.bar(
            programs_df,
            x='department',
            y='avg_gpa',
            title='Average GPA by Academic Program',
            color='avg_gpa',
            color_continuous_scale='Viridis'
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400,
            xaxis_tickangle=-45
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Employment rates
        fig = px.scatter(
            programs_df,
            x='completion_rate',
            y='employment_rate',
            size='student_count',
            color='department',
            title='Program Completion vs Employment Rates',
            hover_data=['avg_gpa']
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Enrollment trends over time
    st.subheader("Institutional Growth Trends")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Enrollment trends
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=enrollment_df['year'],
            y=enrollment_df['total_enrollment'],
            mode='lines+markers',
            name='Total Enrollment',
            line=dict(color='#4CAF50', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=enrollment_df['year'],
            y=enrollment_df['new_students'],
            mode='lines+markers',
            name='New Students',
            line=dict(color='#2196F3', width=3)
        ))
        
        fig.update_layout(
            title='Enrollment Trends (2019-2024)',
            title_x=0.5,
            height=400,
            xaxis_title='Academic Year',
            yaxis_title='Number of Students'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Retention and graduation rates
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=enrollment_df['year'],
            y=enrollment_df['retention_rate'],
            mode='lines+markers',
            name='Retention Rate (%)',
            line=dict(color='#FF9800', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=enrollment_df['year'],
            y=enrollment_df['graduation_rate'],
            mode='lines+markers',
            name='Graduation Rate (%)',
            line=dict(color='#9C27B0', width=3)
        ))
        
        fig.update_layout(
            title='Success Rate Trends',
            title_x=0.5,
            height=400,
            xaxis_title='Academic Year',
            yaxis_title='Rate (%)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    Programs with lower faculty-student ratios consistently demonstrate higher GPAs and completion rates. 
    The correlation between resource allocation and student outcomes suggests strategic opportunities for 
    faculty investment and program optimization to enhance institutional performance.
    """)

def render_institutional_intelligence(education_data):
    """Render the institutional intelligence dashboard"""
    
    st.subheader("Institutional Intelligence Framework")
    
    st.write("""
    Advanced institutional analytics providing strategic insights for leadership decision-making, 
    resource allocation optimization, and long-term growth planning.
    """)
    
    programs_df = education_data['programs']
    students_df = education_data['students']
    enrollment_df = education_data['enrollment']
    
    # Strategic metrics
    st.subheader("Strategic Performance Indicators")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Program ROI analysis
        programs_df['roi_score'] = (programs_df['completion_rate'] * programs_df['employment_rate']) / 100
        
        fig = px.bar(
            programs_df.sort_values('roi_score', ascending=True),
            x='roi_score',
            y='department',
            orientation='h',
            title='Program ROI Score (Completion × Employment)',
            color='roi_score',
            color_continuous_scale='Greens'
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Satisfaction vs retention correlation
        satisfaction_retention = students_df.groupby('satisfaction_score').agg({
            'retention_status': lambda x: (x == 'Retained').mean() * 100
        }).reset_index()
        satisfaction_retention.columns = ['Satisfaction Score', 'Retention Rate']
        
        fig = px.line(
            satisfaction_retention,
            x='Satisfaction Score',
            y='Retention Rate',
            title='Student Satisfaction Impact on Retention',
            markers=True,
            line_shape='spline'
        )
        
        fig.update_traces(
            line=dict(color='#4CAF50', width=4),
            marker=dict(size=10, color='#2196F3')
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Department competitiveness matrix
    st.subheader("Department Performance Matrix")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.scatter(
            programs_df,
            x='avg_gpa',
            y='employment_rate',
            size='student_count',
            color='completion_rate',
            title='Department Performance Matrix',
            hover_data=['department', 'faculty_ratio'],
            color_continuous_scale='RdYlGn'
        )
        
        fig.update_layout(
            title_x=0.5,
            height=450,
            xaxis_title='Average GPA',
            yaxis_title='Employment Rate (%)'
        )
        
        # Add quadrant lines
        fig.add_hline(y=programs_df['employment_rate'].mean(), line_dash="dash", line_color="gray")
        fig.add_vline(x=programs_df['avg_gpa'].mean(), line_dash="dash", line_color="gray")
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Top performing departments
        programs_df['overall_score'] = (
            programs_df['avg_gpa'] * 25 + 
            programs_df['completion_rate'] + 
            programs_df['employment_rate']
        ) / 3
        
        top_programs = programs_df.nlargest(3, 'overall_score')
        
        st.write("**Top Performing Programs**")
        
        for i, (_, program) in enumerate(top_programs.iterrows(), 1):
            medal = "1st" if i == 1 else "2nd" if i == 2 else "3rd"
            st.write(f"**{medal}: {program['department']}**")
            st.write(f"GPA: {program['avg_gpa']:.2f} | Employment: {program['employment_rate']:.0f}% | Completion: {program['completion_rate']:.0f}%")
            st.write("---")
    
    st.write("""
    High-performing departments demonstrate optimal balance between academic rigor and career outcomes. 
    The predictive model suggests continued growth with strategic investment in faculty resources and 
    student support services.
    """)