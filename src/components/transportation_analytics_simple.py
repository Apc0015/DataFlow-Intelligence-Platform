"""
Transportation Analytics component - Simplified version
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
    
    st.title("Transportation Analytics")
    
    # Overview section
    st.subheader("Overview")
    st.write("""
    Transportation Analytics provides comprehensive aviation analytics by transforming complex flight data 
    into strategic business insights. This solution empowers aviation stakeholders with data-driven tools 
    for route optimization, operational efficiency, and competitive market analysis.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Route Optimization**")
        st.write("Advanced Analytics")
    with col2:
        st.write("**Market Intelligence**")
        st.write("Comprehensive Insights")
    with col3:
        st.write("**Operational Analytics**")
        st.write("Strategic Performance")
    
    # Development approach
    st.subheader("Development Approach")
    st.write("**Challenge Addressed:** Aviation data is complex and fragmented, making it difficult to extract actionable business insights for strategic decision-making.")
    st.write("**Solution Implemented:** Research into aviation industry needs informed the development of an integrated analytics platform that combines geospatial analysis, operational metrics, and competitive intelligence.")
    st.write("**Technical Skills Applied:** Advanced geospatial programming with Folium, interactive dashboard development, aviation domain expertise, and business intelligence visualization techniques.")
    
    # Sidebar configuration
    st.sidebar.subheader("Configuration")
    st.sidebar.write("Select Aviation Hub for Analysis")
    
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
    st.sidebar.write("**Analytics Approach**")
    st.sidebar.write("These strategic hubs were selected because each represents distinct market positioning opportunities. The analysis framework reveals how operational patterns drive competitive advantages.")
    
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
    
    # Create analytical framework sections
    tab1, tab2, tab3 = st.tabs([
        "Route Intelligence", 
        "Performance Analytics", 
        "Competitive Intelligence"
    ])
    
    with tab1:
        render_route_intelligence(airport_code, airport_data)
    
    with tab2:
        render_performance_analytics(airport_data)
    
    with tab3:
        render_competitive_intelligence(airport_data)

