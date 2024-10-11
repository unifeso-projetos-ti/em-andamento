import folium
from folium.plugins import HeatMap
import mysql.connector
from conexao import conn

# Obtém a conexão ao banco de dados
connection = conn()

try:
    if connection:
        cursor = connection.cursor(dictionary=True)

        # Consulta para obter as coordenadas de latitude e longitude
        cursor.execute("SELECT LATITUDE, LONGITUDE FROM LOCALIZACAO WHERE LATITUDE IS NOT NULL AND LONGITUDE IS NOT NULL LIMIT 10000")
        location_data = cursor.fetchall()

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

# Extraindo latitudes e longitudes
locations = [(float(row['LATITUDE']), float(row['LONGITUDE'])) for row in location_data]

# Criando o mapa centrado na média das coordenadas
if locations:
    average_lat = sum(lat for lat, lon in locations) / len(locations)
    average_lon = sum(lon for lat, lon in locations) / len(locations)
    map_center = [average_lat, average_lon]
else:
    # Caso não haja dados, usar coordenadas padrão
    map_center = [0, 0]

# Criando o mapa com o folium
mymap = folium.Map(location=map_center, zoom_start=10)

# Adicionando o mapa de calor ao mapa
HeatMap(locations).add_to(mymap)

# Salvando o mapa em um arquivo HTML
mymap.save('mapa_calor.html')

# Exibindo o mapa no Jupyter Notebook ou em uma página HTML
mymap
