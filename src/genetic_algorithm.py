import random
import networkx as nx
from utils import afecta_ruta
from config import CONFIG

def algoritmo_genetico(grafo, nodo_aduana, nodos_sucursales, medicamentos, factores_externos):
    POBLACION_INICIAL = CONFIG['POBLACION_INICIAL']
    CRUCE_PROBABILIDAD = CONFIG['CRUCE_PROBABILIDAD']
    MUTACION_PROBABILIDAD = CONFIG['MUTACION_PROBABILIDAD']
    GENERACIONES = CONFIG['GENERACIONES']

    poblacion = inicializar_poblacion(POBLACION_INICIAL, nodos_sucursales)
    
    for _ in range(GENERACIONES):
        nueva_poblacion = []

        for i in range(POBLACION_INICIAL // 2):
            padre1 = seleccionar_individuo(poblacion, grafo, medicamentos, factores_externos)
            padre2 = seleccionar_individuo(poblacion, grafo, medicamentos, factores_externos)
            
            if random.random() < CRUCE_PROBABILIDAD:
                hijo1, hijo2 = cruzar(padre1, padre2)
            else:
                hijo1, hijo2 = padre1, padre2
            
            nueva_poblacion.extend([hijo1, hijo2])

        for i in range(len(nueva_poblacion)):
            if random.random() < MUTACION_PROBABILIDAD:
                nueva_poblacion[i] = mutar(nueva_poblacion[i])

        poblacion = nueva_poblacion

    mejor_ruta = min(poblacion, key=lambda ruta: evaluar_ruta(ruta, grafo, medicamentos, factores_externos))
    return mejor_ruta

def inicializar_poblacion(tamano, nodos_sucursales):
    poblacion = []
    for _ in range(tamano):
        ruta = random.sample(nodos_sucursales, len(nodos_sucursales))
        poblacion.append(ruta)
    return poblacion

def seleccionar_individuo(poblacion, grafo, medicamentos, factores_externos):
    return random.choice(poblacion)

def cruzar(padre1, padre2):
    punto_cruce = len(padre1) // 2
    hijo1 = padre1[:punto_cruce] + [nodo for nodo in padre2 if nodo not in padre1[:punto_cruce]]
    hijo2 = padre2[:punto_cruce] + [nodo for nodo in padre1 if nodo not in padre2[:punto_cruce]]
    return hijo1, hijo2

def mutar(ruta):
    idx1, idx2 = random.sample(range(len(ruta)), 2)
    ruta[idx1], ruta[idx2] = ruta[idx2], ruta[idx1]
    return ruta

def evaluar_ruta(ruta, grafo, medicamentos, factores_externos):
    
    if not all(nodo in grafo.nodes for nodo in ruta):
        return float('inf')  # Penaliza rutas inválidas
    
    distancia_total = 0
    penalizacion = 0

    for i in range(len(ruta) - 1):
        nodo_actual, nodo_siguiente = ruta[i], ruta[i + 1]
        distancia_total += nx.shortest_path_length(grafo, nodo_actual, nodo_siguiente, weight='length')

        for factor in factores_externos:
            if afecta_ruta(factor, nodo_actual, nodo_siguiente):
                penalizacion += CONFIG['IMPACTO_' + factor['impacto'].upper()]

    for medicamento in medicamentos:
        if medicamento['refrigeracion'] and distancia_total > 5000:
            penalizacion += CONFIG['PENALIZACION_REFRIGERACION']

    return distancia_total + penalizacion
