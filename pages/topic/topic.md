# Taipy Dashboard - **Topic**{: .color-primary} Statistics

This page provides a view of the tourists' interests, with statistics on the number of enquiries.

<br/>

<|layout|columns=1 1 1|columns[mobile]=1|
<|{selected_topic}|selector|lov={selector_topic}|on_change=on_change_topic|dropdown|label=Topic|>
|>

<br/>

<|layout|columns=2 2 2 2 |gap=25px|columns[mobile]=1|
<|card|
**Attractions**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Attractions'])}|text|class_name=h3|>
|>

<|card|
**Dining**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Dining'])}|text|class_name=h3|>
|>

<|card|
**Shopping**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Shopping'])}|text|class_name=h3|>
|>
|>

<br/>

<|layout|columns=2 1|columns[mobile]=1|
<|{data_topic_date}|chart|type=bar|x=Date|y[3]=Attractions|y[2]=Dining|y[1]=Shopping|layout={layout}|options={options}|title=Tourists'Activities|>

<|{pie_chart}|chart|type=pie|values=values|labels=labels|title=Distribution Among Activities|>
|>
 
<br/>

The data reflects the inquiries made by tourists, categorized by topics and subcategories. 
The bar chart shows the evolution of inquiries over time, while the pie chart displays the 
distribution of inquiries across topics or subcategories.
