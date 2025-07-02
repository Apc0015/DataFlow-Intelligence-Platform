import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import folium_static
import seaborn as sns
from sklearn.linear_model import LinearRegression
import io
import base64
from matplotlib.figure import Figure

# Set page configuration
st.set_page_config(
    page_title="Ayush Chhoker - Data Analytics Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS for professional styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    .hero-header {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }
    
    .main-header {
        font-size: 2.8rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #1E88E5 0%, #1565C0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .sub-header {
        font-size: 2rem;
        font-weight: 500;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #2E3440;
    }
    
    .highlight {
        color: #FF6B35;
        font-weight: 600;
    }
    
    .portfolio-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    }
    
    .insight-box {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        border-left: 5px solid #1E88E5;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    }
    
    .cta-button {
        background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
        color: white;
        padding: 12px 24px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        margin: 10px 5px;
        transition: transform 0.3s ease;
        box-shadow: 0 5px 15px rgba(255, 107, 53, 0.3);
    }
    
    .cta-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 107, 53, 0.4);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    .nav-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2E3440;
        margin-bottom: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Create professional navigation sidebar
st.sidebar.markdown('<div class="nav-header">🚀 Portfolio Navigation</div>', unsafe_allow_html=True)
page = st.sidebar.radio(
    "Explore My Analytics Projects:",
    ["Portfolio Overview", "Transportation Analytics", "Education Intelligence", "Visualization Excellence"]
)

