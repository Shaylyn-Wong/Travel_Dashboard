import numpy as np
import pandas as pd
from taipy.gui import Markdown
from data.data import data  # Ensure this import provides the correct dataframe

selected_topic = 'All'
data_topic_date = None
pie_chart = None
bar_properties = None

layout = {'barmode':'stack', "hovermode":"x"}
options = {"unselected":{"marker":{"opacity":0.5}}}

def initialize_case_evolution(data, selected_topic='All'):
    if selected_topic == 'All':
        # Group by Date and Topic, sum the Inquiries
        data_topic_date = data.groupby(['Date', 'Topic'])['Inquiries'].sum().unstack(fill_value=0).reset_index()
        columns = ['Attractions', 'Dining', 'Shopping']
    else:
        # Filter for selected topic, then group by Date and Subcategory
        data_filtered = data[data['Topic'] == selected_topic]
        data_topic_date = data_filtered.groupby(['Date', 'Subcategory'])['Inquiries'].sum().unstack(fill_value=0).reset_index()
        columns = data_topic_date.columns[1:].tolist()  # Exclude 'Date' column

    # Create bar_properties
    bar_properties = {
        "x": "Date",
        "layout": {
            "barmode": "stack",
            "hovermode": "x",
            "title": f"Tourists' Activities - {selected_topic}",
            "xaxis": {"title": "Date"},
            "yaxis": {"title": "Number of Inquiries"}
        }
    }

    # Ensure y values are correctly assigned for each column
    for i, col in enumerate(columns, start=1):
        bar_properties[f"y[{i}]"] = col

    # Print for debugging
    print(f"Selected topic: {selected_topic}")
    print(f"Columns: {columns}")
    print(f"Bar properties: {bar_properties}")

    return data_topic_date, bar_properties

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
data_topic_date, bar_properties = initialize_case_evolution(data)
pie_chart = create_pie_chart(data)

def on_change_topic(state):
    print("Chosen topic: ", state.selected_topic)
    state.data_topic_date, state.bar_properties = initialize_case_evolution(data, state.selected_topic)
    state.pie_chart = create_pie_chart(data, state.selected_topic)
    print("Updated bar_properties:", state.bar_properties)

topic_md = Markdown("pages/topic/topic.md")
