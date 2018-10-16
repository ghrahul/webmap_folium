import folium
#Mokshcommit
import pandas
import numpy
def color(elev):
    if elev<1000:
        return "green"
    elif elev>1000 and elev<3000:
        return "orange"
    elif elev>3000:
        return "red"
        
        
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
map = folium.Map()
fgv = folium.FeatureGroup(name = "volcanos")
for lt, ln, el in zip(lat,lon,elev):
    fgv.add_child(folium.Marker(location = [lt,ln], popup=str(el) + " m",icon=folium.Icon(color=color(el))))
fgp = folium.FeatureGroup(name = "population")
fgp.add_child(folium.GeoJson(data=open("world.json",'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor': 'yellow'
if x['properties']['POP2005']<10000000 else 'orange' if 10000000<= x['properties']['POP2005']<20000000 else 'red' } ))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("mylocation.html")
