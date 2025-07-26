"""
Portfolio Overview component for the DataFlow Intelligence Platform
"""

import streamlit as st

def render_portfolio_overview():
    """Render the portfolio overview page"""
    
    # Hero Section
    st.title("DataFlow Intelligence Platform")
    
    st.subheader("Advanced Analytics Across Multiple Business Domains")

    # Project overview 
    st.subheader("Project Overview")
    st.write("""
    DataFlow Intelligence Platform is a comprehensive analytics solution demonstrating expertise in 
    multi-domain data analysis. This platform transforms complex business challenges into 
    actionable insights across transportation, education, and data visualization domains.
    """)
    
    st.write("""
    **Objective:** Advanced analytics through intuitive, business-focused solutions that enable 
    data-driven decision making across industries. This platform combines statistical rigor with 
    compelling data storytelling to deliver measurable business value.
    """)

    # Technical approach
    st.subheader("Technical Excellence")
    st.write("""
    Each module represents a real-world business challenge solved through 
    research, experimentation, and iterative development. The approach combines 
    theoretical knowledge with practical application to create solutions that deliver measurable business impact.
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("**Python**")
    with col2:
        st.write("**Streamlit**")
    with col3:
        st.write("**Plotly**")
    with col4:
        st.write("**Machine Learning**")

    # Performance metrics with enhanced styling
    st.subheader("Platform Performance Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    metrics_data = [
        ("40%", "Application Growth Analysis", "📈"),
        ("90%", "Retention Rate Optimization", "🎯"),
        ("15+", "Interactive Visualizations", "📊"),
        ("10K+", "Data Points Processed", "🔢")
    ]
    
    for i, (col, (value, description, icon)) in enumerate(zip([col1, col2, col3, col4], metrics_data)):
        with col:
            st.metric(description, value)

    # Platform modules with enhanced cards
    st.subheader("Intelligence Modules")
    
    # Transportation Intelligence Hub
    st.markdown("""
    <div class="portfolio-card fade-in-up">
        <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
            <div style="font-size: 3rem; margin-right: 1rem;">✈️</div>
            <h3 style="color: #1a202c; margin: 0; font-weight: 700;">Transportation Intelligence Hub</h3>
        </div>
        <p style="font-size: 1.05rem; line-height: 1.6; color: #2d3748; margin-bottom: 1.5rem;">
            <strong style="color: #1a202c;">Mission:</strong> Comprehensive route optimization and operational analytics solution for the aviation industry, 
            transforming complex flight data into strategic business insights.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem;">
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; border-left: 4px solid #2563eb; border: 1px solid #e2e8f0;">
                <strong style="color: #2563eb;">🎯 Key Features</strong>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: #2d3748;">Interactive route mapping analyzing 50+ destinations with real-time performance metrics</p>
            </div>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; border-left: 4px solid #059669; border: 1px solid #e2e8f0;">
                <strong style="color: #059669;">📈 Business Value</strong>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: #2d3748;">Operational efficiency dashboards enabling data-driven capacity planning</p>
            </div>
        </div>
        <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; border-left: 4px solid #eab308; border: 1px solid #fde047;">
            <strong style="color: #1a202c;">💼 Strategic Impact:</strong> <span style="color: #2d3748;">Market intelligence platform supporting route optimization and revenue maximization strategies</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Education Intelligence Platform
    st.markdown("""
    <div class="portfolio-card fade-in-up">
        <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
            <div style="font-size: 3rem; margin-right: 1rem;">🎓</div>
            <h3 style="color: #1a202c; margin: 0; font-weight: 700;">Education Intelligence Platform</h3>
        </div>
        <p style="font-size: 1.05rem; line-height: 1.6; color: #2d3748; margin-bottom: 1.5rem;">
            <strong>Mission:</strong> Comprehensive student lifecycle analytics platform that transforms institutional data 
            into strategic insights for educational performance optimization.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem;">
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; border-left: 4px solid #2563eb; border: 1px solid #e2e8f0;">
                <strong style="color: #2563eb;">📊 Analytics Engine</strong>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: #2d3748;">Multi-year enrollment trend analysis with 90% retention rate optimization insights</p>
            </div>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; border-left: 4px solid #059669; border: 1px solid #e2e8f0;">
                <strong style="color: #059669;">🎯 Success Monitoring</strong>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: #2d3748;">Student success monitoring with departmental performance analytics</p>
            </div>
        </div>
        <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; border-left: 4px solid #eab308; border: 1px solid #fde047;">
            <strong style="color: #1a202c;">💡 Innovation:</strong> <span style="color: #2d3748;">Predictive modeling framework for institutional strategic planning and growth forecasting</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Visualization Excellence Framework
    st.markdown("""
    <div class="portfolio-card fade-in-up">
        <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
            <div style="font-size: 3rem; margin-right: 1rem;">📊</div>
            <h3 style="color: #1a202c; margin: 0; font-weight: 700;">Visualization Excellence Framework</h3>
        </div>
        <p style="font-size: 1.05rem; line-height: 1.6; color: #2d3748; margin-bottom: 1.5rem;">
            <strong>Mission:</strong> Comprehensive framework demonstrating data storytelling best practices and effective 
            business communication through advanced visualization techniques.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem;">
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; border-left: 4px solid #2563eb; border: 1px solid #e2e8f0;">
                <strong style="color: #2563eb;">🎨 Design Principles</strong>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: #2d3748;">Comparative analysis showcasing effective vs. ineffective visualization design</p>
            </div>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; border-left: 4px solid #059669; border: 1px solid #e2e8f0;">
                <strong style="color: #059669;">📈 Statistical Analysis</strong>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: #2d3748;">Global happiness data with correlation modeling and regression analysis</p>
            </div>
        </div>
        <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; border-left: 4px solid #eab308; border: 1px solid #fde047;">
            <strong style="color: #1a202c;">🌍 Impact:</strong> <span style="color: #2d3748;">Reusable framework for effective data storytelling that enhances stakeholder engagement</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Personal branding section with modern design
    st.markdown("---")
    st.markdown("""
    <div class="personal-brand fade-in-up">
        <div style="font-size: 3rem; margin-bottom: 1rem;">👨‍💻</div>
        <h3 style="margin-bottom: 0.5rem; font-size: 1.5rem;">Ayush Chhoker</h3>
        <p style="font-size: 1.1rem; font-weight: 500; margin-bottom: 1rem; opacity: 0.9;"><strong>Data Analytics Professional</strong></p>
        <p style="font-size: 0.95rem; margin: 1rem 0; opacity: 0.8; line-height: 1.5;">
            Passionate about transforming raw data into strategic business insights through innovative analytics solutions.
            Specializing in end-to-end data science projects that drive measurable business impact.
        </p>
        <div style="margin-top: 2rem;">
            <a href="https://www.linkedin.com/in/apc15/" target="_blank" class="cta-button" style="font-size: 0.9rem; padding: 12px 24px; margin: 0 8px;">
                🔗 LinkedIn Profile
            </a>
            <a href="https://github.com/Apc0015" target="_blank" class="cta-button" style="font-size: 0.9rem; padding: 12px 24px; margin: 0 8px;">
                🐙 GitHub Portfolio
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Project resources with modern styling
    st.markdown("### 🔗 Project Resources")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0;" class="fade-in-up">
            <p style="font-size: 1.1rem; margin-bottom: 2rem; color: #2d3748;">
                Explore the live application and technical implementation
            </p>
            <div style="margin-top: 1.5rem;">
                <a href="https://dataflow-intelligence-platformgit-abnunhzst7htqqrrgffm2a.streamlit.app/" target="_blank" class="cta-button" style="margin: 0 8px; font-size: 0.9rem;">
                    🚀 Live Demo
                </a>
                <a href="https://github.com/Apc0015/DataFlow-Intelligence-Platform" target="_blank" class="cta-button" style="margin: 0 8px; font-size: 0.9rem;">
                    📂 Source Code
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)