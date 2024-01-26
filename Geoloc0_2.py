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
    quest = input("Quieres seguir? (si/no): ")
    if quest == "si":
        #Se pregunta la latitud y la longitud y se localiza el lugar
        latitud = input("Latitud:")
        longitud = input("Longitud:")
        sit = (latitud,longitud)
        print(latitud,longitud)
        loc = geo.geocode(sit)
        print(loc)

        #Se localiza el lugar en el mapa
        plt.figure(figsize=(20,16))
        my_map = Basemap (projection = "robin", lon_0 = 0, lat_0 = 0)
        my_map.drawcoastlines()
        my_map.drawcountries()
        my_map.fillcontinents(color="white")
        my_map.drawmapboundary(fill_color="aqua")
        x,y = my_map(longitud,latitud)
        my_map.plot(x,y,color="r", marker="o", markersize="5")
        plt.show()

    if quest == "no":
        break
