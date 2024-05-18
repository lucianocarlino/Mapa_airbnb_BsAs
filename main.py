import folium
from ObtenerInformacion import ObtenerInformarcion

lista = ObtenerInformarcion()

map = folium.Map(location=(-34.583484918773294, -58.41637042427801), zoom_start=12)

for i in range(len(lista)):
    folium.Marker(location=(float(lista[i][2][0]), float(lista[i][2][1])), tooltip=f"{lista[i][1]}", popup=f"{lista[i][0]}").add_to(map)

map.show_in_browser()