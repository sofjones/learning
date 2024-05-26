import folium
import pandas as pd
import webbrowser
import base

df = pd.DataFrame({'Lat': [39.74], 'Long': [-104.98]})

m = folium.Map(location=[df.Lat[0], df.Long[0]])


folium.Marker(
    location=[39.04,-77.49]
).add_to(m)

m.save("map.html")
webbrowser.open("map.html")

trace = base.Command("tracert -d ",[],"tryhackme.com")
trace.run_command()