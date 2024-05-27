import folium
import pandas as pd
import webbrowser

def map_locations(lat, long):
    colors = ["green", "blue", "purple", "red", "pink", "cadetblue"]
    df = pd.DataFrame({'Lat': lat, 'Long': long})
    m = folium.Map(location=[df.Lat[0], df.Long[0]], zoom_start=4)
    print('Mapping the ' + str(len(lat)) + ' hops to your destination url')
    for i in range(len(lat)):
        folium.Marker(
            location=[lat[i],long[i]],
            popup=i,
            icon=folium.Icon(color=colors[i % len(colors)-1], icon='star')
        ).add_to(m)
    m.save("map.html")
    webbrowser.open("map.html")

# trace = base.Command("tracert -d ",[],"tryhackme.com")
# trace.run_command()