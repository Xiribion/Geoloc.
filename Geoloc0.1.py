##Geolocalizacion
from geopy.geocoders import Nominatim
import geopy.distance
import time
import math

##Diseño
from mpl_toolkits.basemap.test import Basemap
import matplotlib.pyplot as plt

##Crear objeto Nominatim
geo = Nominatim(user_agent = "MyApp", timeout=2)


while 1 :
    quest = input("Quieres saber donde esta una ciudad? (si/no): ")
    if quest == "si":
        lugar = input("Dime un lugar: ")
        loc = geo.geocode(lugar)
        print(loc.latitude, loc.longitude)
        plt.figure(figsize=(20,16))
        my_map = Basemap (projection = "robin", lon_0 = 0, lat_0 = 0)
        my_map.drawcoastlines()
        my_map.drawcountries()
        my_map.fillcontinents(color="white")
        my_map.drawmapboundary(fill_color="aqua")
        x,y = my_map(loc.longitude, loc.latitude)
        my_map.plot(x,y,color="r", marker="o", markersize="5")
        plt.show()
    if quest == "no":
        break








