import random
import networkx as nx

def generar_ruta_aleatoria(aduana, sucursales):
    ruta = [aduana]
    random.shuffle(sucursales)
    ruta += sucursales
    return ruta

def evaluar_ruta(ruta, grafo):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        try:
            distancia = nx.shortest_path_length(grafo, ruta[i], ruta[i + 1], weight="length")
            distancia_total += distancia
        except:
            distancia_total += float("inf")
    return distancia_total

def seleccion_por_torneo(poblacion, grafo, k):
    seleccionados = []
    for _ in range(len(poblacion)):
        competidores = random.sample(poblacion, k)
        mejor = min(competidores, key=lambda ruta: evaluar_ruta(ruta, grafo))
        seleccionados.append(mejor)
    return seleccionados

def cruce_rutas(ruta1, ruta2):
    punto_cruce = random.randint(1, len(ruta1) - 2)
    nueva_ruta = ruta1[:punto_cruce] + [nodo for nodo in ruta2 if nodo not in ruta1[:punto_cruce]]
    return nueva_ruta

def mutacion_ruta(ruta, probabilidad_mutacion):
    if random.random() < probabilidad_mutacion:
        i, j = random.sample(range(1, len(ruta) - 1), 2)
        ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta
