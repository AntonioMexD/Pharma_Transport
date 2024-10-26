# src/main.py
import osmnx as ox
from utils import cargar_sucursales, cargar_medicamentos, cargar_factores, obtener_nodos_mas_cercanos
from genetic_algorithm import algoritmo_genetico
from visualization import plot_route

def main():
    ciudad = "Cochabamba, Bolivia"
    grafo = ox.graph_from_place(ciudad, network_type="drive")

    # Imprimir el número de nodos y bordes en el grafo
    print(f"Número de nodos en el grafo: {len(grafo.nodes)}")
    print(f"Número de bordes en el grafo: {len(grafo.edges)}")

    nodos_sucursales = cargar_sucursales('data/sucursales.csv', grafo)
    ubicaciones = [(suc['latitud'], suc['longitud']) for suc in nodos_sucursales]
    nodos_sucursales = obtener_nodos_mas_cercanos(grafo, ubicaciones)

    nodo_aduana = ox.distance.nearest_nodes(grafo, -17.390678145175766, -66.25262790979859)
    
    medicamentos = cargar_medicamentos('data/medicamentos.csv')
    factores_externos = cargar_factores('data/factores_externos.csv')

    mejor_ruta = algoritmo_genetico(grafo, nodo_aduana, nodos_sucursales, medicamentos, factores_externos)

    # Imprime mejor_ruta para depuración
    print("Mejor ruta generada:", mejor_ruta)

    # Verifica si todos los nodos de mejor_ruta están en el grafo
    nodos_validos = all(nodo in grafo.nodes for nodo in mejor_ruta)
    rutas_validas = all(grafo.has_edge(mejor_ruta[i], mejor_ruta[i + 1]) for i in range(len(mejor_ruta) - 1))

    if nodos_validos and rutas_validas:
        plot_route(grafo, mejor_ruta)
    else:
        print("Algunos nodos en la mejor ruta no están en el grafo o no están conectados.")

if __name__ == "__main__":
    main()
