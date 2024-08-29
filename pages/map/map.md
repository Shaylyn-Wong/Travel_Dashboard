# Taipy Dashboard - **Map**{: .color-primary} Statistics

<|layout|columns=1 1|columns[mobile]=1|
<|
### Total IP Addresses by Country
##### Total Unique IPs: <|{to_text(total_ips)}|text|raw|>
<|chart|figure={ip_map}|height=700px|selected={countries_selected}|>

This map shows the total distribution of IP addresses by country using a logarithmic scale. This helps to visualize the differences between countries with very high and very low numbers of IP addresses.
|>

<|
### Daily IP Addresses by Country
<|chart|figure={daily_ip_map}|height=700px|>

This map shows the daily count of IP addresses by country. Use the play button to see how the distribution changes over time. The color intensity represents the number of IP addresses for each country on a given day.
|>
|>
