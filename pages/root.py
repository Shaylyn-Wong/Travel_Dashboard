from taipy.gui import Markdown 

import numpy as np

from data.data import data

selector_topic = ['All'] + list(np.sort(data['Topic'].astype(str).unique()))
selected_topic = 'Attractions'

def to_text(val):
    try:
        return '{:,}'.format(int(val)).replace(',', ' ')
    except:
        print("Error trying to format value: ", val)
        if val:
            return val
        else:
            return 'No information'
        
def on_menu(state, action, info):
        page = info["args"][0]
        state.navigate(page)

root = Markdown("pages/root.md")