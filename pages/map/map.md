# Taipy Dashboard - **Map**{: .color-primary} Statistics

You can interact with the two maps below to get information on IP addresses and daily country counts.

<|layout|columns=1 1|columns[mobile]=1|
<|
### Total IP Addresses by Country
##### Total Unique IPs: <|{to_text(total_ips)}|text|raw|>
<|chart|figure={ip_map}|height=700px|selected={countries_selected}|>

This map shows the total distribution of IP addresses by country. The color intensity represents the number of IP addresses for each country.
|>

<|
### Daily IP Count by Country
##### Average Daily IP Count: <|{int(avg_daily_ip_count)}|text|raw|> | Total Daily IP Count: <|{to_text(total_daily_ip_count)}|text|raw|>
<|chart|figure={daily_country_map}|height=700px|>

This map shows the daily count of IP addresses for each country. The color intensity represents the number of IP addresses for each country on a given day. Use the animation controls to see how the distribution changes over time.
|>
|>

