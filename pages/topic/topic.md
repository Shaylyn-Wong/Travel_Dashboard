# Taipy Dashboard - **Topic**{: .color-primary} Statistics

This page provides a view of the tourists' interests, with statistics on the number of enquiries.

<br/>

<|layout|columns=1 1 1|columns[mobile]=1|
<|{selected_topic}|selector|lov={selector_topic}|on_change=on_change_topic|dropdown|label=Topic|>
|>

<br/>

<|layout|columns=3 3 3|gap=25px|columns[mobile]=1|
<|card|
**Attractions**{: .color-primary}
<|{card_values["Attractions"]}|text|class_name=h3|>
|>

<|card|
**Dining**{: .color-primary}
<|{card_values["Dining"]}|text|class_name=h3|>
|>

<|card|
**Shopping**{: .color-primary}
<|{card_values["Shopping"]}|text|class_name=h3|>
|>
|>

<br/>

<|layout|columns=2 1|columns[mobile]=1|
<|{data_topic_date}|chart|type=bar|properties={bar_properties}|rebuild|>

<|{pie_chart}|chart|type=pie|values=values|labels=labels|>
|>
 
<br/>

The data reflects the inquiries made by tourists, categorized by topics and subcategories. 
The bar chart shows the evolution of inquiries over time, while the pie chart displays the 
distribution of inquiries across topics or subcategories.
