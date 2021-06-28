import folium
import pandas as pd

web_map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles="Stamen Terrain")

fg_volcanoes = folium.FeatureGroup(name="Volcanoes")

data = pd.read_csv("volcano.csv")
data = data.dropna(subset=["hazard"])

for lt, ln, name, hazard, country, region, subregion in zip(data.Latitude, data.Longitude, data.V_Name, data.hazard,
                                                            data.Country, data.Region, data.Subregion):
    if hazard >= 3:
        color = "red"
    elif hazard == 2 :
        color = "orange"
    else:
        color = "green"
    fg_volcanoes.add_child(folium.CircleMarker(location=[lt, ln],
                                               radius=10,
                                               color="grey",
                                               fill=True,
                                               fill_color=color,
                                               fill_opacity=0.7,
                                               popup=f"{name}, {hazard}, {country}, {region}, {subregion}",
                                               ))

web_map.add_child(fg_volcanoes)


web_map.save('volcanoes_map.html')
