##Geolocalizacion
from geopy.geocoders import Nominatim
import geopy.distance
import time
import math

##Diseño
from mpl_toolkits.basemap.test import Basemap
import matplotlib.pyplot as plt


###Crear el diseño del mapa y poner el sitio correspondiente en el mapa

##----------------------------------------------------------------------------------
##Crear objeto Nominatim
#geo = Nominatim(user_agent = "MyApp", timeout=2)
#lugar = geo.geocode("Madrid")
#plt.figure(figsize=(20,16))
#my_map = Basemap (projection = "robin", lon_0 = 0, lat_0 = 0)
#my_map.drawcoastlines()
#my_map.drawcountries()
#my_map.fillcontinents(color="white")
#x,y = my_map(lugar.longitude, lugar.latitude)
#my_map.plot(x,y,color="r", marker="o", markersize="5")
#plt.show()


##------------------------------------------------------

###Crear el diseño del mapa, hacer una lista y ponerlo en el mapa

#geo = Nominatim(user_agent = "MyApp", timeout=2)
#lugar_list = ["Guadalupe","Milan", "Pekin"]
#plt.figure(figsize=(20,16))
#my_map = Basemap (projection = "robin", lon_0 = 0, lat_0 = 0)
#my_map.drawcoastlines()
#my_map.drawcountries()
#my_map.fillcontinents(color="white")
#my_map.drawmapboundary(fill_color="aqua")

##Recorrer la lista de ciudades
#for i in lugar_list:
#    address = geo.geocode(i)
#    time.sleep(0.5)
#    x,y = my_map(address.longitude, address.latitude)
#    my_map.plot(x,y,color="r", marker="o", markersize="9")

#plt.show()


##--------------------------------------------------------

##Crear objeto Nominatim
#geo = Nominatim(user_agent = "MyApp", timeout=2)

##Imprimo el lugar o calle al que quiero ir
#lugar = input("Dime un lugar: ")
#loc = geo.geocode(lugar)
#print(loc)

##Imprime la longitud y la latitud
#print(loc.latitude, loc.longitude)

##Localizar Varias Ciudades
#lugar_list = ["Sevilla","Nueva York", "Paris"]

##Recorrer la lista para solicitar su localizacion
#for i in lugar_list:
#    address = geo.geocode(i,timeout=3)
#   print("ciudad = " + i + " " + str(address.latitude) + " " + str(address.longitude))
#    time.sleep(1)

##Distacia entre ciudades
#lugar_in = input("Dime lugar de inicio: ")
#inicio = geo.geocode(lugar_in)

#lugar_fin = input("Dime lugar de llegada: ")
#final = geo.geocode(lugar_fin)

##Coordenadas
#coord_in = (inicio.latitude, inicio.longitude)
#coord_fin = (final.latitude, final.longitude)

##Calculo de la distacia
#distancia = geopy.distance.distance(coord_in,coord_fin)
#print("La distancia es: " + str(distancia))


#Hacer una funcion para saber la distancia en cualquier punto
#def distancia(origen,destino):
    #lugar_origen = geo.geocode(origen)
    #lugar_destino = geo.geocode(destino)
    ##coord_origen = (lugar_origen.latitude, lugar_origen.longitude)
    ##coord_destino = (lugar_destino.latitude, lugar_destino.longitude)
    #dist = geopy.distance.distance((lugar_origen.latitude, lugar_origen.longitude),(lugar_destino.latitude, lugar_destino.longitude))
    #print("La distancia entre " + origen + " y "+ destino + " es = " + str(dist))

    #return

#a = input("Dime el lugar de origen = ")
#b = input("Dime el lugar de destino = ")
#distancia(a,b)

