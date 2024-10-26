import osmnx as ox
import matplotlib.pyplot as plt

def visualizar_mejor_ruta(grafo, mejor_ruta):
    fig, ax = ox.plot_graph_route(grafo, mejor_ruta, route_linewidth=2, node_size=30, bgcolor='white')
    plt.show()
