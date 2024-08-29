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
    # Define required columns for each topic
    required_columns = {
        'Attractions': ['Indoor Attractions', 'Outdoor Attractions', 
                        'Seasonal/Events-Based Attractions', 'Family-Friendly Attractions'],
        'Dining': ['Local Cuisine', 'International Cuisine', 'Fine Dining', 'Street Food'],
        'Shopping': ['Luxury Goods', 'Local Products', 'Electronics', 'Fashion']
    }
    
    if selected_topic == 'All':
        # Group by Date and Topic, sum the Inquiries
        data_topic_date = data.groupby(['Date', 'Topic'])['Inquiries'].sum().unstack(fill_value=0).reset_index()
        # Ensure all main topics are present
        for topic in ['Attractions', 'Dining', 'Shopping']:
            if topic not in data_topic_date.columns:
                data_topic_date[topic] = 0
    else:
        # Filter for selected topic, then group by Date and Subcategory
        data_filtered = data[data['Topic'] == selected_topic]
        data_topic_date = data_filtered.groupby(['Date', 'Subcategory'])['Inquiries'].sum().unstack(fill_value=0).reset_index()
        
        # Ensure all required columns are present for the selected topic
        if selected_topic in required_columns:
            for col in required_columns[selected_topic]:
                if col not in data_topic_date.columns:
                    data_topic_date[col] = 0
    
    # Ensure the DataFrame is not empty
    if data_topic_date.empty:
        data_topic_date = pd.DataFrame(columns=['Date'] + list(required_columns.keys()))
        data_topic_date['Date'] = pd.to_datetime('today')
        data_topic_date = data_topic_date.fillna(0)
    
    return data_topic_date

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
data_topic_date = initialize_case_evolution(data)
pie_chart = create_pie_chart(data)

# Define selector_topic here
selector_topic = ['All'] + list(np.sort(data['Topic'].astype(str).unique()))

def on_change_topic(state):
    print("Chosen topic: ", state.selected_topic)
    state.data_topic_date = initialize_case_evolution(data, state.selected_topic)
    state.pie_chart = create_pie_chart(data, state.selected_topic)

topic_md = Markdown("pages/topic/topic.md")
