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


if __name__ == '__main__':
    gui_multi_pages = Gui(pages=pages)

    tp.Core().run()
    
    gui_multi_pages.run(title="Taipy Dashboard")
