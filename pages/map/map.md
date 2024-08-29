# Taipy Dashboard - **Map**{: .color-primary} Statistics

<|layout|columns=1 1|columns[mobile]=1|
<|
### IP Clusters
##### Total Deaths: <|{to_text(sum_deaths)}|text|raw|>
<|chart|figure={cluster_map}|height=700px|selected={cluster_selected}|>
|>

<|
### IP Addresses by Country (Log Scale)
##### Total Unique IPs: <|{to_text(total_ips)}|text|raw|>
<|chart|figure={ip_map}|height=700px|selected={countries_selected}|>

The map above shows the distribution of IP addresses by country using a logarithmic scale. This helps to visualize the differences between countries with very high and very low numbers of IP addresses.
|>
|>


[//]: <> (This is a Markdown comment, here is how you can create the same map with Taipy:)
[//]: <> (<|{data_province_displayed}|chart|type=scattermapbox|lat=Latitude|lon=Longitude|marker={marker_map}|layout={layout_map}|text=Text|mode=markers|height=800px|options={options}|>)
