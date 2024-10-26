import osmnx as ox
import pandas as pd

def cargar_grafo(ciudad, tipo_red="drive"):
    return ox.graph_from_place(ciudad, network_type=tipo_red)

def cargar_sucursales(ruta_archivo):
    return pd.read_csv(ruta_archivo)[['latitud', 'longitud']].values

def guardar_grafo(grafo, ruta_archivo):
    ox.save_graphml(grafo, ruta_archivo)

def obtener_nodos_mas_cercanos(grafo, sucursales):
    return [ox.distance.nearest_nodes(grafo, suc[1], suc[0]) for suc in sucursales]