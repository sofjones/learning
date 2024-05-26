import folium
import pandas as pd
import webbrowser

def map_locations(lat, long):
    df = pd.DataFrame({'Lat': lat, 'Long': long})
    m = folium.Map(location=[df.Lat[0], df.Long[0]])
    for i in range(len(lat)):
        folium.Marker(
            location=[lat[i],long[i]]
        ).add_to(m)
    m.save("map.html")
    webbrowser.open("map.html")

# trace = base.Command("tracert -d ",[],"tryhackme.com")
# trace.run_command()