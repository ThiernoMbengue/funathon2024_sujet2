# Localisatios des aéroport


import pandas as pd
import geopandas as gpd
from src.create_data_list import create_data_list

urls = create_data_list("funathon2024_sujet2/sources.yml")
airports_location = gpd.read_file(urls['geojson']['airport'])

# Vérifier le système de coordonnées
print(airports_location.crs)

# En Python
import folium 

m = folium.Map()

folium.GeoJson(airports_location).add_to(m)
m.save('map.html')
m

