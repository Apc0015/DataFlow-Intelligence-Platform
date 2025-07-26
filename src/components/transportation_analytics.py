"""
Transportation Analytics component for the DataFlow Intelligence Platform
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import folium_static
from utils.data_handler import DataHandler

def render_transportation_analytics():
    """Render the transportation analytics page"""
    
    st.markdown('<div class="main-header">✈️ Transportation Intelligence Hub</div>', unsafe_allow_html=True)
    
    # Project overview with enhanced styling
    st.markdown("""
    <div class="portfolio-card fade-in-up">
        <h3 style="color: #1e293b; margin-bottom: 1rem;">🎯 Strategic Analytics Solution</h3>
        <p style="font-size: 1.1rem; line-height: 1.6; color: #475569;">
            Transportation Intelligence Hub addresses the critical need for comprehensive aviation analytics by 
            transforming complex flight data into strategic business insights. This solution empowers aviation stakeholders with 
            data-driven tools for route optimization, operational efficiency, and competitive market analysis.
        </p>
        
        <div style="display: flex; justify-content: space-around; margin-top: 2rem; flex-wrap: wrap;">
            <div style="text-align: center; margin: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎯</div>
                <p style="margin: 0; font-weight: 600; color: #1e293b;">Route Optimization</p>
                <p style="margin: 0; font-size: 0.9rem; color: #64748b;">Advanced Analytics</p>
            </div>
            <div style="text-align: center; margin: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">📊</div>
                <p style="margin: 0; font-weight: 600; color: #1e293b;">Market Intelligence</p>
                <p style="margin: 0; font-size: 0.9rem; color: #64748b;">Comprehensive Insights</p>
            </div>
            <div style="text-align: center; margin: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">⚡</div>
                <p style="margin: 0; font-weight: 600; color: #1e293b;">Operational Analytics</p>
                <p style="margin: 0; font-size: 0.9rem; color: #64748b;">Strategic Performance</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Development approach section
    st.markdown("""
    <div class="value-prop fade-in-up">
        <h3 style="color: #92400e; margin-bottom: 1rem;">💡 Development Approach</h3>
        <div style="margin-bottom: 1rem;">
            <p style="font-size: 1.05rem; line-height: 1.6; color: #78350f; margin-bottom: 1rem;">
                <strong>Challenge Addressed:</strong> Aviation data is complex and fragmented, making it difficult to extract 
                actionable business insights for strategic decision-making.
            </p>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #78350f; margin-bottom: 1rem;">
                <strong>Solution Implemented:</strong> Research into aviation industry needs informed the development of an integrated analytics platform 
                that combines geospatial analysis, operational metrics, and competitive intelligence in an intuitive interface.
            </p>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #78350f;">
                <strong>Technical Skills Applied:</strong> Advanced geospatial programming with Folium, interactive dashboard development, 
                aviation domain expertise, and business intelligence visualization techniques.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar configuration with improved styling
    st.sidebar.markdown("## 🎯 Hub Analysis Configuration")
    st.sidebar.markdown("**Select Aviation Hub for Deep Dive Analysis**")
    
    airport_options = [
        "JFK - John F. Kennedy International (New York)",
        "ATL - Hartsfield-Jackson Atlanta International",
        "MIA - Miami International", 
        "BOS - Boston Logan International",
        "PHL - Philadelphia International"
    ]
    
    airport = st.sidebar.selectbox(
        "Select Major East Coast Hub:",
        airport_options,
        index=0
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div class="insight-box" style="margin: 1rem 0;">
        <h4 style="color: #0ea5e9; margin-bottom: 0.5rem;">💡 Analytics Approach</h4>
        <p style="font-size: 0.9rem; line-height: 1.5; color: #475569;">
            These strategic hubs were selected because each represents distinct market positioning opportunities. 
            The analysis framework reveals how operational patterns drive competitive advantages and identifies 
            optimization opportunities for route planning and capacity allocation.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get airport code
    airport_code = airport.split(" - ")[0]
    
    # Load airport data with error handling
    try:
        airport_data = DataHandler.load_airport_data(airport_code)
        
        if airport_data.empty:
            st.error("No data available for the selected airport. Please try another airport.")
            return
            
    except Exception as e:
        st.error(f"Error loading airport data: {str(e)}")
        return
    
    # Add spacing before tabs
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # Create analytical framework sections
    tab1, tab2, tab3 = st.tabs([
        "🗺️ Route Intelligence System", 
        "📊 Performance Analytics Dashboard", 
        "🏢 Competitive Intelligence Framework"
    ])
    
    with tab1:
        st.markdown("<div style='padding-top: 1rem;'>", unsafe_allow_html=True)
        render_route_intelligence(airport_code, airport_data)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<div style='padding-top: 1rem;'>", unsafe_allow_html=True)
        render_performance_analytics(airport_data)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<div style='padding-top: 1rem;'>", unsafe_allow_html=True)
        render_competitive_intelligence(airport_data)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Strategic insights section
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    render_strategic_insights()

def render_route_intelligence(airport_code, airport_data):
    """Render the route intelligence mapping system"""
    
    st.markdown('<div class="sub-header">🗺️ Route Intelligence Mapping System</div>', unsafe_allow_html=True)
    
    # Wrap content in a container for proper layout
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    # Innovation context
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #0ea5e9; margin-bottom: 0.5rem;">📈 Analytics Innovation</h4>
        <p style="line-height: 1.5; color: #475569;">
            This interactive route visualization system transforms complex aviation data into 
            strategic business intelligence. The solution enables decision-makers to identify network expansion 
            opportunities, optimize capacity allocation, and develop competitive positioning strategies through 
            data-driven insights.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Airport coordinates
    airport_coordinates = {
        "JFK": {"lat": 40.6413, "lon": -73.7781},
        "ATL": {"lat": 33.6407, "lon": -84.4277},
        "MIA": {"lat": 25.7932, "lon": -80.2906},
        "BOS": {"lat": 42.3656, "lon": -71.0096},
        "PHL": {"lat": 39.8729, "lon": -75.2437}
    }
    
    # Get source coordinates
    if airport_code not in airport_coordinates:
        st.error(f"Airport coordinates not found for {airport_code}")
        return
        
    source_lat = airport_coordinates[airport_code]["lat"]
    source_lon = airport_coordinates[airport_code]["lon"]
    
    # Create enhanced interactive map
    flight_map = folium.Map(
        location=[source_lat, source_lon], 
        zoom_start=3,
        tiles='OpenStreetMap'
    )
    
    # Add the source airport marker with custom icon
    folium.Marker(
        location=[source_lat, source_lon],
        popup=folium.Popup(f"<b>{airport_code}</b><br>Hub Airport", max_width=200),
        icon=folium.Icon(color="red", icon="plane", prefix="fa"),
        tooltip=f"{airport_code} - Hub Airport"
    ).add_to(flight_map)
    
    # Add destination markers and flight paths with enhanced styling
    unique_destinations = airport_data.drop_duplicates(subset=['destination_airport'])
    
    for _, flight in unique_destinations.iterrows():
        # Calculate flight frequency for this destination
        flight_count = len(airport_data[airport_data['destination_airport'] == flight['destination_airport']])
        
        # Destination marker with flight count info
        popup_content = f"""
        <b>{flight['destination_airport']}</b><br>
        {flight['destination_name']}<br>
        <i>{'Domestic' if flight['domestic'] else 'International'}</i><br>
        <b>Flights: {flight_count}</b>
        """
        
        folium.Marker(
            location=[flight['destination_lat'], flight['destination_lon']],
            popup=folium.Popup(popup_content, max_width=250),
            icon=folium.Icon(
                color="blue" if flight['domestic'] else "green", 
                icon="plane", 
                prefix="fa"
            ),
            tooltip=f"{flight['destination_airport']} - {flight_count} flights"
        ).add_to(flight_map)
        
        # Enhanced flight path with weight based on frequency
        line_weight = max(2, min(8, flight_count / 3))
        line_opacity = max(0.4, min(0.8, flight_count / 20))
        
        folium.PolyLine(
            locations=[[source_lat, source_lon], [flight['destination_lat'], flight['destination_lon']]],
            color="#2563eb" if flight['domestic'] else "#059669",
            weight=line_weight,
            opacity=line_opacity,
            tooltip=f"Route to {flight['destination_airport']} - {flight_count} flights"
        ).add_to(flight_map)
    
    # Add map legend
    st.markdown("""
    <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; border-left: 4px solid #0ea5e9;">
        <strong>🗺️ Interactive Route Network Visualization</strong><br>
        <span style="color: #0ea5e9;">●</span> Domestic routes (blue): Core revenue streams and market positioning<br>
        <span style="color: #10b981;">●</span> International routes (green): Global expansion opportunities<br>
        <small>Route thickness indicates flight frequency and market importance</small>
    </div>
    """, unsafe_allow_html=True)
    
    # Display the enhanced map with proper container
    st.markdown("""
    <div style="margin: 1rem 0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px -3px rgba(0, 0, 0, 0.1);">
    """, unsafe_allow_html=True)
    
    folium_static(flight_map, width=None, height=400)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Top destinations analysis with enhanced visualization
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">🎯 High-Value Market Destinations</h3>', unsafe_allow_html=True)
    
    top_destinations = airport_data['destination_airport'].value_counts().reset_index()
    top_destinations.columns = ['Destination', 'Number of Flights']
    top_destinations = top_destinations.head(8)  # Show more destinations
    
    # Get full names for the destinations
    dest_names = airport_data.groupby('destination_airport')['destination_name'].first().to_dict()
    top_destinations['Destination Name'] = top_destinations['Destination'].map(dest_names)
    top_destinations['Route Type'] = top_destinations['Destination'].map(
        airport_data.set_index('destination_airport')['domestic'].to_dict()
    ).map({True: 'Domestic', False: 'International'})
    
    # Enhanced horizontal bar chart
    fig = px.bar(
        top_destinations,
        y='Destination',
        x='Number of Flights',
        text='Number of Flights',
        color='Route Type',
        color_discrete_map={'Domestic': '#2563eb', 'International': '#059669'},
        orientation='h',
        title='Strategic Market Prioritization: Top Revenue-Generating Routes',
        hover_data=['Destination Name']
    )
    
    fig.update_traces(textposition='outside')
    fig.update_layout(
        title_font_size=16,
        title_x=0.5,
        height=400,
        showlegend=True,
        xaxis_title="Number of Flights",
        yaxis_title="Destination Airport"
    )
    
    st.plotly_chart(fig, use_container_width=True, key="enhanced_top_destinations")
    
    # Strategic insight
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #0ea5e9; margin-bottom: 0.5rem;">💡 Strategic Intelligence</h4>
        <p style="line-height: 1.5; color: #475569;">
            High-frequency routes represent the backbone of operational revenue and market dominance. Route concentration 
            patterns indicate opportunities for strategic partnerships, code-sharing agreements, and capacity optimization. 
            The domestic-international mix reveals portfolio diversification and risk management strategies.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Close content section container
    st.markdown('</div>', unsafe_allow_html=True)

def render_performance_analytics(airport_data):
    """Render the performance analytics dashboard"""
    
    st.markdown('<div class="sub-header">📊 Operational Performance Analytics</div>', unsafe_allow_html=True)
    
    # Wrap content in a container for proper layout
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    # Business context
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #0ea5e9; margin-bottom: 0.5rem;">⚡ Operational Excellence Metrics</h4>
        <p style="line-height: 1.5; color: #475569;">
            Understanding flight distribution patterns and temporal optimization opportunities enables 
            resource allocation efficiency, capacity planning, and revenue maximization strategies.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced market diversification analysis
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">🌍 Market Portfolio Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        domestic_count = airport_data['domestic'].value_counts()
        total_flights = len(airport_data)
        
        # Enhanced pie chart
        fig = go.Figure(data=[go.Pie(
            labels=['Domestic Routes', 'International Routes'],
            values=[domestic_count.get(True, 0), domestic_count.get(False, 0)],
            hole=0.4,
            marker_colors=['#0ea5e9', '#10b981'],
            textinfo='label+percent+value',
            textfont_size=12,
            hovertemplate='<b>%{label}</b><br>Flights: %{value}<br>Percentage: %{percent}<extra></extra>'
        )])
        
        fig.update_layout(
            title='Market Diversification: Domestic vs International Operations',
            title_x=0.5,
            height=400,
            showlegend=True,
            annotations=[dict(text=f'Total<br>{total_flights}<br>Flights', x=0.5, y=0.5, font_size=14, showarrow=False)]
        )
        
        st.plotly_chart(fig, use_container_width=True, key="market_diversification")
    
    with col2:
        # Key metrics
        domestic_pct = (domestic_count.get(True, 0) / total_flights * 100)
        international_pct = (domestic_count.get(False, 0) / total_flights * 100)
        
        st.markdown(f"""
        <div class="metric-card" style="margin-bottom: 1rem;">
            <h4 style="margin: 0;">🏠 Domestic Focus</h4>
            <h2 style="margin: 0.5rem 0;">{domestic_pct:.1f}%</h2>
            <p style="margin: 0; opacity: 0.8;">{domestic_count.get(True, 0)} flights</p>
        </div>
        
        <div class="metric-card">
            <h4 style="margin: 0;">🌍 Global Reach</h4>
            <h2 style="margin: 0.5rem 0;">{international_pct:.1f}%</h2>
            <p style="margin: 0; opacity: 0.8;">{domestic_count.get(False, 0)} flights</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Enhanced temporal analysis
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">⏰ Temporal Optimization Analysis</h3>', unsafe_allow_html=True)
    
    # Create time categories with better binning
    airport_data_copy = airport_data.copy()
    airport_data_copy['time_category'] = pd.cut(
        airport_data_copy['flight_hour'],
        bins=[0, 6, 12, 18, 24],
        labels=['Early Morning\n(0-6)', 'Morning\n(6-12)', 'Afternoon\n(12-18)', 'Evening\n(18-24)'],
        include_lowest=True
    )
    
    time_distribution = airport_data_copy['time_category'].value_counts().reset_index()
    time_distribution.columns = ['Time Period', 'Number of Flights']
    time_distribution['Percentage'] = (time_distribution['Number of Flights'] / len(airport_data_copy) * 100).round(1)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Enhanced donut chart
        fig = px.pie(
            time_distribution,
            values='Number of Flights',
            names='Time Period',
            title='Flight Distribution by Time Period',
            color_discrete_sequence=['#1e293b', '#475569', '#64748b', '#94a3b8'],
            hole=0.4
        )
        
        fig.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            hovertemplate='<b>%{label}</b><br>Flights: %{value}<br>Percentage: %{percent}<extra></extra>'
        )
        
        fig.update_layout(
            height=400,
            showlegend=True,
            title_x=0.5
        )
        
        st.plotly_chart(fig, use_container_width=True, key="time_distribution")
    
    with col2:
        # Time-based insights
        peak_time = time_distribution.loc[time_distribution['Number of Flights'].idxmax(), 'Time Period']
        peak_flights = time_distribution['Number of Flights'].max()
        
        # Build the complete HTML content
        insights_html = """
        <div class="insight-box" style="padding: 1.5rem; min-height: auto;">
            <h4 style="color: #0ea5e9; margin-bottom: 1rem;">⏰ Operational Insights</h4>
        """
        
        for _, row in time_distribution.iterrows():
            is_peak = row['Time Period'] == peak_time
            if is_peak:
                style_class = "font-weight: bold; color: #0ea5e9;"
                icon = "🔥"
            else:
                style_class = "color: #64748b;"
                icon = "📊"
            
            insights_html += f"""
            <div style="margin-bottom: 0.8rem;">
                <span style="{style_class}">{icon} {row['Time Period']}: {row['Number of Flights']} flights ({row['Percentage']}%)</span>
            </div>
            """
        
        insights_html += "</div>"
        st.markdown(insights_html, unsafe_allow_html=True)
    
    # Strategic insight
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #0ea5e9; margin-bottom: 0.5rem;">💡 Operational Excellence Insight</h4>
        <p style="line-height: 1.5; color: #475569;">
            Temporal distribution patterns reveal peak capacity utilization windows and identify opportunities 
            for dynamic pricing strategies, resource optimization, and competitive scheduling advantages. 
            Understanding time-based demand enables strategic workforce allocation and infrastructure planning.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Close content section container
    st.markdown('</div>', unsafe_allow_html=True)

