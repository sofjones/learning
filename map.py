import folium
import pandas as pd
import webbrowser

def map_locations(lat, long):
    colors = ["green", "blue", "purple", "lightblue", "pink", "cadetblue"]
    df = pd.DataFrame({'Lat': lat, 'Long': long})
    m = folium.Map(location=[df.Lat[0], df.Long[0]], zoom_start=6)
    print('Mapping the ' + str(len(lat)) + ' hops to your destination url')
    for i in range(len(lat)-1):
        folium.Marker(
            location=[lat[i],long[i]],
            popup=i+1,
            icon=folium.Icon(color=colors[i % len(colors)-1], prefix='fa', icon='bolt')
        ).add_to(m)
    folium.Marker(
        location=[lat[-1], long[-1]],
        popup = len(lat),
        icon = folium.Icon(color='red', prefix='fa', icon='flag')
    ).add_to(m)
    m.save("map.html")
    webbrowser.open("map.html")

# trace = base.Command("tracert -d ",[],"tryhackme.com")
# trace.run_command()