"""
Education Intelligence Platform component for the DataFlow Intelligence Platform
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

def render_education_intelligence():
    """Render the complete education intelligence platform"""
    
    st.markdown('<div class="main-header">🎓 Education Intelligence Platform</div>', unsafe_allow_html=True)
    
    # Project overview with enhanced styling
    st.markdown("""
    <div class="portfolio-card fade-in-up">
        <h3 style="color: #1a202c; margin-bottom: 1rem; font-weight: 700;">🎯 Institutional Excellence Analytics</h3>
        <p style="font-size: 1.1rem; line-height: 1.6; color: #2d3748;">
            Education Intelligence Platform transforms institutional data into strategic insights for academic excellence. 
            This comprehensive analytics solution empowers educational leaders with data-driven tools for student success, 
            operational efficiency, and institutional growth planning.
        </p>
        
        <div style="display: flex; justify-content: space-around; margin-top: 2rem; flex-wrap: wrap;">
            <div style="text-align: center; margin: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">📊</div>
                <p style="margin: 0; font-weight: 700; color: #1a202c;">Student Analytics</p>
                <p style="margin: 0; font-size: 0.9rem; color: #4b5563;">Success Prediction</p>
            </div>
            <div style="text-align: center; margin: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎯</div>
                <p style="margin: 0; font-weight: 700; color: #1a202c;">Performance Intelligence</p>
                <p style="margin: 0; font-size: 0.9rem; color: #4b5563;">Program Optimization</p>
            </div>
            <div style="text-align: center; margin: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">📈</div>
                <p style="margin: 0; font-weight: 700; color: #1a202c;">Predictive Modeling</p>
                <p style="margin: 0; font-size: 0.9rem; color: #4b5563;">Enrollment Forecasting</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Development approach section
    st.markdown("""
    <div class="value-prop fade-in-up">
        <h3 style="color: #1a202c; margin-bottom: 1rem; font-weight: 700;">💡 Educational Innovation Approach</h3>
        <div style="margin-bottom: 1rem;">
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2d3748; margin-bottom: 1rem;">
                <strong style="color: #1a202c;">Challenge Addressed:</strong> Educational institutions struggle with fragmented data systems 
                that make it difficult to gain comprehensive insights into student success and institutional performance.
            </p>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2d3748; margin-bottom: 1rem;">
                <strong style="color: #1a202c;">Solution Implemented:</strong> Integrated analytics platform that combines student lifecycle data, 
                academic performance metrics, and institutional KPIs to provide actionable insights for educational excellence.
            </p>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2d3748;">
                <strong style="color: #1a202c;">Technical Skills Applied:</strong> Educational data modeling, statistical analysis, 
                predictive analytics, dashboard development, and institutional research methodologies.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar configuration
    st.sidebar.markdown("## 🎯 Institution Analysis Configuration")
    st.sidebar.markdown("**Select Educational Focus Area**")
    
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
    st.sidebar.markdown("""
    <div class="insight-box" style="margin: 1rem 0;">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">💡 Analytics Framework</h4>
        <p style="font-size: 0.9rem; line-height: 1.5; color: #2d3748;">
            Our educational analytics framework combines student lifecycle data with institutional metrics to identify 
            patterns that drive academic success and operational excellence.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate synthetic education data
    education_data = generate_education_data()
    
    # Add spacing before tabs
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # Create analytical framework sections
    tab1, tab2, tab3 = st.tabs([
        "📊 Student Success Dashboard", 
        "🎯 Academic Performance Analytics", 
        "📈 Institutional Intelligence"
    ])
    
    with tab1:
        st.markdown("<div style='padding-top: 1rem;'>", unsafe_allow_html=True)
        render_student_success_dashboard(education_data, focus_area)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<div style='padding-top: 1rem;'>", unsafe_allow_html=True)
        render_academic_performance_analytics(education_data, time_period)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<div style='padding-top: 1rem;'>", unsafe_allow_html=True)
        render_institutional_intelligence(education_data)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Strategic insights section
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    render_educational_insights()

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
    
    st.markdown('<div class="sub-header">📊 Student Success Analytics Dashboard</div>', unsafe_allow_html=True)
    
    # Wrap content in a container for proper layout
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    # Success context
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">🎯 Student Success Intelligence</h4>
        <p style="line-height: 1.5; color: #2d3748;">
            Advanced analytics platform tracking student lifecycle metrics to identify success patterns, predict at-risk 
            students, and optimize support interventions for improved retention and graduation outcomes.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    students_df = education_data['students']
    
    # Key performance indicators
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">🎯 Student Success Metrics</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    avg_gpa = students_df['gpa'].mean()
    retention_rate = (students_df['retention_status'] == 'Retained').mean() * 100
    high_engagement = (students_df['engagement_level'] == 'High').mean() * 100
    at_risk_students = (students_df['retention_status'] == 'At Risk').sum()
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="margin: 0; color: #1a202c; font-weight: 600;">📚 Average GPA</h4>
            <h2 style="margin: 0.5rem 0; color: #2563eb; font-weight: 700;">{avg_gpa:.2f}</h2>
            <p style="margin: 0; color: #4b5563;">Institution-wide</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="margin: 0; color: #1a202c; font-weight: 600;">✅ Retention Rate</h4>
            <h2 style="margin: 0.5rem 0; color: #059669; font-weight: 700;">{retention_rate:.1f}%</h2>
            <p style="margin: 0; color: #4b5563;">Year-over-year</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="margin: 0; color: #1a202c; font-weight: 600;">🔥 High Engagement</h4>
            <h2 style="margin: 0.5rem 0; color: #eab308; font-weight: 700;">{high_engagement:.1f}%</h2>
            <p style="margin: 0; color: #4b5563;">Active students</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="margin: 0; color: #1a202c; font-weight: 600;">⚠️ At-Risk Students</h4>
            <h2 style="margin: 0.5rem 0; color: #dc2626; font-weight: 700;">{at_risk_students}</h2>
            <p style="margin: 0; color: #4b5563;">Need intervention</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Student distribution analysis
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">📊 Student Population Analytics</h3>', unsafe_allow_html=True)
    
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
            title_font_size=16,
            title_x=0.5,
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True, key="dept_enrollment")
    
    with col2:
        # Year level distribution
        year_counts = students_df['year_level'].value_counts()
        
        fig = go.Figure(data=[go.Pie(
            labels=year_counts.index,
            values=year_counts.values,
            hole=0.4,
            marker_colors=['#2563eb', '#1d4ed8', '#1e40af', '#3b82f6']
        )])
        
        fig.update_layout(
            title='Student Distribution by Year Level',
            title_x=0.5,
            height=400,
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True, key="year_distribution")
    
    # GPA and performance analysis
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">📈 Academic Performance Analysis</h3>', unsafe_allow_html=True)
    
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
        
        st.plotly_chart(fig, use_container_width=True, key="gpa_by_dept")
    
    with col2:
        # Engagement vs Retention analysis
        engagement_retention = students_df.groupby(['engagement_level', 'retention_status']).size().reset_index(name='count')
        
        fig = px.bar(
            engagement_retention,
            x='engagement_level',
            y='count',
            color='retention_status',
            title='Student Engagement vs Retention Status',
            color_discrete_map={'Retained': '#059669', 'At Risk': '#dc2626', 'Graduated': '#2563eb'}
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True, key="engagement_retention")
    
    # Strategic insight
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">💡 Student Success Intelligence</h4>
        <p style="line-height: 1.5; color: #2d3748;">
            High-engagement students show significantly better retention rates across all departments. The data reveals 
            opportunities for targeted intervention programs for at-risk students and demonstrates the correlation between 
            student engagement metrics and academic success outcomes.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Close content section container
    st.markdown('</div>', unsafe_allow_html=True)