def render_competitive_intelligence(airport_data):
    """Render the competitive intelligence framework"""
    
    st.markdown('<div class="sub-header">🏢 Competitive Intelligence & Market Share</div>', unsafe_allow_html=True)
    
    # Wrap content in a container for proper layout
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    # Business context
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #0ea5e9; margin-bottom: 0.5rem;">🎯 Market Positioning Analysis</h4>
        <p style="line-height: 1.5; color: #475569;">
            Competitive intelligence reveals market concentration, partnership opportunities, and 
            strategic positioning for market share expansion and defensive strategies.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced airline analysis
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">🏆 Market Leadership Analysis</h3>', unsafe_allow_html=True)
    
    airline_counts = airport_data['airline'].value_counts().reset_index().head(8)
    airline_counts.columns = ['Airline', 'Number of Flights']
    airline_counts['Market Share %'] = (airline_counts['Number of Flights'] / len(airport_data) * 100).round(1)
    
    # Enhanced bar chart with market share
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=airline_counts['Airline'],
        y=airline_counts['Number of Flights'],
        text=[f"{row['Number of Flights']}<br>({row['Market Share %']}%)" 
              for _, row in airline_counts.iterrows()],
        textposition='auto',
        marker_color='#0ea5e9',
        hovertemplate='<b>%{x}</b><br>Flights: %{y}<br>Market Share: %{customdata}%<extra></extra>',
        customdata=airline_counts['Market Share %']
    ))
    
    fig.update_layout(
        title='Market Share Leaders: Competitive Positioning Analysis',
        xaxis_title='Airline Carrier',
        yaxis_title='Market Presence (Number of Flights)',
        xaxis={'categoryorder': 'total descending'},
        title_font_size=16,
        title_x=0.5,
        height=450
    )
    
    st.plotly_chart(fig, use_container_width=True, key="enhanced_airline_analysis")
    
    # Strategic market segmentation
    st.markdown('<h3 style="color: #1a202c; font-weight: 700; margin: 2rem 0 1rem 0;">🌐 Strategic Market Segmentation Analysis</h3>', unsafe_allow_html=True)
    
    # Prepare data for segmentation analysis
    airline_by_type = airport_data.groupby(['airline', 'domestic']).size().reset_index()
    airline_by_type.columns = ['Airline', 'Domestic', 'Count']
    airline_by_type['Flight Type'] = airline_by_type['Domestic'].map({True: 'Domestic', False: 'International'})
    
    # Filter to top airlines
    top_airlines = airline_counts['Airline'].head(6).tolist()
    airline_by_type_filtered = airline_by_type[airline_by_type['Airline'].isin(top_airlines)]
    
    # Enhanced grouped bar chart
    fig = px.bar(
        airline_by_type_filtered,
        x='Airline',
        y='Count',
        color='Flight Type',
        color_discrete_map={'Domestic': '#2563eb', 'International': '#059669'},
        barmode='group',
        title='Competitive Strategy Matrix: Market Specialization vs. Diversification',
        text='Count'
    )
    
    fig.update_traces(textposition='outside')
    fig.update_layout(
        title_font_size=16,
        title_x=0.5,
        xaxis_title='Airline Carrier',
        yaxis_title='Flight Operations Count',
        height=450,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True, key="market_segmentation")
    
    # Competitive insights
    col1, col2 = st.columns(2)
    
    with col1:
        # Market concentration analysis
        total_airlines = len(airline_counts)
        top_3_share = airline_counts.head(3)['Market Share %'].sum()
        
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="margin: 0;">🎯 Market Concentration</h4>
            <h2 style="margin: 0.5rem 0;">{top_3_share:.1f}%</h2>
            <p style="margin: 0; opacity: 0.8;">Top 3 carriers control</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="margin: 0;">✈️ Carrier Diversity</h4>
            <h2 style="margin: 0.5rem 0;">{total_airlines}</h2>
            <p style="margin: 0; opacity: 0.8;">Active airlines</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Strategic intelligence summary
    st.markdown("""
    <div class="insight-box">
        <h4 style="color: #0ea5e9; margin-bottom: 0.5rem;">💡 Competitive Strategy Intelligence</h4>
        <p style="line-height: 1.5; color: #475569;">
            Market specialization patterns reveal competitive advantages and strategic positioning opportunities. 
            Balanced carriers demonstrate diversified risk strategies and operational flexibility, while specialized carriers 
            show focused market dominance approaches. Understanding competitor positioning enables strategic partnership 
            identification and competitive response planning.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Close content section container
    st.markdown('</div>', unsafe_allow_html=True)

def render_strategic_insights():
    """Render strategic insights section"""
    
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
        
        st.markdown("## Recommendations")
        st.markdown("""
        **Strategic Priorities:**
        - Expand capacity on high-frequency domestic routes
        - Develop international partnerships for global market access
        - Implement dynamic pricing based on temporal demand patterns
        - Monitor competitive positioning for defensive strategies
        - Invest in operational efficiency improvements during peak periods
        """)