# Covid Dashboard - **Map**{: .color-primary} Statistics

You can select clusters and countries in the two maps below. These will give you information on these clusters and countries. 

<|layout|columns=1 1|columns[mobile]=1|
<|
### Covid Clusters
##### Total Deaths: <|{to_text(sum_deaths)}|text|raw|>
<|chart|figure={cluster_map}|height=700px|selected={cluster_selected}|>
|>

<|
### IP Addresses by Country
##### Total IPs: <|{to_text(total_ips)}|text|raw|>
<|chart|figure={ip_map}|height=700px|selected={countries_selected}|>
|>
|>


[//]: <> (This is a Markdown comment, here is how you can create the same map with Taipy:)
[//]: <> (<|{data_province_displayed}|chart|type=scattermapbox|lat=Latitude|lon=Longitude|marker={marker_map}|layout={layout_map}|text=Text|mode=markers|height=800px|options={options}|>)
