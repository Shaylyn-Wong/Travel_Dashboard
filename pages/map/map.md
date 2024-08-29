# Taipy Dashboard - **Map**{: .color-primary} Statistics

<|layout|columns=1 1|columns[mobile]=1|
<|
### Total IP Addresses by Country
##### Total Unique IPs: <|{to_text(total_ips)}|text|raw|>
<|chart|figure={ip_map}|height=700px|selected={countries_selected}|>

This map shows the total distribution of IP addresses by country using a logarithmic scale. This helps to visualize the differences between countries with very high and very low numbers of IP addresses.
|>

<|
### Daily Unique Country Count
<|chart|figure={daily_country_chart}|height=700px|>

This chart shows the daily count of unique countries. The line represents how the number of unique countries changes over time.
|>
|>