def render_academic_performance_analytics(education_data, time_period):
    """Render the academic performance analytics dashboard"""
    
    st.markdown('<div class="sub-header">🎯 Academic Performance Analytics</div>', unsafe_allow_html=True)
    
    # Wrap content in a container for proper layout
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    # Performance context
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">📊 Program Excellence Metrics</h4>
        <p style="line-height: 1.5; color: #2d3748;">
            Comprehensive analysis of academic program performance, graduation rates, and employment outcomes 
            to identify top-performing programs and opportunities for strategic improvement.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    programs_df = education_data['programs']
    enrollment_df = education_data['enrollment']
    
    # Program performance comparison
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">🏆 Program Performance Comparison</h3>', unsafe_allow_html=True)
    
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
        
        st.plotly_chart(fig, use_container_width=True, key="gpa_by_program")
    
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
        
        st.plotly_chart(fig, use_container_width=True, key="completion_employment")
    
    # Enrollment trends over time
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">📈 Institutional Growth Trends</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Enrollment trends
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=enrollment_df['year'],
            y=enrollment_df['total_enrollment'],
            mode='lines+markers',
            name='Total Enrollment',
            line=dict(color='#2563eb', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=enrollment_df['year'],
            y=enrollment_df['new_students'],
            mode='lines+markers',
            name='New Students',
            line=dict(color='#059669', width=3)
        ))
        
        fig.update_layout(
            title='Enrollment Trends (2019-2024)',
            title_x=0.5,
            height=400,
            xaxis_title='Academic Year',
            yaxis_title='Number of Students'
        )
        
        st.plotly_chart(fig, use_container_width=True, key="enrollment_trends")
    
    with col2:
        # Retention and graduation rates
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=enrollment_df['year'],
            y=enrollment_df['retention_rate'],
            mode='lines+markers',
            name='Retention Rate (%)',
            line=dict(color='#eab308', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=enrollment_df['year'],
            y=enrollment_df['graduation_rate'],
            mode='lines+markers',
            name='Graduation Rate (%)',
            line=dict(color='#dc2626', width=3)
        ))
        
        fig.update_layout(
            title='Success Rate Trends',
            title_x=0.5,
            height=400,
            xaxis_title='Academic Year',
            yaxis_title='Rate (%)'
        )
        
        st.plotly_chart(fig, use_container_width=True, key="success_rates")
    
    # Faculty-student ratios
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">👥 Resource Optimization Analysis</h3>', unsafe_allow_html=True)
    
    fig = px.scatter(
        programs_df,
        x='faculty_ratio',
        y='avg_gpa',
        size='student_count',
        color='completion_rate',
        title='Faculty-Student Ratio Impact on Academic Performance',
        hover_data=['department', 'employment_rate'],
        color_continuous_scale='RdYlBu_r'
    )
    
    fig.update_layout(
        title_x=0.5,
        height=450,
        xaxis_title='Faculty-Student Ratio',
        yaxis_title='Average GPA'
    )
    
    st.plotly_chart(fig, use_container_width=True, key="faculty_ratio_analysis")
    
    # Performance insights
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">💡 Academic Excellence Insights</h4>
        <p style="line-height: 1.5; color: #2d3748;">
            Programs with lower faculty-student ratios consistently demonstrate higher GPAs and completion rates. 
            The correlation between resource allocation and student outcomes suggests strategic opportunities for 
            faculty investment and program optimization to enhance institutional performance.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Close content section container
    st.markdown('</div>', unsafe_allow_html=True)

