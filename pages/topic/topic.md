# HKTB Dashboard - **Topic**{: .color-primary} Statistics

This page provides a view of the tourists' interests, with statistics on the number of enquiries.

<br/>

<|layout|columns=1 1 1|columns[mobile]=1|
<|{selected_topic}|selector|lov={selector_topic}|on_change=on_change_topic|dropdown|label=Topic|>
|>

<br/>

<|part|render={selected_topic == 'All'}|
<|layout|columns=2 2 2 2 2 1|gap=25px|columns[mobile]=1|
<|card|
**Attractions**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Attractions'] if 'Attractions' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>

<|card|
**Dining**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Dining'] if 'Dining' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>

<|card|
**Shopping**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Shopping'] if 'Shopping' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>
|>
|>

<|part|render={selected_topic == 'Attractions'}|
<|layout|columns=2 2 2 2|gap=25px|columns[mobile]=1|
<|card|
**Indoor Attractions**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Indoor Attractions'] if 'Indoor Attractions' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>

<|card|
**Outdoor Attractions**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Outdoor Attractions'] if 'Outdoor Attractions' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>

<|card|
**Seasonal/Events-Based Attractions**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Seasonal/Events-Based Attractions'] if 'Seasonal/Events-Based Attractions' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>

<|card|
**Family-Friendly Attractions**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Family-Friendly Attractions'] if 'Family-Friendly Attractions' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>
|>
|>

<|part|render={selected_topic == 'Dining'}|
<|layout|columns=2 2 2 2|gap=25px|columns[mobile]=1|
<|card|
**Local Cuisine**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Local Cuisine'] if 'Local Cuisine' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>

<|card|
**International Cuisine**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['International Cuisine'] if 'International Cuisine' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>

<|card|
**Fine Dining**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Fine Dining'] if 'Fine Dining' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>

<|card|
**Street Food**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Street Food'] if 'Street Food' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>
|>
|>

<|part|render={selected_topic == 'Shopping'}|
<|layout|columns=2 2 2 2|gap=25px|columns[mobile]=1|
<|card|
**Luxury Goods**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Luxury Goods'] if 'Luxury Goods' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>

<|card|
**Local Products**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Local Products'] if 'Local Products' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>

<|card|
**Electronics**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Electronics'] if 'Electronics' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>

<|card|
**Fashion**{: .color-primary}
<|{to_text(data_topic_date.iloc[-1]['Fashion'] if 'Fashion' in data_topic_date.columns else 0)}|text|class_name=h3|>
|>
|>
|>

<br/>

<|part|render={selected_topic == 'All'}|
<|layout|columns=2 1|columns[mobile]=1|
<|{data_topic_date}|chart|type=bar|x=Date|y[3]=Attractions|y[2]=Dining|y[1]=Shopping|layout={layout}|options={options}|title=Tourists'Activities|>

<|{pie_chart}|chart|type=pie|values=values|labels=labels|title=Distribution Among Activities|>
|>
|>

<|part|render={selected_topic == 'Attractions'}|
<|layout|columns=2 1|columns[mobile]=1|
<|{data_topic_date}|chart|type=bar|x=Date|y[4]=Indoor Attractions|y[3]=Outdoor Attractions|y[2]=Seasonal/Events-Based Attractions|y[1]=Family-Friendly Attractions|options={options}|title=Inquiries Over Time for Attractions|>

<|{pie_chart}|chart|type=pie|values=values|labels=labels|title=Distribution of Subcategories for {selected_topic}|>
|>
|>

<|part|render={selected_topic == 'Dining'}|
<|layout|columns=2 1|columns[mobile]=1|
<|{data_topic_date}|chart|type=bar|x=Date|y[4]=Local Cuisine|y[3]=International Cuisine|y[2]=Fine Dining|y[1]=Street Food|options={options}|title=Inquiries Over Time for Dining|>

<|{pie_chart}|chart|type=pie|values=values|labels=labels|title=Distribution of Subcategories for {selected_topic}|>
|>
|>

<|part|render={selected_topic == 'Shopping'}|
<|layout|columns=2 1|columns[mobile]=1|
<|{data_topic_date}|chart|type=bar|x=Date|y[4]=Luxury Goods|y[3]=Local Products|y[2]=Electronics|y[1]=Fashion|options={options}|title=Inquiries Over Time for Shopping|>

<|{pie_chart}|chart|type=pie|values=values|labels=labels|title=Distribution of Subcategories for {selected_topic}|>
|>
|>
 
<br/>

The data reflects the inquiries made by tourists, categorized by topics and subcategories. 
The bar chart shows the evolution of inquiries over time, while the pie chart displays the 
distribution of inquiries across topics or subcategories.