def render_route_intelligence(airport_code, airport_data):
    """Render the route intelligence mapping system"""
    
    st.subheader("Route Intelligence Mapping System")
    
    st.write("""
    This interactive route visualization system transforms complex aviation data into 
    strategic business intelligence. The solution enables decision-makers to identify network expansion 
    opportunities, optimize capacity allocation, and develop competitive positioning strategies.
    """)
    
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
    
    # Create interactive map
    flight_map = folium.Map(
        location=[source_lat, source_lon], 
        zoom_start=3,
        tiles='OpenStreetMap'
    )
    
    # Add the source airport marker
    folium.Marker(
        location=[source_lat, source_lon],
        popup=f"<b>{airport_code}</b><br>Hub Airport",
        icon=folium.Icon(color="red", icon="plane", prefix="fa"),
        tooltip=f"{airport_code} - Hub Airport"
    ).add_to(flight_map)
    
    # Add destination markers and flight paths
    unique_destinations = airport_data.drop_duplicates(subset=['destination_airport'])
    
    for _, flight in unique_destinations.iterrows():
        # Calculate flight frequency for this destination
        flight_count = len(airport_data[airport_data['destination_airport'] == flight['destination_airport']])
        
        # Destination marker
        popup_content = f"""
        <b>{flight['destination_airport']}</b><br>
        {flight['destination_name']}<br>
        <i>{'Domestic' if flight['domestic'] else 'International'}</i><br>
        <b>Flights: {flight_count}</b>
        """
        
        folium.Marker(
            location=[flight['destination_lat'], flight['destination_lon']],
            popup=popup_content,
            icon=folium.Icon(
                color="blue" if flight['domestic'] else "green", 
                icon="plane", 
                prefix="fa"
            ),
            tooltip=f"{flight['destination_airport']} - {flight_count} flights"
        ).add_to(flight_map)
        
        # Flight path
        line_weight = max(2, min(8, flight_count / 3))
        line_opacity = max(0.4, min(0.8, flight_count / 20))
        
        folium.PolyLine(
            locations=[[source_lat, source_lon], [flight['destination_lat'], flight['destination_lon']]],
            color="#4CAF50" if flight['domestic'] else "#2196F3",
            weight=line_weight,
            opacity=line_opacity,
            tooltip=f"Route to {flight['destination_airport']} - {flight_count} flights"
        ).add_to(flight_map)
    
    # Add map legend
    st.info("Blue routes: Domestic flights | Green routes: International flights | Route thickness indicates flight frequency")
    
    # Display the map
    folium_static(flight_map, width=None, height=400)
    
    # Top destinations analysis
    st.subheader("High-Value Market Destinations")
    
    top_destinations = airport_data['destination_airport'].value_counts().reset_index()
    top_destinations.columns = ['Destination', 'Number of Flights']
    top_destinations = top_destinations.head(8)
    
    # Get full names for the destinations
    dest_names = airport_data.groupby('destination_airport')['destination_name'].first().to_dict()
    top_destinations['Destination Name'] = top_destinations['Destination'].map(dest_names)
    top_destinations['Route Type'] = top_destinations['Destination'].map(
        airport_data.set_index('destination_airport')['domestic'].to_dict()
    ).map({True: 'Domestic', False: 'International'})
    
    # Bar chart
    fig = px.bar(
        top_destinations,
        y='Destination',
        x='Number of Flights',
        text='Number of Flights',
        color='Route Type',
        color_discrete_map={'Domestic': '#4CAF50', 'International': '#2196F3'},
        orientation='h',
        title='Top Revenue-Generating Routes',
        hover_data=['Destination Name']
    )
    
    fig.update_traces(textposition='outside')
    fig.update_layout(
        title_x=0.5,
        height=400,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    High-frequency routes represent the backbone of operational revenue and market dominance. Route concentration 
    patterns indicate opportunities for strategic partnerships, code-sharing agreements, and capacity optimization.
    """)

def render_performance_analytics(airport_data):
    """Render the performance analytics dashboard"""
    
    st.subheader("Operational Performance Analytics")
    
    st.write("""
    Understanding flight distribution patterns and temporal optimization opportunities enables 
    resource allocation efficiency, capacity planning, and revenue maximization strategies.
    """)
    
    # Market diversification analysis
    st.subheader("Market Portfolio Analysis")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        domestic_count = airport_data['domestic'].value_counts()
        total_flights = len(airport_data)
        
        # Pie chart
        fig = go.Figure(data=[go.Pie(
            labels=['Domestic Routes', 'International Routes'],
            values=[domestic_count.get(True, 0), domestic_count.get(False, 0)],
            hole=0.4,
            marker_colors=['#4CAF50', '#2196F3'],
            textinfo='label+percent+value'
        )])
        
        fig.update_layout(
            title='Market Diversification: Domestic vs International Operations',
            title_x=0.5,
            height=400,
            showlegend=True,
            annotations=[dict(text=f'Total<br>{total_flights}<br>Flights', x=0.5, y=0.5, font_size=14, showarrow=False)]
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Key metrics
        domestic_pct = (domestic_count.get(True, 0) / total_flights * 100)
        international_pct = (domestic_count.get(False, 0) / total_flights * 100)
        
        st.metric("Domestic Focus", f"{domestic_pct:.1f}%", f"{domestic_count.get(True, 0)} flights")
        st.metric("Global Reach", f"{international_pct:.1f}%", f"{domestic_count.get(False, 0)} flights")
    
    # Temporal analysis
    st.subheader("Temporal Optimization Analysis")
    
    # Create time categories
    airport_data_copy = airport_data.copy()
    airport_data_copy['time_category'] = pd.cut(
        airport_data_copy['flight_hour'],
        bins=[0, 6, 12, 18, 24],
        labels=['Early Morning (0-6)', 'Morning (6-12)', 'Afternoon (12-18)', 'Evening (18-24)'],
        include_lowest=True
    )
    
    time_distribution = airport_data_copy['time_category'].value_counts().reset_index()
    time_distribution.columns = ['Time Period', 'Number of Flights']
    time_distribution['Percentage'] = (time_distribution['Number of Flights'] / len(airport_data_copy) * 100).round(1)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Pie chart
        fig = px.pie(
            time_distribution,
            values='Number of Flights',
            names='Time Period',
            title='Flight Distribution by Time Period',
            color_discrete_sequence=['#FF9800', '#4CAF50', '#2196F3', '#9C27B0'],
            hole=0.4
        )
        
        fig.update_traces(
            textposition='inside', 
            textinfo='percent+label'
        )
        
        fig.update_layout(
            height=400,
            showlegend=True,
            title_x=0.5
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Time-based insights
        peak_time = time_distribution.loc[time_distribution['Number of Flights'].idxmax(), 'Time Period']
        
        st.write("**Operational Insights**")
        for _, row in time_distribution.iterrows():
            is_peak = row['Time Period'] == peak_time
            if is_peak:
                st.write(f"**{row['Time Period']}: {row['Number of Flights']} flights ({row['Percentage']}%) - PEAK**")
            else:
                st.write(f"{row['Time Period']}: {row['Number of Flights']} flights ({row['Percentage']}%)")
    
    st.write("""
    Temporal distribution patterns reveal peak capacity utilization windows and identify opportunities 
    for dynamic pricing strategies, resource optimization, and competitive scheduling advantages.
    """)

def render_competitive_intelligence(airport_data):
    """Render the competitive intelligence framework"""
    
    st.subheader("Competitive Intelligence & Market Share")
    
    st.write("""
    Competitive intelligence reveals market concentration, partnership opportunities, and 
    strategic positioning for market share expansion and defensive strategies.
    """)
    
    # Enhanced airline analysis
    st.subheader("Market Leadership Analysis")
    
    airline_counts = airport_data['airline'].value_counts().reset_index().head(8)
    airline_counts.columns = ['Airline', 'Number of Flights']
    airline_counts['Market Share %'] = (airline_counts['Number of Flights'] / len(airport_data) * 100).round(1)
    
    # Bar chart with market share
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=airline_counts['Airline'],
        y=airline_counts['Number of Flights'],
        text=[f"{row['Number of Flights']}<br>({row['Market Share %']}%)" 
              for _, row in airline_counts.iterrows()],
        textposition='auto',
        marker_color='#4CAF50'
    ))
    
    fig.update_layout(
        title='Market Share Leaders: Competitive Positioning Analysis',
        xaxis_title='Airline Carrier',
        yaxis_title='Market Presence (Number of Flights)',
        xaxis={'categoryorder': 'total descending'},
        title_x=0.5,
        height=450
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Strategic market segmentation
    st.subheader("Strategic Market Segmentation Analysis")
    
    # Prepare data for segmentation analysis
    airline_by_type = airport_data.groupby(['airline', 'domestic']).size().reset_index()
    airline_by_type.columns = ['Airline', 'Domestic', 'Count']
    airline_by_type['Flight Type'] = airline_by_type['Domestic'].map({True: 'Domestic', False: 'International'})
    
    # Filter to top airlines
    top_airlines = airline_counts['Airline'].head(6).tolist()
    airline_by_type_filtered = airline_by_type[airline_by_type['Airline'].isin(top_airlines)]
    
    # Grouped bar chart
    fig = px.bar(
        airline_by_type_filtered,
        x='Airline',
        y='Count',
        color='Flight Type',
        color_discrete_map={'Domestic': '#4CAF50', 'International': '#2196F3'},
        barmode='group',
        title='Competitive Strategy Matrix: Market Specialization vs. Diversification',
        text='Count'
    )
    
    fig.update_traces(textposition='outside')
    fig.update_layout(
        title_x=0.5,
        xaxis_title='Airline Carrier',
        yaxis_title='Flight Operations Count',
        height=450,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Competitive insights
    col1, col2 = st.columns(2)
    
    with col1:
        # Market concentration analysis
        total_airlines = len(airline_counts)
        top_3_share = airline_counts.head(3)['Market Share %'].sum()
        
        st.metric("Market Concentration", f"{top_3_share:.1f}%", "Top 3 carriers control")
    
    with col2:
        st.metric("Carrier Diversity", f"{total_airlines}", "Active airlines")
    
    st.write("""
    Market specialization patterns reveal competitive advantages and strategic positioning opportunities. 
    Balanced carriers demonstrate diversified risk strategies and operational flexibility, while specialized carriers 
    show focused market dominance approaches.
    """)