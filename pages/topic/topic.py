import numpy as np
import pandas as pd
from taipy.gui import Markdown
from data.data import data  # Ensure this import provides the correct dataframe

selected_topic = 'All'
data_topic_date = None
pie_chart = None
bar_properties = None
selector_topic = ['All', 'Attractions', 'Dining', 'Shopping']

layout = {'barmode':'stack', "hovermode":"x"}
options = {"unselected":{"marker":{"opacity":0.5}}}

def initialize_case_evolution(data, selected_topic='All'):
    if selected_topic == 'All':
        data_topic_date = data.groupby(['Date', 'Topic'])['Inquiries'].sum().unstack(fill_value=0).reset_index()
        columns = ['Attractions', 'Dining', 'Shopping']
        chart_title = "Tourists' Activities - All Topics"
    else:
        data_filtered = data[data['Topic'] == selected_topic]
        data_topic_date = data_filtered.groupby(['Date', 'Subcategory'])['Inquiries'].sum().unstack(fill_value=0).reset_index()
        columns = data_topic_date.columns[1:].tolist() if not data_topic_date.empty else []
        chart_title = f"Tourists' Activities - {selected_topic}"

    # Check if the DataFrame is empty
    if data_topic_date.empty:
        print(f"Warning: No data available for topic '{selected_topic}'")
        return pd.DataFrame(columns=['Date']), {}, columns, {}, selected_topic, chart_title

    # Create the correct properties structure
    y_properties = {f"y[{i+1}]": col for i, col in enumerate(columns)}
    color_properties = {f"color[{i+1}]": f"rgba({(i*50)%255}, {(i*100)%255}, {(i*150)%255}, 0.7)" for i in range(len(columns))}

    bar_properties = {
        "x": "Date",
        **y_properties,
        **color_properties,
        "layout": {
            "barmode": "stack",
            "hovermode": "x",
            "title": chart_title,
            "xaxis": {"title": "Date"},
            "yaxis": {"title": "Number of Inquiries"}
        }
    }

    # Print debug information
    print(f"Selected topic: {selected_topic}")
    print(f"Columns: {columns}")
    print(f"Bar properties: {bar_properties}")
    print(f"Data shape: {data_topic_date.shape}")
    print(f"Data columns: {data_topic_date.columns}")
    print(f"Data sample:\n{data_topic_date.head()}")

    # Get the latest values for each topic
    latest_values = data_topic_date.iloc[-1].to_dict() if not data_topic_date.empty else {}
    latest_values.pop('Date', None)  # Remove the 'Date' key if it exists

    return data_topic_date, bar_properties, columns, latest_values, selected_topic, chart_title

def create_pie_chart(data, selected_topic='All'):
    if selected_topic == 'All':
        pie_data = data.groupby('Topic')['Inquiries'].sum().reset_index()
    else:
        pie_data = data[data['Topic'] == selected_topic].groupby('Subcategory')['Inquiries'].sum().reset_index()

    return pd.DataFrame({
        "labels": pie_data.iloc[:, 0],  # Topic or Subcategory
        "values": pie_data['Inquiries']
    })

def on_change_topic(state):
    print("Chosen topic: ", state.selected_topic)
    state.data_topic_date, state.bar_properties, state.columns, _, state.selected_topic, state.chart_title = initialize_case_evolution(data, state.selected_topic)
    state.pie_chart = create_pie_chart(data, state.selected_topic)
    
    # Update bar chart title
    if state.bar_properties:
        state.bar_properties["layout"]["title"] = state.chart_title
    
    # Update pie chart title
    if state.pie_chart is not None:
        state.pie_chart["title"] = f"Distribution among {state.selected_topic}"
    
    print("Updated bar_properties:", state.bar_properties)
    print("Updated pie_chart title:", state.pie_chart["title"] if state.pie_chart else "No pie chart data")
    print("Updated data_topic_date shape:", state.data_topic_date.shape)
    print("Updated data_topic_date columns:", state.data_topic_date.columns)

def on_change(state, var_name, var_value):
    if var_name == "selected_topic":
        on_change_topic(state)

topic_md = Markdown("pages/topic/topic.md")

# Initialize data
data_topic_date, bar_properties, columns, latest_values, selected_topic, chart_title = initialize_case_evolution(data)
pie_chart = create_pie_chart(data)
pie_chart["title"] = f"Distribution among {selected_topic}"
card_values = {
    "Attractions": latest_values.get("Attractions", 0),
    "Dining": latest_values.get("Dining", 0),
    "Shopping": latest_values.get("Shopping", 0)
}
num_cards = len(card_values)