def render_institutional_intelligence(education_data):
    """Render the institutional intelligence dashboard"""
    
    st.markdown('<div class="sub-header">📈 Institutional Intelligence Framework</div>', unsafe_allow_html=True)
    
    # Wrap content in a container for proper layout
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    # Intelligence context
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">🎯 Strategic Planning Intelligence</h4>
        <p style="line-height: 1.5; color: #2d3748;">
            Advanced institutional analytics providing strategic insights for leadership decision-making, 
            resource allocation optimization, and long-term growth planning.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    programs_df = education_data['programs']
    students_df = education_data['students']
    enrollment_df = education_data['enrollment']
    
    # Strategic metrics
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">🎯 Strategic Performance Indicators</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Program ROI analysis (completion rate vs employment rate)
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
        
        st.plotly_chart(fig, use_container_width=True, key="program_roi")
    
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
            line=dict(color='#2563eb', width=4),
            marker=dict(size=10, color='#1d4ed8')
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True, key="satisfaction_retention")
    
    # Predictive enrollment modeling
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">🔮 Predictive Enrollment Modeling</h3>', unsafe_allow_html=True)
    
    # Generate future projections
    future_years = [2025, 2026, 2027, 2028]
    current_trend = np.polyfit(enrollment_df['year'], enrollment_df['total_enrollment'], 1)
    projected_enrollment = [int(current_trend[0] * year + current_trend[1]) for year in future_years]
    
    # Combine historical and projected data
    all_years = list(enrollment_df['year']) + future_years
    all_enrollment = list(enrollment_df['total_enrollment']) + projected_enrollment
    
    projection_df = pd.DataFrame({
        'year': all_years,
        'enrollment': all_enrollment,
        'type': ['Historical'] * len(enrollment_df) + ['Projected'] * len(future_years)
    })
    
    fig = px.line(
        projection_df,
        x='year',
        y='enrollment',
        color='type',
        title='Enrollment Projection Through 2028',
        markers=True
    )
    
    fig.update_layout(
        title_x=0.5,
        height=400,
        xaxis_title='Academic Year',
        yaxis_title='Total Enrollment'
    )
    
    st.plotly_chart(fig, use_container_width=True, key="enrollment_projection")
    
    # Department competitiveness matrix
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">🏢 Department Competitiveness Matrix</h3>', unsafe_allow_html=True)
    
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
        
        st.plotly_chart(fig, use_container_width=True, key="competitiveness_matrix")
    
    with col2:
        # Top performing departments
        programs_df['overall_score'] = (
            programs_df['avg_gpa'] * 25 + 
            programs_df['completion_rate'] + 
            programs_df['employment_rate']
        ) / 3
        
        top_programs = programs_df.nlargest(3, 'overall_score')
        
        st.markdown("""
        <div class="insight-box" style="height: 400px;">
            <h4 style="color: #2563eb; margin-bottom: 1rem; font-weight: 600;">🏆 Top Performing Programs</h4>
        """, unsafe_allow_html=True)
        
        for i, (_, program) in enumerate(top_programs.iterrows(), 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉"
            st.markdown(f"""
            <div style="margin-bottom: 1rem; padding: 0.5rem; background: #f8fafc; border-radius: 8px;">
                <strong style="color: #1a202c;">{medal} {program['department']}</strong><br>
                <small style="color: #4b5563;">
                    GPA: {program['avg_gpa']:.2f} | Employment: {program['employment_rate']:.0f}% | 
                    Completion: {program['completion_rate']:.0f}%
                </small>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Strategic recommendations
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #2563eb; margin-bottom: 0.5rem; font-weight: 600;">💡 Strategic Intelligence Summary</h4>
        <p style="line-height: 1.5; color: #2d3748;">
            High-performing departments demonstrate optimal balance between academic rigor and career outcomes. 
            The predictive model suggests continued growth with strategic investment in faculty resources and 
            student support services. Programs in the upper-right quadrant of the performance matrix represent 
            institutional competitive advantages and growth opportunities.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Close content section container
    st.markdown('</div>', unsafe_allow_html=True)

def render_educational_insights():
    """Render strategic educational insights section"""
    
    with st.expander("📋 Educational Intelligence Executive Summary", expanded=False):
        st.markdown("# Education Intelligence Platform: Strategic Analysis")
        
        st.markdown("## Executive Summary")
        st.markdown("""
        This comprehensive educational analytics platform delivers actionable intelligence for institutional 
        leadership, focusing on student success optimization, program performance enhancement, and strategic 
        enrollment planning. The insights enable data-driven decision making for academic excellence and 
        institutional growth.
        
        **Key Strategic Value:**
        - Student success prediction and intervention strategies
        - Program performance optimization for competitive advantage
        - Predictive enrollment modeling for resource planning
        - Faculty allocation optimization for maximum impact
        """)
        
        st.markdown("## Strategic Intelligence Findings")
        st.markdown("""
        1. **Student Success Correlation**: High engagement levels strongly correlate with retention rates, 
           indicating opportunities for targeted intervention programs and student support optimization.
           
        2. **Program Performance Indicators**: Departments with optimal faculty-student ratios demonstrate 
           superior academic outcomes and employment placement rates, suggesting strategic investment opportunities.
           
        3. **Enrollment Growth Projections**: Predictive modeling indicates sustainable growth trajectory with 
           current trends supporting strategic capacity planning and infrastructure development.
           
        4. **Institutional Competitiveness**: Performance matrix analysis reveals market positioning strengths 
           and identifies programs with competitive advantages for strategic emphasis and resource allocation.
           
        5. **Resource Optimization Insights**: Faculty allocation analysis provides clear guidance for 
           strategic hiring and program investment to maximize student outcomes and institutional performance.
        """)
        
        st.markdown("## Strategic Recommendations")
        st.markdown("""
        **Priority Actions:**
        - Implement predictive early warning systems for at-risk student identification
        - Optimize faculty-student ratios in high-performing departments
        - Develop targeted engagement programs to improve retention rates
        - Invest in top-performing programs for competitive market positioning
        - Establish data-driven enrollment planning processes for sustainable growth
        """)