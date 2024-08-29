
import numpy as np
import pandas as pd
from taipy.gui import Markdown
import plotly.express as px
import plotly.graph_objects as go
import pycountry

from data.data import geojson, origin

# Function to convert country name to ISO 3166-1 alpha-3 code
def country_name_to_code(name):
    try:
        return pycountry.countries.search_fuzzy(name)[0].alpha_3
    except:
        return None

# Process origin data
def process_origin_data(origin):
    # Ensure 'date' column is datetime
    origin['date'] = pd.to_datetime(origin['date'])
    
    # Convert country names to ISO 3166-1 alpha-3 codes
    origin['country_code'] = origin['country'].apply(country_name_to_code)
    
    # Total counts per country
    country_ip_counts = origin.groupby('country_code').size().reset_index(name='IP_Count')
    country_ip_counts.columns = ['COUNTRY', 'IP_Count']
    
    # Counts per country per day
    daily_counts = origin.groupby(['date', 'country_code']).size().reset_index(name='IP_Count')
    daily_counts.columns = ['Date', 'COUNTRY', 'IP_Count']
    
    # Ensure all countries are represented for each date
    all_dates = daily_counts['Date'].unique()
    all_countries = origin['country_code'].unique()
    
    # Create a complete DataFrame with all date-country combinations
    complete_daily = pd.DataFrame([(date, country) for date in all_dates for country in all_countries],
                                  columns=['Date', 'COUNTRY'])
    
    # Merge with the actual counts, filling missing values with 0
    daily_counts = complete_daily.merge(daily_counts, on=['Date', 'COUNTRY'], how='left').fillna(0)
    
    # Convert Date to string for choropleth
    daily_counts['Date'] = daily_counts['Date'].astype(str)
    
    return country_ip_counts, daily_counts

country_ip_data, daily_country_data = process_origin_data(origin)
total_ips = country_ip_data['IP_Count'].sum()
countries_selected = []

# Create daily counts
daily_counts = daily_country_data.groupby('Date')['IP_Count'].sum().reset_index()

# Create total IP count map
ip_map = px.choropleth_mapbox(country_ip_data,
                           geojson=geojson,
                           featureidkey="id",
                           locations="COUNTRY",
                           color="IP_Count",
                           hover_name="COUNTRY",
                           zoom=1,
                           center={"lat": 0, "lon": 0},
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           labels={"IP_Count": "Total IP Count"},
                           title="Total IP Count by Country")

ip_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                     coloraxis_colorbar=dict(title="Total IPs"),
                     height=700)

# Create daily country count map
daily_country_map = px.choropleth(daily_country_data,
                           geojson=geojson,
                           featureidkey="id",
                           locations="COUNTRY",
                           color="IP_Count",
                           animation_frame="Date",
                           scope="world",
                           color_continuous_scale="Viridis",
                           range_color=[0, daily_country_data['IP_Count'].max()],
                           labels={"IP_Count": "IP Count"},
                           title="Daily IP Count by Country")

daily_country_map.update_traces(
    hovertemplate="<b>%{location}</b><br>Date: %{customdata[0]}<br>IP Count: %{z}",
    customdata=daily_country_data[['Date', 'IP_Count']]
)

daily_country_map.update_layout(
    geo=dict(showframe=False, showcoastlines=True, projection_type='equirectangular'),
    height=700,
    updatemenus=[dict(
        type='buttons',
        showactive=False,
        buttons=[dict(label='Play',
                      method='animate',
                      args=[None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}]),
                 dict(label='Pause',
                      method='animate',
                      args=[[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate', 'transition': {'duration': 0}}])]
    )],
    sliders=[dict(
        active=0,
        steps=[dict(
            method='animate',
            args=[[f.name], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate'}],
            label=f.name
        ) for f in daily_country_map.frames]
    )]
)

# Add these lines after processing the data
avg_daily_ip_count = daily_counts['IP_Count'].mean()
total_daily_ip_count = daily_counts['IP_Count'].sum()

# Initialize state variables
state = {
    'total_ips': total_ips,
    'avg_daily_ip_count': avg_daily_ip_count,
    'total_daily_ip_count': total_daily_ip_count
}

def on_change(state, var_name, var_value):
    if var_name == 'countries_selected' and len(var_value) > 0:
        # Sum of IPs for selected countries
        state.total_ips = state.country_ip_data.loc[state.country_ip_data['COUNTRY'].isin(var_value), 'IP_Count'].sum()
        # Update daily statistics for selected countries
        selected_daily = state.daily_counts[state.daily_counts['COUNTRY'].isin(var_value)]
        state.avg_daily_ip_count = selected_daily['IP_Count'].mean()
        state.total_daily_ip_count = selected_daily['IP_Count'].sum()
    elif var_name == 'countries_selected':
        state.total_ips = state.country_ip_data['IP_Count'].sum()
        state.avg_daily_ip_count = state.daily_counts['IP_Count'].mean()
        state.total_daily_ip_count = state.daily_counts['IP_Count'].sum()


map_md = Markdown("pages/map/map.md")
