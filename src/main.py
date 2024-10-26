from utils import cargar_grafo, cargar_sucursales, guardar_grafo, obtener_nodos_mas_cercanos
from route_optimization import algoritmo_genetico
from visualization import visualizar_mejor_ruta
import osmnx as ox

def main():
    ciudad = "Cochabamba, Bolivia"
    grafo = cargar_grafo(ciudad)

    aduana = (-17.390678145175766, -66.25262790979859)  # Coordenadas de la aduana
    sucursales = cargar_sucursales("data/sucursales.csv")
    nodos_sucursales = obtener_nodos_mas_cercanos(grafo, sucursales)
    nodo_aduana = ox.distance.nearest_nodes(grafo, aduana[1], aduana[0])

    mejor_ruta = algoritmo_genetico(grafo, nodo_aduana, nodos_sucursales)
    visualizar_mejor_ruta(grafo, mejor_ruta)

if __name__ == "__main__":
    main()