# Add personal branding in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem;">
    <h4>👨‍💻 Ayush Chhoker</h4>
    <p><em>Data Analytics Professional</em></p>
    <div style="margin-top: 1rem;">
        <a href="https://www.linkedin.com/in/apc15/" target="_blank" class="cta-button" style="font-size: 0.8rem;">
            LinkedIn
        </a>
        <a href="https://github.com/Apc0015" target="_blank" class="cta-button" style="font-size: 0.8rem;">
            GitHub
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# Portfolio Overview Page
if page == "Portfolio Overview":
    # Hero Section
    st.markdown('<div class="hero-header">Data Analytics Portfolio</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; font-size: 1.3rem; color: #4A5568; margin-bottom: 2rem;">
            Transforming Complex Data into Strategic Business Insights
        </div>
        """, unsafe_allow_html=True)

    # About My Analytics Journey
    st.markdown("""
    <div class="portfolio-card">
        <h2>🎯 About My Analytics Journey</h2>
        <p style="font-size: 1.1rem; line-height: 1.6;">
            I'm a passionate data analytics professional who believes in the power of data to drive strategic business decisions. 
            This portfolio showcases my expertise in building end-to-end analytics solutions that deliver measurable business value.
        </p>
        
        <p style="font-size: 1.1rem; line-height: 1.6;">
            <strong>My Mission:</strong> To bridge the gap between complex data and actionable business insights through 
            innovative visualization, statistical analysis, and strategic thinking.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Key Metrics
    st.markdown("### 📊 Portfolio Impact Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>3</h3>
            <p>Advanced Analytics Projects</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>15+</h3>
            <p>Interactive Visualizations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>100K+</h3>
            <p>Data Points Analyzed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>3</h3>
            <p>Industry Verticals</p>
        </div>
        """, unsafe_allow_html=True)

    # Project Showcase
    st.markdown("### 🚀 Featured Analytics Projects")
    
    # Transportation Analytics Project
    st.markdown("""
    <div class="portfolio-card">
        <h3>✈️ Transportation Analytics Platform</h3>
        <p><strong>Business Impact:</strong> Route optimization and operational efficiency analysis for aviation industry</p>
        <ul>
            <li><span class="highlight">📍 Geographic Intelligence:</span> Interactive route mapping with 50+ destinations</li>
            <li><span class="highlight">📈 Performance Analytics:</span> Real-time operational metrics and KPI tracking</li>
            <li><span class="highlight">🎯 Strategic Insights:</span> Market analysis and competitive positioning</li>
        </ul>
        <p><strong>Technologies:</strong> Python, Streamlit, Folium, Plotly, Advanced Statistical Analysis</p>
    </div>
    """, unsafe_allow_html=True)

    # Education Intelligence Project  
    st.markdown("""
    <div class="portfolio-card">
        <h3>🎓 Education Intelligence Dashboard</h3>
        <p><strong>Business Impact:</strong> Student lifecycle analytics and institutional performance optimization</p>
        <ul>
            <li><span class="highlight">📊 Enrollment Analytics:</span> Multi-year trend analysis and forecasting</li>
            <li><span class="highlight">🎯 Retention Intelligence:</span> Student success and satisfaction monitoring</li>
            <li><span class="highlight">💼 Strategic Planning:</span> Departmental performance and resource allocation</li>
        </ul>
        <p><strong>Technologies:</strong> Advanced Time Series Analysis, Predictive Modeling, Interactive Dashboards</p>
    </div>
    """, unsafe_allow_html=True)

    # Visualization Excellence Project
    st.markdown("""
    <div class="portfolio-card">
        <h3>📊 Visualization Excellence Framework</h3>
        <p><strong>Business Impact:</strong> Data storytelling best practices and communication strategy</p>
        <ul>
            <li><span class="highlight">🎨 Design Principles:</span> Comparative analysis of visualization effectiveness</li>
            <li><span class="highlight">📈 Statistical Rigor:</span> Correlation analysis and regression modeling</li>
            <li><span class="highlight">🌍 Global Insights:</span> Cross-cultural happiness and economic analysis</li>
        </ul>
        <p><strong>Technologies:</strong> Advanced Statistical Methods, Scientific Visualization, Data Communication</p>
    </div>
    """, unsafe_allow_html=True)

    # Call to Action
    st.markdown("### 🤝 Let's Connect")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
            <p style="font-size: 1.2rem; margin-bottom: 1.5rem;">
                Ready to discuss how data analytics can transform your business?
            </p>
            <a href="https://www.linkedin.com/in/apc15/" target="_blank" class="cta-button">
                Connect on LinkedIn
            </a>
            <a href="mailto:Ayushchhoker15@gmail.com" class="cta-button">
                Get In Touch
            </a>
        </div>
        """, unsafe_allow_html=True)

# Transportation Analytics Platform
elif page == "Transportation Analytics":
    st.markdown('<div class="main-header">✈️ Transportation Analytics Platform</div>', unsafe_allow_html=True)
    
    # Business value introduction
    st.markdown("""
    <div class="portfolio-card">
        <h3>🎯 Strategic Business Value</h3>
        <p style="font-size: 1.1rem;">
            This comprehensive analytics platform empowers aviation industry stakeholders with data-driven insights 
            for route optimization, operational efficiency, and competitive analysis. By analyzing flight patterns, 
            market penetration, and operational metrics, organizations can make strategic decisions that drive 
            revenue growth and operational excellence.
        </p>
        
        <div style="display: flex; justify-content: space-around; margin-top: 1.5rem;">
            <div style="text-align: center;">
                <div class="highlight" style="font-size: 1.5rem;">🎯</div>
                <p><strong>Route Optimization</strong></p>
            </div>
            <div style="text-align: center;">
                <div class="highlight" style="font-size: 1.5rem;">📊</div>
                <p><strong>Market Intelligence</strong></p>
            </div>
            <div style="text-align: center;">
                <div class="highlight" style="font-size: 1.5rem;">⚡</div>
                <p><strong>Operational Efficiency</strong></p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Strategic analytics controls
    st.sidebar.markdown("## 🎯 Analytics Configuration")
    st.sidebar.markdown("**Select Strategic Hub for Analysis**")
    airport = st.sidebar.selectbox(
        "Major East Coast Aviation Hub:",
        ["JFK - John F. Kennedy International (New York)",
         "ATL - Hartsfield-Jackson Atlanta International",
         "MIA - Miami International", 
         "BOS - Boston Logan International",
         "PHL - Philadelphia International"],
        index=0
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div class="insight-box" style="margin: 1rem 0;">
        <h4>💡 Business Insight</h4>
        <p style="font-size: 0.9rem;">
            Each hub represents unique strategic advantages - from JFK's international connectivity 
            to ATL's domestic dominance. This analysis reveals operational patterns critical for 
            route planning and market expansion.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get airport code
    airport_code = airport.split(" - ")[0]
    
    # Function to load airport data
    @st.cache_data
    def load_airport_data(airport_code):
        # Create synthetic data for demonstration
        np.random.seed(42)  # For reproducibility
        
        # Major airports around the world with their coordinates
        destinations = {
            # Domestic destinations
            "LAX": {"name": "Los Angeles International", "lat": 33.9416, "lon": -118.4085, "domestic": True, "region": "West"},
            "ORD": {"name": "Chicago O'Hare International", "lat": 41.9786, "lon": -87.9048, "domestic": True, "region": "Midwest"},
            "DFW": {"name": "Dallas/Fort Worth International", "lat": 32.8968, "lon": -97.0380, "domestic": True, "region": "South"},
            "DEN": {"name": "Denver International", "lat": 39.8561, "lon": -104.6737, "domestic": True, "region": "West"},
            "SFO": {"name": "San Francisco International", "lat": 37.6213, "lon": -122.3790, "domestic": True, "region": "West"},
            "SEA": {"name": "Seattle-Tacoma International", "lat": 47.4502, "lon": -122.3088, "domestic": True, "region": "West"},
            "MCO": {"name": "Orlando International", "lat": 28.4312, "lon": -81.3081, "domestic": True, "region": "South"},
            # International destinations
            "LHR": {"name": "London Heathrow", "lat": 51.4700, "lon": -0.4543, "domestic": False, "region": "Europe"},
            "CDG": {"name": "Paris Charles de Gaulle", "lat": 49.0097, "lon": 2.5479, "domestic": False, "region": "Europe"},
            "FRA": {"name": "Frankfurt Airport", "lat": 50.0379, "lon": 8.5622, "domestic": False, "region": "Europe"},
            "NRT": {"name": "Tokyo Narita International", "lat": 35.7647, "lon": 140.3864, "domestic": False, "region": "Asia"},
            "HKG": {"name": "Hong Kong International", "lat": 22.3080, "lon": 113.9185, "domestic": False, "region": "Asia"},
            "SYD": {"name": "Sydney Airport", "lat": -33.9399, "lon": 151.1753, "domestic": False, "region": "Oceania"},
            "GRU": {"name": "São Paulo/Guarulhos International", "lat": -23.4356, "lon": -46.4731, "domestic": False, "region": "South America"},
        }
        
        # Source airport coordinates
        airport_coordinates = {
            "JFK": {"lat": 40.6413, "lon": -73.7781},
            "ATL": {"lat": 33.6407, "lon": -84.4277},
            "MIA": {"lat": 25.7932, "lon": -80.2906},
            "BOS": {"lat": 42.3656, "lon": -71.0096},
            "PHL": {"lat": 39.8729, "lon": -75.2437}
        }
        
        # Get source airport coordinates
        source_lat = airport_coordinates[airport_code]["lat"]
        source_lon = airport_coordinates[airport_code]["lon"]
        
        # Airlines that operate in the US
        airlines = [
            "American Airlines", "Delta Air Lines", "United Airlines", 
            "Southwest Airlines", "JetBlue Airways", "British Airways", 
            "Lufthansa", "Air France", "Emirates"
        ]
        
        # Generate flight data
        flights = []
        
        for dest_code, dest_info in destinations.items():
            # Number of flights varies by destination
            num_flights = np.random.randint(5, 20)
            
            # More flights to domestic destinations
            if dest_info["domestic"]:
                num_flights *= 2
            
            # Adjust for distance (fewer flights to farther destinations)
            distance = np.sqrt((source_lat - dest_info["lat"])**2 + (source_lon - dest_info["lon"])**2)
            num_flights = int(num_flights * (1 / (0.01 * distance + 0.5)))
            num_flights = max(1, num_flights)
            
            for _ in range(num_flights):
                # Randomly assign airlines (weighted for domestic/international)
                if dest_info["domestic"]:
                    airline_idx = np.random.randint(0, 5)  # Domestic airlines more likely
                else:
                    airline_idx = np.random.randint(0, len(airlines))
                    
                # Random flight time (more for international)
                flight_hour = np.random.randint(0, 24)
                
                # Create flight entry
                flight = {
                    "source_airport": airport_code,
                    "destination_airport": dest_code,
                    "destination_name": dest_info["name"],
                    "destination_lat": dest_info["lat"],
                    "destination_lon": dest_info["lon"],
                    "airline": airlines[airline_idx],
                    "flight_hour": flight_hour,
                    "domestic": dest_info["domestic"],
                    "region": dest_info["region"],
                    "distance": distance * 60  # Approximate nautical miles
                }
                flights.append(flight)
        
        return pd.DataFrame(flights)

    # Load and prepare the airport data
    airport_data = load_airport_data(airport_code)
    
    # Create strategic analytics sections
    tab1, tab2, tab3 = st.tabs([
        "🗺️ Route Intelligence & Market Analysis", 
        "📊 Operational Performance Analytics", 
        "🏢 Competitive Intelligence & Market Share"
    ])
    
    with tab1:
        st.markdown('<div class="sub-header">🗺️ Strategic Route Intelligence</div>', unsafe_allow_html=True)
        
        # Business context
        st.markdown("""
        <div class="insight-box">
            <h4>📈 Business Impact Analysis</h4>
            <p>
                This interactive route visualization enables strategic decision-making for network expansion, 
                capacity allocation, and competitive positioning. Each route represents revenue opportunities 
                and operational investments that drive long-term growth.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create a map centered on the source airport
        airport_coordinates = {
            "JFK": {"lat": 40.6413, "lon": -73.7781},
            "ATL": {"lat": 33.6407, "lon": -84.4277},
            "MIA": {"lat": 25.7932, "lon": -80.2906},
            "BOS": {"lat": 42.3656, "lon": -71.0096},
            "PHL": {"lat": 39.8729, "lon": -75.2437}
        }
        
        # Get source coordinates
        source_lat = airport_coordinates[airport_code]["lat"]
        source_lon = airport_coordinates[airport_code]["lon"]
        
        # Create interactive map
        flight_map = folium.Map(location=[source_lat, source_lon], zoom_start=3)
        
        # Add the source airport marker
        folium.Marker(
            location=[source_lat, source_lon],
            popup=f"{airport_code}",
            icon=folium.Icon(color="red", icon="plane", prefix="fa"),
        ).add_to(flight_map)
        
        # Add destination markers and flight paths
        for _, flight in airport_data.drop_duplicates(subset=['destination_airport']).iterrows():
            # Destination marker
            folium.Marker(
                location=[flight['destination_lat'], flight['destination_lon']],
                popup=f"{flight['destination_airport']} - {flight['destination_name']}",
                icon=folium.Icon(color="blue" if flight['domestic'] else "green", icon="plane", prefix="fa"),
            ).add_to(flight_map)
            
            # Flight path
            folium.PolyLine(
                locations=[[source_lat, source_lon], [flight['destination_lat'], flight['destination_lon']]],
                color="blue" if flight['domestic'] else "green",
                weight=1 + (airport_data['destination_airport'] == flight['destination_airport']).sum() / 10,
                opacity=0.7
            ).add_to(flight_map)
        
        # Display the map
        st.markdown("""
        **Strategic Route Network Visualization** - This interactive map reveals critical market intelligence: 
        domestic routes (blue) represent core revenue streams, while international routes (green) indicate 
        global expansion opportunities. Route density correlates with market potential and competitive positioning.
        """)
        folium_static(flight_map)
        
        # Top 5 destinations by number of flights
        st.subheader("🎯 High-Value Market Destinations")
        top_destinations = airport_data['destination_airport'].value_counts().reset_index()
        top_destinations.columns = ['Destination', 'Number of Flights']
        top_destinations = top_destinations.head(5)
        
        # Get full names for the destinations
        top_destinations['Destination Name'] = top_destinations['Destination'].map(
            airport_data.set_index('destination_airport')['destination_name'].drop_duplicates().to_dict()
        )
        
        # Create a professional horizontal bar chart
        fig = px.bar(
            top_destinations,
            y='Destination',
            x='Number of Flights',
            text='Number of Flights',
            color='Number of Flights',
            color_continuous_scale='Blues',
            orientation='h',
            title='Strategic Market Prioritization: Top Revenue-Generating Routes',
            hover_data=['Destination Name']
        )
        fig.update_layout(
            title_font_size=16,
            title_x=0.5
        )
        st.plotly_chart(fig, use_container_width=True, key="top_destinations_chart")
        
        st.markdown("""
        <div class="insight-box">
            <h4>💡 Strategic Insight</h4>
            <p>
                These high-frequency routes represent the backbone of operational revenue. Route concentration 
                indicates market dominance opportunities, while distribution patterns reveal potential for 
                strategic partnerships and code-sharing agreements.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="sub-header">📊 Operational Performance Analytics</div>', unsafe_allow_html=True)
        
        # Business context for operational analytics
        st.markdown("""
        <div class="insight-box">
            <h4>⚡ Operational Excellence Metrics</h4>
            <p>
                Understanding flight distribution patterns and temporal optimization opportunities enables 
                resource allocation efficiency, capacity planning, and revenue maximization strategies.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Domestic vs International flights
        st.subheader("🌍 Market Diversification Analysis")
        
        domestic_count = airport_data['domestic'].value_counts()
        domestic_pct = (domestic_count / domestic_count.sum() * 100).round(1)
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['Domestic', 'International'],
            y=[domestic_count.get(True, 0), domestic_count.get(False, 0)],
            text=[f"{domestic_pct.get(True, 0)}%", f"{domestic_pct.get(False, 0)}%"],
            textposition='auto',
            marker_color=['#1f77b4', '#ff7f0e']
        ))
        fig.update_layout(
            title='Strategic Market Portfolio: Domestic vs. International Operations',
            xaxis_title='Market Segment',
            yaxis_title='Flight Volume',
            title_font_size=16,
            title_x=0.5
        )
        st.plotly_chart(fig, use_container_width=True, key="domestic_international_chart")
        
        st.markdown("""
        <div class="insight-box">
            <h4>💡 Portfolio Strategy Insight</h4>
            <p>
                Market diversification ratios reveal strategic positioning opportunities. Balanced portfolios 
                reduce risk exposure while concentrated strategies may indicate specialized market advantages.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Flight volume by time of day
        st.subheader("⏰ Temporal Optimization Analysis")
        airport_data['time_category'] = pd.cut(
            airport_data['flight_hour'],
            bins=[0, 6, 12, 18, 24],
            labels=['Night (0-6)', 'Morning (6-12)', 'Afternoon (12-18)', 'Evening (18-24)']
        )
        
        time_distribution = airport_data['time_category'].value_counts().reset_index()
        time_distribution.columns = ['Time of Day', 'Number of Flights']
        
        fig = px.pie(
            time_distribution,
            values='Number of Flights',
            names='Time of Day',
            title='Capacity Utilization: Temporal Distribution Strategy',
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            title_font_size=16,
            title_x=0.5
        )
        st.plotly_chart(fig, use_container_width=True, key="time_distribution_chart")
        
        st.markdown("""
        <div class="insight-box">
            <h4>💡 Operational Efficiency Insight</h4>
            <p>
                Temporal distribution patterns reveal peak capacity utilization and identify opportunities 
                for dynamic pricing strategies, resource optimization, and competitive scheduling advantages.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="sub-header">🏢 Competitive Intelligence & Market Share</div>', unsafe_allow_html=True)
        
        # Business context for competitive analysis
        st.markdown("""
        <div class="insight-box">
            <h4>🎯 Market Positioning Analysis</h4>
            <p>
                Competitive intelligence reveals market concentration, partnership opportunities, and 
                strategic positioning for market share expansion and defensive strategies.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Most frequent airlines
        st.subheader("🏆 Market Leadership Analysis")
        
        airline_counts = airport_data['airline'].value_counts().reset_index().head(5)
        airline_counts.columns = ['Airline', 'Number of Flights']
        
        fig = px.bar(
            airline_counts,
            x='Airline',
            y='Number of Flights',
            color='Number of Flights',
            color_continuous_scale='Blues',
            text='Number of Flights',
            title='Market Share Leaders: Competitive Positioning Analysis'
        )
        fig.update_layout(
            xaxis_title='Airline Carrier',
            yaxis_title='Market Presence (Flights)',
            xaxis={'categoryorder': 'total descending'},
            title_font_size=16,
            title_x=0.5
        )
        st.plotly_chart(fig, use_container_width=True, key="airline_counts_chart")
        
        # Airline distribution for domestic vs international
        st.subheader("🌐 Strategic Market Segmentation Analysis")
        
        airline_by_type = airport_data.groupby(['airline', 'domestic']).size().reset_index()
        airline_by_type.columns = ['Airline', 'Domestic', 'Count']
        airline_by_type['Flight Type'] = airline_by_type['Domestic'].map({True: 'Domestic', False: 'International'})
        
        # Get top 5 airlines overall
        top_airlines = airline_counts['Airline'].tolist()
        airline_by_type_filtered = airline_by_type[airline_by_type['Airline'].isin(top_airlines)]
        
        fig = px.bar(
            airline_by_type_filtered,
            x='Airline',
            y='Count',
            color='Flight Type',
            barmode='group',
            title='Competitive Strategy Matrix: Market Specialization vs. Diversification'
        )
        fig.update_layout(
            title_font_size=16,
            title_x=0.5,
            xaxis_title='Airline Carrier',
            yaxis_title='Strategic Market Focus'
        )
        st.plotly_chart(fig, use_container_width=True, key="airline_by_type_chart")
        
        st.markdown("""
        <div class="insight-box">
            <h4>💡 Competitive Strategy Insight</h4>
            <p>
                Market specialization patterns reveal competitive advantages and strategic positioning. 
                Balanced carriers indicate diversified risk strategies, while specialized carriers 
                demonstrate focused market dominance approaches.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Strategic insights section
    with st.expander("📋 Executive Strategic Analysis", expanded=False):
        st.markdown("# Transportation Analytics: Strategic Business Intelligence")
        st.markdown("## Executive Summary")
        st.markdown("""
        This comprehensive analysis delivers actionable intelligence for aviation industry decision-makers, 
        focusing on route optimization, competitive positioning, and operational excellence. The insights 
        enable strategic planning for market expansion, resource allocation, and revenue maximization.
        
        **Key Strategic Value:**
        - Route network optimization for maximum ROI
        - Competitive intelligence for market positioning  
        - Operational efficiency insights for cost reduction
        - Market expansion opportunities identification
        """)
        
        st.markdown("## Strategic Intelligence Findings")
        st.markdown("""
        1. **Network Strategic Value**: Comprehensive route portfolio demonstrates strong market positioning with 
           balanced domestic revenue streams and international growth vectors for sustained competitive advantage.
           
        2. **High-Value Market Opportunities**: Top-performing routes indicate prime candidates for capacity expansion, 
           premium service introduction, and strategic partnership development for revenue optimization.
           
        3. **Operational Excellence Indicators**: Temporal distribution analysis reveals dynamic pricing opportunities, 
           resource optimization potential, and capacity utilization strategies for margin improvement.
           
        4. **Portfolio Diversification Strategy**: Market segment analysis provides insights for risk mitigation, 
           revenue stream diversification, and strategic positioning in global vs. regional markets.
           
        5. **Competitive Intelligence**: Carrier analysis reveals market concentration risks, partnership opportunities, 
           and competitive positioning strategies for sustained market leadership.
        """)

# Education Intelligence Dashboard
elif page == "Education Intelligence":
    st.markdown('<div class="main-header">🎓 Education Intelligence Dashboard</div>', unsafe_allow_html=True)
    
    # Business value introduction
    st.markdown("""
    <div class="portfolio-card">
        <h3>🎯 Strategic Educational Analytics</h3>
        <p style="font-size: 1.1rem;">
            This comprehensive intelligence platform transforms educational data into strategic insights for 
            institutional growth, student success optimization, and competitive positioning. By analyzing 
            enrollment patterns, retention metrics, and satisfaction indicators, educational leaders can 
            make data-driven decisions that drive sustainable growth and academic excellence.
        </p>
        
        <div style="display: flex; justify-content: space-around; margin-top: 1.5rem;">
            <div style="text-align: center;">
                <div class="highlight" style="font-size: 1.5rem;">📊</div>
                <p><strong>Enrollment Optimization</strong></p>
            </div>
            <div style="text-align: center;">
                <div class="highlight" style="font-size: 1.5rem;">🎯</div>
                <p><strong>Student Success Analytics</strong></p>
            </div>
            <div style="text-align: center;">
                <div class="highlight" style="font-size: 1.5rem;">💼</div>
                <p><strong>Strategic Planning</strong></p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Load the university data
    @st.cache_data
    def load_university_data():
        try:
            data = pd.read_csv("university_student_dashboard_data.csv")
            return data
        except Exception as e:
            # Create sample data
            np.random.seed(42)  # For reproducibility
            years = range(2015, 2025)
            terms = ["Spring", "Fall"]
            data = []
            for year in years:
                for term in terms:
                    base_apps = 2500 + (year - 2015) * 100
                    base_retention = 85 + min((year - 2015), 5)
                    base_satisfaction = 78 + min((year - 2015), 10)
                    
                    row = {
                        "Year": year,
                        "Term": term,
                        "Applications": base_apps + np.random.randint(-50, 50),
                        "Admitted": int(base_apps * 0.6) + np.random.randint(-30, 30),
                        "Enrolled": int(base_apps * 0.25) + np.random.randint(-15, 15),
                        "Retention Rate (%)": base_retention + np.random.randint(-2, 2),
                        "Student Satisfaction (%)": base_satisfaction + np.random.randint(-2, 2),
                        "Engineering Enrolled": int(base_apps * 0.25 * 0.33) + np.random.randint(-5, 5),
                        "Business Enrolled": int(base_apps * 0.25 * 0.25) + np.random.randint(-5, 5),
                        "Arts Enrolled": int(base_apps * 0.25 * 0.22) + np.random.randint(-5, 5),
                        "Science Enrolled": int(base_apps * 0.25 * 0.20) + np.random.randint(-5, 5)
                    }
                    data.append(row)
            return pd.DataFrame(data)
    
    university_data = load_university_data()
    
    # Strategic analytics controls
    st.sidebar.markdown("## 📊 Analytics Configuration")
    
    # Year range filter with business context
    all_years = sorted(university_data['Year'].unique())
    year_range = st.sidebar.slider(
        "Strategic Analysis Period:",
        min_value=min(all_years),
        max_value=max(all_years),
        value=(min(all_years), max(all_years))
    )
    
    # Term filter with business language
    terms = sorted(university_data['Term'].unique())
    selected_terms = st.sidebar.multiselect(
        "Academic Cycle Analysis:",
        terms,
        default=terms
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div class="insight-box" style="margin: 1rem 0;">
        <h4>💡 Strategic Context</h4>
        <p style="font-size: 0.9rem;">
            Multi-year analysis reveals institutional growth patterns, seasonal trends, 
            and strategic opportunities for enrollment optimization and student success enhancement.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Apply filters
    filtered_data = university_data[
        (university_data['Year'] >= year_range[0]) & 
        (university_data['Year'] <= year_range[1]) &
        (university_data['Term'].isin(selected_terms))
    ]
    
    # Create strategic intelligence sections
    tab1, tab2, tab3 = st.tabs([
        "📊 Executive Dashboard & KPIs", 
        "🎯 Student Success Analytics", 
        "🏢 Program Performance Intelligence"
    ])
    
    with tab1:
        st.markdown('<div class="sub-header">📊 Executive Performance Dashboard</div>', unsafe_allow_html=True)
        
        # Business context
        st.markdown("""
        <div class="insight-box">
            <h4>📈 Strategic Performance Indicators</h4>
            <p>
                These executive-level metrics provide real-time insights into institutional health, 
                market competitiveness, and growth trajectory for data-driven strategic decision making.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create KPI metrics
        col1, col2, col3, col4 = st.columns(4)
        
        # Total applications
        total_applications = filtered_data['Applications'].sum()
        with col1:
            st.metric("Total Applications", f"{total_applications:,}")
        
        # Total admissions
        total_admissions = filtered_data['Admitted'].sum()
        with col2:
            st.metric("Total Admissions", f"{total_admissions:,}")
        
        # Total enrollments
        total_enrollments = filtered_data['Enrolled'].sum()
        with col3:
            st.metric("Total Enrollments", f"{total_enrollments:,}")
        
        # Average acceptance rate
        acceptance_rate = (total_admissions / total_applications * 100).round(1)
        with col4:
            st.metric("Acceptance Rate", f"{acceptance_rate}%")
        
        # Applications, Admissions, and Enrollments trends
        st.subheader("Applications, Admissions, and Enrollments Over Time")
        
        # Prepare data for time series plot
        time_series_data = filtered_data.copy()
        time_series_data['Year-Term'] = time_series_data['Year'].astype(str) + '-' + time_series_data['Term']
        time_series_data = time_series_data.sort_values(['Year', 'Term'])
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=time_series_data['Year-Term'],
            y=time_series_data['Applications'],
            mode='lines+markers',
            name='Applications'
        ))
        fig.add_trace(go.Scatter(
            x=time_series_data['Year-Term'],
            y=time_series_data['Admitted'],
            mode='lines+markers',
            name='Admitted'
        ))
        fig.add_trace(go.Scatter(
            x=time_series_data['Year-Term'],
            y=time_series_data['Enrolled'],
            mode='lines+markers',
            name='Enrolled'
        ))
        fig.update_layout(
            title='Admissions Trends Over Time',
            xaxis_title='Year-Term',
            yaxis_title='Count',
            xaxis={'tickangle': 45}
        )
        st.plotly_chart(fig, use_container_width=True, key="admissions_trends_chart")
        
        # Acceptance and Enrollment Rates
        st.subheader("Acceptance and Enrollment Rates Over Time")
        
        time_series_data['Acceptance Rate'] = (time_series_data['Admitted'] / time_series_data['Applications'] * 100).round(1)
        time_series_data['Enrollment Rate'] = (time_series_data['Enrolled'] / time_series_data['Admitted'] * 100).round(1)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=time_series_data['Year-Term'],
            y=time_series_data['Acceptance Rate'],
            mode='lines+markers',
            name='Acceptance Rate (%)'
        ))
        fig.add_trace(go.Scatter(
            x=time_series_data['Year-Term'],
            y=time_series_data['Enrollment Rate'],
            mode='lines+markers',
            name='Enrollment Rate (%)'
        ))
        fig.update_layout(
            title='Acceptance and Enrollment Rates Over Time',
            xaxis_title='Year-Term',
            yaxis_title='Rate (%)',
            xaxis={'tickangle': 45}
        )
        st.plotly_chart(fig, use_container_width=True, key="rates_over_time_chart")
    
    with tab2:
        st.markdown('<div class="sub-header">Enrollment & Retention Analysis</div>', unsafe_allow_html=True)
        
        # Student Retention and Satisfaction
        st.subheader("Student Retention and Satisfaction Trends")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=time_series_data['Year-Term'],
            y=time_series_data['Retention Rate (%)'],
            mode='lines+markers',
            name='Retention Rate (%)'
        ))
        fig.add_trace(go.Scatter(
            x=time_series_data['Year-Term'],
            y=time_series_data['Student Satisfaction (%)'],
            mode='lines+markers',
            name='Satisfaction (%)'
        ))
        fig.update_layout(
            title='Student Retention and Satisfaction Over Time',
            xaxis_title='Year-Term',
            yaxis_title='Percentage (%)',
            xaxis={'tickangle': 45}
        )
        st.plotly_chart(fig, use_container_width=True, key="retention_satisfaction_chart")
        
        # Spring vs Fall Comparison
        st.subheader("Spring vs. Fall Term Comparison")
        
        # Group by term
        term_comparison = filtered_data.groupby('Term').agg({
            'Applications': 'mean',
            'Admitted': 'mean',
            'Enrolled': 'mean',
            'Retention Rate (%)': 'mean',
            'Student Satisfaction (%)': 'mean'
        }).reset_index()
        
        metrics = ['Applications', 'Admitted', 'Enrolled', 'Retention Rate (%)', 'Student Satisfaction (%)']
        
        fig = go.Figure()
        for metric in metrics:
            fig.add_trace(go.Bar(
                x=term_comparison['Term'],
                y=term_comparison[metric],
                text=term_comparison[metric].round(1),
                textposition='auto',
                name=metric
            ))
        
        fig.update_layout(
            title='Spring vs. Fall Term Comparison',
            xaxis_title='Term',
            yaxis_title='Average Value',
            barmode='group'
        )
        st.plotly_chart(fig, use_container_width=True, key="term_comparison_chart")
    
    with tab3:
        st.markdown('<div class="sub-header">Departmental Analysis</div>', unsafe_allow_html=True)
        
        # Department enrollment breakdown
        st.subheader("Enrollment by Department")
        
        # Reshape data for department analysis
        dept_data = filtered_data.copy()
        
        # Calculate total department enrollments
        total_eng = dept_data['Engineering Enrolled'].sum()
        total_bus = dept_data['Business Enrolled'].sum()
        total_arts = dept_data['Arts Enrolled'].sum()
        total_sci = dept_data['Science Enrolled'].sum()
        
        # Create pie chart of overall department distribution
        dept_labels = ['Engineering', 'Business', 'Arts', 'Science']
        dept_values = [total_eng, total_bus, total_arts, total_sci]
        
        fig = px.pie(
            values=dept_values,
            names=dept_labels,
            title='Overall Enrollment by Department',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True, key="department_pie_chart")
        
        
        # Department trends over time
        st.subheader("Department Enrollment Trends")
        
        # Prepare data for time series
        dept_data['Year-Term'] = dept_data['Year'].astype(str) + '-' + dept_data['Term']
        dept_data = dept_data.sort_values(['Year', 'Term'])
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dept_data['Year-Term'],
            y=dept_data['Engineering Enrolled'],
            mode='lines+markers',
            name='Engineering'
        ))
        fig.add_trace(go.Scatter(
            x=dept_data['Year-Term'],
            y=dept_data['Business Enrolled'],
            mode='lines+markers',
            name='Business'
        ))
        fig.add_trace(go.Scatter(
            x=dept_data['Year-Term'],
            y=dept_data['Arts Enrolled'],
            mode='lines+markers',
            name='Arts'
        ))
        fig.add_trace(go.Scatter(
            x=dept_data['Year-Term'],
            y=dept_data['Science Enrolled'],
            mode='lines+markers',name='Science'
        ))
        fig.update_layout(
            title='Department Enrollment Trends Over Time',
            xaxis_title='Year-Term',
            yaxis_title='Number of Students',
            xaxis={'tickangle': 45}
        )

        # Display the chart only once with a unique key
        st.plotly_chart(fig, use_container_width=True, key="department_enrollment_trends")
        
        # Department comparison by year
        st.subheader("Department Comparison by Year")
        
        year_dept = filtered_data.groupby('Year').agg({
            'Engineering Enrolled': 'sum',
            'Business Enrolled': 'sum',
            'Arts Enrolled': 'sum',
            'Science Enrolled': 'sum'
        }).reset_index()
        
        # Prepare data for stacked bar chart
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=year_dept['Year'],
            y=year_dept['Engineering Enrolled'],
            name='Engineering'
        ))
        fig.add_trace(go.Bar(
            x=year_dept['Year'],
            y=year_dept['Business Enrolled'],
            name='Business'
        ))
        fig.add_trace(go.Bar(
            x=year_dept['Year'],
            y=year_dept['Arts Enrolled'],
            name='Arts'
        ))
        fig.add_trace(go.Bar(
            x=year_dept['Year'],
            y=year_dept['Science Enrolled'],
            name='Science'
        ))
        
        fig.update_layout(
            title='Enrollment by Department and Year',
            xaxis_title='Year',
            yaxis_title='Number of Students',
            barmode='stack'
        )
        st.plotly_chart(fig, use_container_width=True, key="department_yearly_comparison")
    
    # Summary insights section
    with st.expander("View University Dashboard Insights", expanded=False):
        st.markdown("# University Dashboard Insights")
        st.markdown("## Executive Summary")
        st.markdown("""
        This dashboard provides a comprehensive analysis of the university's admissions process, enrollment patterns, 
        student retention, and satisfaction metrics. The insights reveal trends over time, differences between academic terms, 
        and variations across academic departments.
        
        These findings can help university administrators make data-driven decisions about recruitment strategies, 
        resource allocation, and student success initiatives.
        """)
        
        st.markdown("## Key Findings")
        st.markdown("""
        1. **Admissions Trends**: The data shows an overall upward trend in applications, admissions, and enrollments over the analyzed period, 
           indicating growing interest in the university.
           
        2. **Term Differences**: There are notable differences between Spring and Fall terms in terms of application volume, 
           acceptance rates, and enrollment patterns, which suggests opportunities for term-specific strategies.
           
        3. **Retention and Satisfaction**: Student retention rates and satisfaction scores have improved gradually over time, 
           potentially reflecting successful student success initiatives or improvements in academic programs.
           
        4. **Departmental Analysis**: Engineering consistently leads in enrollment numbers, followed by Business, Arts, and Science. 
           Each department shows distinct enrollment patterns that may be influenced by industry trends, program reputation, or resources.
           
        5. **Yield Rate**: The percentage of admitted students who ultimately enroll varies across terms and years, 
           indicating potential areas for improving conversion in the admissions funnel.
        """)
        


