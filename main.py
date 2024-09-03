from taipy.gui import Gui, navigate

import taipy as tp

from pages.topic.topic import topic_md
from pages.performance.performance import performance_md
from pages.map.map import map_md
#from pages.predictions.predictions import predictions_md, selected_scenario
from pages.root import root, selected_topic, selector_topic, to_text

from config.config import Config


pages = {
    '/':root,
    "Performance": performance_md,
    "Topic":topic_md,
    "Map":map_md,
    #"Predictions":predictions_md
}
page_names = [page for page in pages.keys() if page != "/"]

def menu_action(state, action, payload):
    page = payload["args"][0]
    navigate(state, page)


def initialize_state(state):
    state.selected_topic, state.columns, state.bar_properties, state.data_topic_date, state.latest_values = initialize_case_evolution(data, selected_topic)
    state.pie_chart = create_pie_chart(data, selected_topic)
    gui_multi_pages = Gui(pages=pages)

    tp.Core().run()
    
    # Initialize the state
    initialize_state(gui_multi_pages.state)
    
    gui_multi_pages.run(title="Taipy Dashboard")
