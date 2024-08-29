
import numpy as np
from taipy.gui import Markdown
import plotly.express as px

from data.data import data, geojson, origin


def initialize_map(data):
    data['Province/State'] = data['Province/State'].fillna(data["Country/Region"])
    data_province = data.groupby(["Country/Region",
                                  'Province/State',
                                  'Longitude',
                                  'Latitude'])\
                         .max()
                         

    data_province_displayed = data_province[data_province['Deaths']>10].reset_index()

    # Size when using Taipy charts
    # data_province_displayed['Size'] = np.sqrt(data_province_displayed.loc[:,'Deaths']/data_province_displayed.loc[:,'Deaths'].max())*80 + 3
    # data_province_displayed['Text'] = data_province_displayed.loc[:,'Deaths'].astype(str) + ' deaths </br> ' + data_province_displayed.loc[:,'Province/State']

    # Size when using Plotly Python
    data_province_displayed['Size'] = ((data_province_displayed.loc[:,'Deaths']/data_province_displayed.loc[:,'Deaths'].max()) * 100) + 0.1
    return data_province_displayed


data_province_displayed = initialize_map(data)

sum_deaths = data_province_displayed['Deaths'].sum()
cluster_selected = [] 
# Creating a Plotly scatter mapbox plot
cluster_map = px.scatter_mapbox(data_province_displayed,
                        lat="Latitude",
                        lon="Longitude",
                        size="Size",
                        color="Deaths",
                        color_continuous_scale="solar",
                        size_max=60,
                        hover_name="Province/State",
                        hover_data={"Deaths": True, "Latitude": False, "Longitude": False, "Size": False},
                        mapbox_style="open-street-map",
                        zoom=3,
                        center={"lat": 38, "lon": -90})

# Update layout with specific options
cluster_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                  dragmode="zoom")


def process_origin_data(origin):
    # Group by country and count unique IPs
    country_ip_counts = origin.groupby('country')['ip'].nunique().reset_index()
    country_ip_counts.columns = ['COUNTRY', 'IP_Count']
    return country_ip_counts

country_ip_data = process_origin_data(origin)
total_ips = country_ip_data['IP_Count'].sum()
countries_selected = []

ip_map = px.choropleth_mapbox(country_ip_data,
                           geojson=geojson,
                           featureidkey="id",
                           locations="COUNTRY",  # Assuming 'COUNTRY' matches the geojson ids
                           color="IP_Count",
                           hover_name="COUNTRY",
                           hover_data={"IP_Count": True},
                           zoom=1,
                           center={"lat": 0, "lon": 0},
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           labels={"IP_Count": "Number of IPs"},
                           title="Number of IP Addresses by Country")

ip_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


def on_change(state, var_name, var_value):
    if var_name == 'countries_selected' and len(var_value)>0:
        # Sum of IPs for selected countries
        state.total_ips = state.country_ip_data.loc[state.country_ip_data['COUNTRY'].isin(var_value), 'IP_Count'].sum()
    elif var_name == 'countries_selected':
        state.total_ips = state.country_ip_data['IP_Count'].sum()
    
    if var_name == 'cluster_selected' and len(var_value)>0:
        # Sum of deaths (keeping this part as it was)
        state.sum_deaths = state.data_province_displayed.loc[var_value, 'Deaths'].sum()
    elif var_name == 'cluster_selected':    
        state.sum_deaths = data_province_displayed['Deaths'].sum()
        

map_md = Markdown("pages/map/map.md")


"""
# For Taipy charts
marker_map = {"color":"Deaths", "size": "Size", "showscale":True, "colorscale":"Viridis"}
layout_map = {
            "dragmode": "zoom",
            "mapbox": { "style": "open-street-map", "center": { "lat": 38, "lon": -90 }, "zoom": 3}
            }
options = {"unselected":{"marker":{"opacity":0.5}}}
"""
