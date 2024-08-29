
import numpy as np
import pandas as pd
from taipy.gui import Markdown
import plotly.express as px
import plotly.graph_objects as go

from data.data import data, geojson, origin

# Process origin data
def process_origin_data(origin):
    # Total counts per country
    country_ip_counts = origin.groupby('country').size().reset_index(name='IP_Count')
    country_ip_counts.columns = ['COUNTRY', 'IP_Count']
    country_ip_counts['IP_Count_Log'] = np.log10(country_ip_counts['IP_Count'] + 1)  # Add 1 to avoid log(0)
    
    # Counts of unique countries per day
    origin['date'] = pd.to_datetime(origin['date'])
    daily_counts = origin.groupby('date')['country'].nunique().reset_index(name='Country_Count')
    daily_counts.columns = ['Date', 'Country_Count']
    
    return country_ip_counts, daily_counts

country_ip_data, daily_country_data = process_origin_data(origin)
total_ips = country_ip_data['IP_Count'].sum()
countries_selected = []

# Create total IP count map
ip_map = px.choropleth_mapbox(country_ip_data,
                           geojson=geojson,
                           featureidkey="id",
                           locations="COUNTRY",
                           color="IP_Count_Log",
                           hover_name="COUNTRY",
                           hover_data={"IP_Count": True, "IP_Count_Log": False},
                           zoom=1,
                           center={"lat": 0, "lon": 0},
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           labels={"IP_Count": "Total IP Count", "IP_Count_Log": "Log(Total IP Count)"},
                           title="Total IP Count by Country (Log Scale)")

ip_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                     coloraxis_colorbar=dict(title="Log(Total IPs)"))

# Create daily country count chart
daily_country_chart = px.line(daily_country_data, x='Date', y='Country_Count',
                              title='Daily Unique Country Count',
                              labels={'Country_Count': 'Unique Countries', 'Date': 'Date'},
                              line_shape='linear')

daily_country_chart.update_layout(
    xaxis_title='Date',
    yaxis_title='Number of Unique Countries',
    height=700,
    hovermode='x unified'
)

daily_country_chart.update_traces(mode='lines+markers')

def on_change(state, var_name, var_value):
    if var_name == 'countries_selected' and len(var_value)>0:
        # Sum of IPs for selected countries
        state.total_ips = state.country_ip_data.loc[state.country_ip_data['COUNTRY'].isin(var_value), 'IP_Count'].sum()
    elif var_name == 'countries_selected':
        state.total_ips = state.country_ip_data['IP_Count'].sum()

map_md = Markdown("pages/map/map.md")