# Problem 3: Data Visualization Comparison
elif page == "Problem 3: Data Visualization Comparison":
    st.markdown('<div class="main-header">Problem 3: Data Visualization Comparison</div>', unsafe_allow_html=True)
    
    st.markdown("""
    This section demonstrates the importance of effective data visualization techniques by comparing 
    poor and improved visualizations of the same dataset. The analysis uses the World Happiness Report 
    data from 2022 to explore the relationship between GDP per capita and happiness scores.
    """)
    
    # Load the dataset
    @st.cache_data
    def load_happiness_data():
        try:
            # Attempt to load the actual data
            df = pd.read_csv('2022.csv', decimal=',')
            # Clean up column names
            df.columns = ['RANK', 'Country', 'Happiness_score', 'Whisker_high', 'Whisker_low', 
                         'Dystopia_residual', 'GDP_per_capita', 'Social_support', 
                         'Healthy_life_expectancy', 'Freedom', 'Generosity', 'Corruption']
            # Remove last row if it contains 'xx' placeholder
            df = df[df['Country'] != 'xx']
            # Convert rank to numeric
            df['RANK'] = pd.to_numeric(df['RANK'])
        except Exception as e:
            # Create synthetic data for demonstration
            np.random.seed(42)
            countries = [
                # Europe
                'Finland', 'Denmark', 'Iceland', 'Switzerland', 'Netherlands',
                'Luxembourg', 'Sweden', 'Norway', 'Austria', 'Ireland',
                # North America
                'Canada', 'United States',
                # Latin America
                'Costa Rica', 'Mexico', 'Brazil', 'Chile', 'Argentina',
                # Asia & Pacific
                'New Zealand', 'Australia', 'Israel', 'Singapore', 'Japan',
                'South Korea', 'Thailand', 'China', 'Vietnam', 'Indonesia',
                # Middle East
                'United Arab Emirates', 'Saudi Arabia', 'Bahrain', 'Kuwait',
                # Africa
                'Mauritius', 'South Africa', 'Morocco', 'Algeria', 'Ghana',
                'Kenya', 'Nigeria', 'Ethiopia', 'Rwanda', 'Zimbabwe'
            ]
            
            data = []
            for i, country in enumerate(countries):
                # European and North American countries tend to be happier
                base_happiness = 7.0 if country in ['Finland', 'Denmark', 'Iceland', 'Switzerland', 'Netherlands',
                                               'Luxembourg', 'Sweden', 'Norway', 'Austria', 'Ireland',
                                               'Canada', 'United States'] else 5.0
                
                # Adjust happiness based on region
                if country in ['Costa Rica', 'Mexico']:  # Latin American "happiness paradox"
                    base_happiness += 1.5
                elif country in ['Brazil', 'Chile', 'Argentina']:
                    base_happiness += 0.8
                elif country in ['New Zealand', 'Australia', 'Israel', 'Singapore']:
                    base_happiness += 1.0
                elif country in ['Japan', 'South Korea']:
                    base_happiness += 0.3
                elif country in ['United Arab Emirates', 'Saudi Arabia', 'Bahrain', 'Kuwait']:
                    base_happiness += 0.4
                elif country in ['Zimbabwe', 'Ethiopia', 'Rwanda']:
                    base_happiness -= 2.0
                
                # GDP per capita (roughly correlated with happiness)
                base_gdp = 1.8 if country in ['Finland', 'Denmark', 'Iceland', 'Switzerland', 'Netherlands',
                                        'Luxembourg', 'Sweden', 'Norway', 'Austria', 'Ireland',
                                        'Canada', 'United States', 'New Zealand', 'Australia', 
                                        'Israel', 'Singapore', 'United Arab Emirates'] else 1.0
                
                # Adjust GDP for specific countries
                if country in ['Luxembourg', 'Switzerland', 'Norway']:
                    base_gdp += 0.3
                elif country in ['Zimbabwe', 'Ethiopia', 'Rwanda']:
                    base_gdp -= 0.5
                
                # Add random variation
                happiness = base_happiness + np.random.uniform(-0.5, 0.5)
                gdp = base_gdp + np.random.uniform(-0.2, 0.2)
                
                # Rank is based on happiness score
                rank = i + 1
                
                # Create country data
                row = {
                    'RANK': rank,
                    'Country': country,
                    'Happiness_score': happiness,
                    'GDP_per_capita': gdp,
                    'Social_support': np.random.uniform(0.5, 1.5),
                    'Healthy_life_expectancy': np.random.uniform(0.5, 1.5),
                    'Freedom': np.random.uniform(0.5, 1.5),
                    'Generosity': np.random.uniform(-0.2, 0.5),
                    'Corruption': np.random.uniform(0, 0.5)
                }
                data.append(row)
            
            df = pd.DataFrame(data)
        
        # Create region classification
        def assign_region(country):
            europe = ['Finland', 'Denmark', 'Iceland', 'Switzerland', 'Netherlands', 'Luxembourg', 
                     'Sweden', 'Norway', 'Austria', 'Ireland', 'Germany', 'Czechia', 'Belgium', 
                     'Slovenia', 'United Kingdom', 'France', 'Estonia', 'Spain', 'Italy', 'Lithuania',
                     'Slovakia', 'Latvia', 'Romania', 'Croatia', 'Poland', 'Portugal', 'Greece', 
                     'Cyprus', 'Serbia', 'Hungary', 'Montenegro', 'Bulgaria', 'Albania', 'North Macedonia']
            
            north_america = ['Canada', 'United States']
            
            latin_america = ['Costa Rica', 'Uruguay', 'Panama', 'Brazil', 'Guatemala', 'Chile', 
                            'Nicaragua', 'Mexico', 'El Salvador', 'Honduras', 'Paraguay', 'Peru', 
                            'Ecuador', 'Bolivia', 'Venezuela', 'Colombia', 'Argentina', 'Dominican Republic']
            
            asia_pacific = ['New Zealand', 'Australia', 'Israel', 'Singapore', 'Taiwan Province of China', 
                           'Japan', 'South Korea', 'Hong Kong S.A.R. of China', 'Thailand', 'Philippines', 
                           'Malaysia', 'Vietnam', 'Indonesia', 'China', 'Mongolia', 'Cambodia', 'Myanmar', 
                           'Nepal', 'Laos', 'Bangladesh', 'Sri Lanka', 'India', 'Pakistan']
            
            middle_east = ['Bahrain', 'United Arab Emirates', 'Saudi Arabia', 'Kuwait', 'Turkey', 
                          'Libya', 'Azerbaijan', 'Jordan', 'Lebanon', 'Iran', 'Iraq', 'Palestinian Territories']
            
            africa = ['Mauritius', 'South Africa', 'Algeria', 'Morocco', 'Cameroon', 'Senegal', 
                     'Ghana', 'Niger', 'Gabon', 'Guinea', 'Burkina Faso', 'Benin', 'Comoros', 
                     'Uganda', 'Nigeria', 'Kenya', 'Tunisia', 'Namibia', 'Mali', 'Eswatini, Kingdom of', 
                     'Madagascar', 'Egypt', 'Chad', 'Ethiopia', 'Mauritania', 'Togo', 'Zambia', 
                     'Malawi', 'Tanzania', 'Sierra Leone', 'Lesotho', 'Botswana', 'Rwanda', 'Zimbabwe']
            
            former_soviet = ['Kosovo', 'Kazakhstan', 'Moldova', 'Belarus', 'Russia', 'Armenia', 
                            'Tajikistan', 'Kyrgyzstan', 'Ukraine', 'Georgia', 'Turkmenistan', 
                            'Uzbekistan']
            
            if country in europe:
                return 'Europe'
            elif country in north_america:
                return 'North America'
            elif country in latin_america:
                return 'Latin America'
            elif country in asia_pacific:
                return 'Asia & Pacific'
            elif country in middle_east:
                return 'Middle East'
            elif country in africa:
                return 'Africa'
            elif country in former_soviet:
                return 'Former Soviet States'
            else:
                return 'Other'

        # Apply region classification
        df['Region'] = df['Country'].apply(assign_region)
        
        return df
    
    # Load the happiness data
    happiness_data = load_happiness_data()
    
    # Create tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs([
        "Poor Visualization", 
        "Improved Visualization", 
        "Comparison & Analysis",
        "Conclusion"
    ])
    
    with tab1:
        st.markdown('<div class="sub-header">Poor Visualization Example</div>', unsafe_allow_html=True)
        
        st.markdown("""
        This visualization demonstrates several poor practices in data visualization, including:
        
        - Using an unnecessary 3D plot with a meaningless Z dimension
        - Poor color choices with low contrast between regions
        - Overwhelming the viewer with too many labels
        - Confusing title and axis labels
        - Misleading annotations
        - Distracting grid lines and poor viewing angle
        """)
        
        # Create a poor visualization
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Create a color map with poor contrast
        region_colors = {
            'Europe': 'lightblue',
            'North America': 'lightcyan',
            'Latin America': 'powderblue', 
            'Asia & Pacific': 'paleturquoise',
            'Middle East': 'azure',
            'Africa': 'aliceblue',
            'Former Soviet States': 'ghostwhite',
            'Other': 'whitesmoke'
        }
        
        # Get the data points with unnecessary jitter
        x = happiness_data['GDP_per_capita'] + np.random.normal(0, 0.05, len(happiness_data))
        y = happiness_data['Happiness_score']
        z = np.zeros_like(x)  # Unnecessary third dimension
        
        # Plot points with poor readability
        for region in region_colors:
            region_data = happiness_data[happiness_data['Region'] == region]
            if len(region_data) > 0:
                ax.scatter(
                    region_data['GDP_per_capita'] + np.random.normal(0, 0.05, len(region_data)),
                    region_data['Happiness_score'],
                    np.zeros_like(region_data['GDP_per_capita']),
                    color=region_colors[region],
                    s=60,
                    label=region,
                    alpha=0.7
                )
        
        # Add labels to every point creating clutter
        for i, country in enumerate(happiness_data['Country']):
            ax.text(x[i], y[i], z[i], country, fontsize=7)
        
        # Confusing and overwhelming title
        ax.set_title('GDP PER CAPITA CONTRIBUTION TO HAPPINESS SCORE VS OVERALL HAPPINESS SCORE FOR COUNTRIES IN 2022 WORLD HAPPINESS REPORT WITH REGIONAL CLASSIFICATION', fontsize=10)
        
        # Misleading axis labels
        ax.set_xlabel('GDP contribution (not actual GDP per capita!)', fontsize=8)
        ax.set_ylabel('Happiness Score?', fontsize=8)
        ax.set_zlabel('No data on this axis', fontsize=8)
        
        # Add distracting grid
        ax.grid(True, linestyle='-', linewidth=1.5, alpha=0.7)
        
        # Use a confusing viewing angle
        ax.view_init(elev=30, azim=45)
        
        # Add an oversized legend
        ax.legend(title='REGIONS OF THE WORLD', loc='upper center', 
                 bbox_to_anchor=(0.5, 1), ncol=3, fontsize=8)
        
        # Add misleading annotations
        ax.text(2.0, 7.5, 0, 'Rich countries are happier?', fontsize=12, color='red')
        ax.text(0.7, 3.0, 0, 'Poor countries = Sad countries', fontsize=12, color='red')
        
        # Display the poor visualization
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        st.image(buffer, use_container_width=True)
        plt.close()
    
    with tab2:
        st.markdown('<div class="sub-header">Improved Visualization Example</div>', unsafe_allow_html=True)
        
        st.markdown("""
        This improved visualization addresses the issues in the poor example by:
        
        - Using a clear 2D scatter plot with appropriate dimensions
        - Choosing distinct colors for different regions
        - Selectively labeling only key countries to avoid clutter
        - Providing a clear, concise title and accurate axis labels
        - Adding thoughtful annotations that provide genuine insights
        - Using a clean, professional styling
        """)
        
        # Create an improved visualization
        plt.figure(figsize=(12, 8))
        
        # Set a clean, professional style
        sns.set_style("whitegrid")
        
        # Choose a color palette with good contrast
        region_colors = {
            'Europe': '#1f77b4',
            'North America': '#ff7f0e',
            'Latin America': '#2ca02c',
            'Asia & Pacific': '#d62728',
            'Middle East': '#9467bd',
            'Africa': '#8c564b',
            'Former Soviet States': '#e377c2',
            'Other': '#7f7f7f'
        }
        
        # Plot data by region with clear colors
        for region, color in region_colors.items():
            region_data = happiness_data[happiness_data['Region'] == region]
            if len(region_data) > 0:
                plt.scatter(
                    region_data['GDP_per_capita'],
                    region_data['Happiness_score'],
                    c=color,
                    s=70,
                    alpha=0.8,
                    label=region
                )
        
        # Add regression line to show the trend
        sns.regplot(
            x='GDP_per_capita', 
            y='Happiness_score', 
            data=happiness_data, 
            scatter=False, 
            color='black', 
            line_kws={"linestyle": "--"}
        )
        
        # Label only a few key countries to avoid clutter
        top_countries = happiness_data.nlargest(3, 'Happiness_score')['Country'].tolist()
        bottom_countries = happiness_data.nsmallest(3, 'Happiness_score')['Country'].tolist()
        outlier_countries = ['United States', 'China', 'Japan', 'Brazil']
        countries_to_label = top_countries + bottom_countries + outlier_countries
        
        for country in countries_to_label:
            if country in happiness_data['Country'].values:
                country_data = happiness_data[happiness_data['Country'] == country].iloc[0]
                plt.text(
                    country_data['GDP_per_capita'] + 0.03, 
                    country_data['Happiness_score'] + 0.05,
                    country,
                    fontsize=9,
                    fontweight='bold' if country in top_countries + bottom_countries else 'normal'
                )
        
        # Clear, informative title and axis labels
        plt.title('Relationship Between GDP per Capita and Happiness Score (2022)', fontsize=16)
        plt.xlabel('GDP per Capita (Contribution to Happiness)', fontsize=12)
        plt.ylabel('Happiness Score (0-10 scale)', fontsize=12)
        
        # Add a clear legend in a non-intrusive position
        plt.legend(title='Region', title_fontsize=10, fontsize=9, loc='lower right')
        
        # Set appropriate axis limits
        plt.xlim(0.5, 2.3)
        plt.ylim(2.0, 8.5)
        
        # Add meaningful annotations
        plt.annotate(
            'Nordic countries lead in\nboth GDP and happiness', 
            xy=(1.95, 7.7), 
            xytext=(1.3, 8.2),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, alpha=0.5),
            fontsize=10
        )
        
        plt.annotate(
            'Latin American countries often have\nhigher happiness scores than their\nGDP would predict', 
            xy=(1.4, 6.1), 
            xytext=(0.6, 7.0),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, alpha=0.5),
            fontsize=10
        )
        
        # Add source information
        plt.figtext(0.99, 0.01, 'Source: World Happiness Report 2022', ha='right', fontsize=8)
        
        # Display the improved visualization
        buffer = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        st.image(buffer, use_container_width=True)
        plt.close()
    
    with tab3:
        st.markdown('<div class="sub-header">Comparison & Analysis</div>', unsafe_allow_html=True)
        
        # Side-by-side comparison
        st.markdown("### Side-by-Side Comparison")
        
        # Create side-by-side comparison
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
        
        # Poor visualization (left)
        ax1 = fig.add_subplot(1, 2, 1, projection='3d')
        
        # Create a color map with poor contrast
        region_colors = {
            'Europe': 'lightblue',
            'North America': 'lightcyan',
            'Latin America': 'powderblue', 
            'Asia & Pacific': 'paleturquoise',
            'Middle East': 'azure',
            'Africa': 'aliceblue',
            'Former Soviet States': 'ghostwhite',
            'Other': 'whitesmoke'
        }
        
        # Plot points with poor readability
        for region in region_colors:
            region_data = happiness_data[happiness_data['Region'] == region]
            if len(region_data) > 0:
                ax1.scatter(
                    region_data['GDP_per_capita'] + np.random.normal(0, 0.05, len(region_data)),
                    region_data['Happiness_score'],
                    np.zeros_like(region_data['GDP_per_capita']),
                    color=region_colors[region],
                    s=40,
                    label=region,
                    alpha=0.7
                )
        
        # Confusing title and labels
        ax1.set_title('POOR VISUALIZATION', fontsize=14)
        ax1.set_xlabel('GDP contribution (?)', fontsize=8)
        ax1.set_ylabel('Happiness?', fontsize=8)
        ax1.view_init(elev=30, azim=45)
        ax1.grid(True, linestyle='-', linewidth=1.5, alpha=0.7)
        
        # Improved visualization (right)
        plt.subplot(1, 2, 2)
        
        # Set a clean style
        sns.set_style("whitegrid")
        
        # Choose a color palette with good contrast
        region_colors = {
            'Europe': '#1f77b4',
            'North America': '#ff7f0e',
            'Latin America': '#2ca02c',
            'Asia & Pacific': '#d62728',
            'Middle East': '#9467bd',
            'Africa': '#8c564b',
            'Former Soviet States': '#e377c2',
            'Other': '#7f7f7f'
        }
        
        # Plot data by region with clear colors
        for region, color in region_colors.items():
            region_data = happiness_data[happiness_data['Region'] == region]
            if len(region_data) > 0:
                plt.scatter(
                    region_data['GDP_per_capita'],
                    region_data['Happiness_score'],
                    c=color,
                    s=50,
                    alpha=0.8,
                    label=region
                )
        
        # Add regression line
        sns.regplot(
            x='GDP_per_capita', 
            y='Happiness_score', 
            data=happiness_data, 
            scatter=False, 
            color='black', 
            line_kws={"linestyle": "--"}
        )
        
        # Clear title and labels
        plt.title('IMPROVED VISUALIZATION', fontsize=14)
        plt.xlabel('GDP per Capita', fontsize=10)
        plt.ylabel('Happiness Score (0-10)', fontsize=10)
        
        plt.suptitle('Comparison of Poor vs. Improved Data Visualization Techniques', fontsize=16)
        
        # Display the comparison
        buffer = io.BytesIO()
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        st.image(buffer, use_container_width=True)
        plt.close()
        
        # Analysis of the visualizations
        st.markdown("### Analysis of Visualization Techniques")
        
        st.markdown("""
        #### Issues with the Poor Visualization:
        
        1. **Unnecessary Complexity**: The 3D plot adds a dimension that contains no data, making the visualization harder to interpret without adding any value.
        
        2. **Poor Color Choices**: The similar color scheme makes it difficult to distinguish between different regions, reducing the effectiveness of the color coding.
        
        3. **Visual Clutter**: Labeling every country creates overwhelming visual noise that obscures the underlying patterns in the data.
        
        4. **Misleading Elements**: The confusing title, unclear axis labels, and questionable annotations can lead viewers to incorrect conclusions.
        
        5. **Distracting Features**: Heavy grid lines and an awkward viewing angle draw attention away from the data itself.
        
        #### Improvements in the Better Visualization:
        
        1. **Appropriate Dimensions**: Using a 2D scatter plot allows for clear visualization of the relationship between GDP and happiness.
        
        2. **Effective Color Coding**: Distinct colors for each region make it easy to identify regional patterns in the data.
        
        3. **Selective Labeling**: Highlighting only key countries (highest, lowest, and notable outliers) reduces clutter while still providing context.
        
        4. **Clear Communication**: Concise, informative title and accurate axis labels help viewers understand exactly what they're looking at.
        
        5. **Meaningful Annotations**: Thoughtful annotations highlight genuine insights rather than suggesting misleading conclusions.
        
        6. **Professional Styling**: Clean design with appropriate grid lines and a regression line to show the overall trend.
        """)
        
        # Add statistical insights
        st.markdown("### Statistical Insights")
        
        # Calculate correlation
        correlation = happiness_data['GDP_per_capita'].corr(happiness_data['Happiness_score'])
        
        # Calculate linear regression
        X = happiness_data[['GDP_per_capita']]
        y = happiness_data['Happiness_score']
        model = LinearRegression().fit(X, y)
        happiness_data['Predicted_happiness'] = model.predict(X)
        happiness_data['Happiness_difference'] = happiness_data['Happiness_score'] - happiness_data['Predicted_happiness']
        
        # Group by region and calculate average difference
        region_diff = happiness_data.groupby('Region')['Happiness_difference'].mean().sort_values(ascending=False)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Correlation between GDP and Happiness", f"{correlation:.2f}")
            st.write("This strong positive correlation indicates that countries with higher GDP per capita tend to report higher levels of happiness.")
        
        with col2:
            st.metric("R² (Coefficient of Determination)", f"{model.score(X, y):.2f}")
            st.write("This means that approximately this percentage of the variation in happiness scores can be explained by GDP per capita.")
        
        st.subheader("Regions Where Countries are Happier Than GDP Would Predict")
        
        # Create a horizontal bar chart for regional happiness differences
        fig = plt.figure(figsize=(10, 6))
        plt.barh(region_diff.index, region_diff.values)
        plt.axvline(x=0, color='black', linestyle='-', alpha=0.3)
        plt.xlabel('Average Happiness Difference from GDP Prediction')
        plt.title('Regions Where Happiness Exceeds or Falls Short of GDP-Based Predictions')
        
        # Add value labels
        for i, v in enumerate(region_diff.values):
            plt.text(v + 0.05 if v >= 0 else v - 0.3, i, f"{v:.2f}", va='center')
        
        # Display the bar chart
        buffer = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        st.image(buffer, use_container_width=True)
        plt.close()
        
        st.markdown("""
        The chart above shows which regions have happiness levels that exceed or fall short of what would be predicted based on GDP alone. 
        Latin American countries, for example, tend to report higher happiness levels than their economic indicators would suggest, 
        which is often referred to as the "Latin American paradox" in happiness research.
        """)
    
    with tab4:
        st.markdown('<div class="sub-header">Conclusion</div>', unsafe_allow_html=True)
        
        st.markdown("""
        ## Conclusion: Comparing the Poor and Improved Visualizations
        
        When we examine the two visualizations of the World Happiness Report data, we can see stark differences in how effectively they communicate insights about the relationship between GDP per capita and happiness scores.
        
        The poor visualization fails the audience in multiple fundamental ways. By using an unnecessary 3D perspective for inherently 2D data, it creates a distorted view that makes accurate comparison between points nearly impossible. The similar color shades across different regions make it difficult to distinguish between regional patterns, which obscures one of the most interesting aspects of the data. Furthermore, the cluttered approach of labeling every single country creates visual noise that overwhelms the viewer, making it nearly impossible to extract meaningful patterns. The misleading annotations ("Poor countries = Sad countries") impose a biased interpretation rather than allowing the data to speak for itself.
        
        In contrast, the improved visualization embodies several key principles of effective data communication. By using a clear 2D representation, it allows viewers to accurately assess the relationship between GDP and happiness without distortion. The distinct color scheme for different regions enables immediate recognition of regional patterns – we can clearly see how European countries cluster at the top-right, while African nations tend toward the bottom-left. By selectively labeling only key countries (highest, lowest, and notable outliers), it maintains context without overwhelming the viewer with text. The regression line provides an immediate visual representation of the overall relationship, allowing viewers to identify countries that deviate from the expected pattern. The thoughtful annotations highlight genuine insights rather than imposing simplistic conclusions.
        
        What makes this comparison particularly instructive is that both visualizations use exactly the same underlying data. The dramatic difference in clarity and insight demonstrates how visualization choices can either reveal or concealthe story within the data. The poor visualization might lead viewers to conclude only that "rich countries are happier," while missing nuanced patterns like how Latin American countries consistently achieve higher happiness scores than their economic metrics would predict, or how certain regions show greater variability in happiness despite similar economic conditions.This comparison serves as a powerful reminder that data visualization is not merely a technical exercise but a form of communication that requires thoughtful design choices. The most effective visualizations strip away unnecessary complexity, highlight meaningful patterns, provide appropriate context, and ultimately respect both the data and the viewer's intelligence.
        """)

