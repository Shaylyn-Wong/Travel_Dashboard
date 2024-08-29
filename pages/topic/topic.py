import numpy as np
import pandas as pd
from taipy.gui import Markdown
from data.data import data

selected_topic = 'All'
data_topic_date = None
pie_chart = None

layout = {'barmode':'stack', "hovermode":"x"}
options = {"unselected":{"marker":{"opacity":0.5}}}

def initialize_case_evolution(data, selected_topic='All'):
    # Define y_mapping to determine required columns and y-values for the chart
    y_mapping = {
        'All': ['Attractions', 'Dining', 'Shopping'],
        'Attractions': ['Indoor', 'Outdoor', 'Seasonal/Events-Based', 'Family-Friendly'],
        'Dining': ['Local Cuisine', 'International Cuisine', 'Fine Dining', 'Street Food'],
        'Shopping': ['Luxury Goods', 'Local Products', 'Electronics', 'Fashion']
    }
    
    # Determine the y-values to use based on the selected topic
    y_values = y_mapping.get(selected_topic, y_mapping['All'])

    if selected_topic == 'All':
        # Group by Date and Topic, sum the Inquiries
        data_topic_date = data.groupby(['Date', 'Topic'])['Inquiries'].sum().unstack(fill_value=0).reset_index()
        # Ensure all main topics are present
        for topic in y_mapping['All']:
            if topic not in data_topic_date.columns:
                data_topic_date[topic] = 0
    else:
        # Filter for selected topic, then group by Date and Subcategory
        data_filtered = data[data['Topic'] == selected_topic]
        data_topic_date = data_filtered.groupby(['Date', 'Subcategory'])['Inquiries'].sum().unstack(fill_value=0).reset_index()
        
        # Ensure all required columns are present for the selected topic
        for col in y_values:
            if col not in data_topic_date.columns:
                data_topic_date[col] = 0
    
    # Ensure the DataFrame is not empty
    if data_topic_date.empty:
        data_topic_date = pd.DataFrame(columns=['Date'] + y_values)
        data_topic_date['Date'] = pd.to_datetime('today')
        data_topic_date = data_topic_date.fillna(0)
    
    return data_topic_date, y_values

def generate_chart_config(data_topic_date, y_values, layout, options):
    y_config = "|".join([f"y[{i+1}]={y_value}" for i, y_value in enumerate(y_values[::-1])])
    chart_config = f"<|{data_topic_date}|chart|type=bar|x=Date|{y_config}|layout={layout}|options={options}|title=Tourists' Activities|>"
    return chart_config

def create_pie_chart(data, selected_topic='All'):
    if selected_topic == 'All':
        pie_data = data.groupby('Topic')['Inquiries'].sum().reset_index()
    else:
        pie_data = data[data['Topic'] == selected_topic].groupby('Subcategory')['Inquiries'].sum().reset_index()

    return pd.DataFrame({
        "labels": pie_data.iloc[:, 0],  # Topic or Subcategory
        "values": pie_data['Inquiries']
    })

# Initialize data
data_topic_date, y_values = initialize_case_evolution(data, selected_topic)
chart_config = generate_chart_config(data_topic_date, y_values, layout, options)
pie_chart = create_pie_chart(data)

# Define selector_topic here
selector_topic = ['All'] + list(np.sort(data['Topic'].astype(str).unique()))

def on_change_topic(state):
    print("Chosen topic: ", state.selected_topic)
    state.data_topic_date = initialize_case_evolution(data, state.selected_topic)
    state.pie_chart = create_pie_chart(data, state.selected_topic)

topic_md = Markdown("pages/topic/topic.md")
