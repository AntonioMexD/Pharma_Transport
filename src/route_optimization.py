# import random

# from genetic_algorithm import (
#     generar_ruta_aleatoria, evaluar_ruta, seleccion_por_torneo, cruce_rutas, mutacion_ruta
# )
# from config import CRUCE_PROBABILIDAD, MUTACION_PROBABILIDAD, POBLACION_TAMANO, GENERACIONES, SELECCION_TORNEO_K

# def algoritmo_genetico(grafo, aduana, sucursales):
#     poblacion = [generar_ruta_aleatoria(aduana, sucursales) for _ in range(POBLACION_TAMANO)]

#     for _ in range(GENERACIONES):
#         poblacion = sorted(poblacion, key=lambda ruta: evaluar_ruta(ruta, grafo))
#         nueva_poblacion = seleccion_por_torneo(poblacion, grafo, SELECCION_TORNEO_K)

#         for i in range(0, len(nueva_poblacion) - 1, 2):
#             if random.random() < CRUCE_PROBABILIDAD:
#                 nueva_ruta1 = cruce_rutas(nueva_poblacion[i], nueva_poblacion[i + 1])
#                 nueva_ruta2 = cruce_rutas(nueva_poblacion[i + 1], nueva_poblacion[i])
#                 nueva_poblacion[i], nueva_poblacion[i + 1] = nueva_ruta1, nueva_ruta2

#         nueva_poblacion = [mutacion_ruta(ruta, MUTACION_PROBABILIDAD) for ruta in nueva_poblacion]
#         poblacion = nueva_poblacion

#     return min(poblacion, key=lambda ruta: evaluar_ruta(ruta, grafo))


# src/route_optimization.py
import networkx as nx
import random

def algoritmo_genetico(grafo, nodo_aduana, nodos_sucursales, medicamentos, factores_externos, generaciones=100, tam_poblacion=50):
    """
    Encuentra la mejor ruta usando un algoritmo genético.
    
    Parámetros:
        grafo: El grafo de la ciudad.
        nodo_aduana: Nodo de origen de la aduana.
        nodos_sucursales: Lista de nodos de las sucursales.
        medicamentos: Lista de medicamentos con sus prioridades y sucursales destino.
        factores_externos: Lista de factores que afectan las rutas.
        generaciones: Número de generaciones para el algoritmo genético.
        tam_poblacion: Tamaño de la población de rutas.
    
    Retorna:
        La mejor ruta encontrada por el algoritmo genético.
    """
    
    def evaluar_ruta(ruta):
        """
        Calcula una puntuación para la ruta según la distancia, medicamentos y factores externos.
        """
        distancia_total = 0
        prioridad_total = 0
        
        for i in range(len(ruta) - 1):
            nodo_origen, nodo_destino = ruta[i], ruta[i + 1]
            # Calcular distancia usando el grafo
            distancia_total += nx.shortest_path_length(grafo, nodo_origen, nodo_destino, weight='length')
        
        # Calcular la prioridad total de la ruta
        for nodo in ruta:
            for med in medicamentos:
                if nodo == med['nodo_sucursal']:
                    prioridad_total += med['prioridad']
        
        # Penalizar según factores externos
        penalizacion = 0
        for factor in factores_externos:
            if factor['nodo_afectado'] in ruta:
                penalizacion += factor['impacto']
        
        # La evaluación es una combinación de distancia y penalización ponderada
        return distancia_total + penalizacion - prioridad_total

    def crear_poblacion_inicial():
        """
        Crea una población inicial de rutas aleatorias.
        """
        poblacion = []
        for _ in range(tam_poblacion):
            ruta = nodos_sucursales[:]
            random.shuffle(ruta)  # Mezclar las sucursales para crear una ruta
            ruta.insert(0, nodo_aduana)  # Incluir el nodo de la aduana al inicio
            poblacion.append(ruta)
        return poblacion

    def seleccionar_padres(poblacion):
        """
        Selecciona dos padres de la población basados en la evaluación de las rutas.
        """
        evaluaciones = [(ruta, evaluar_ruta(ruta)) for ruta in poblacion]
        evaluaciones.sort(key=lambda x: x[1])
        return evaluaciones[0][0], evaluaciones[1][0]  # Retornar las dos mejores rutas

    def cruzar_rutas(padre1, padre2):
        """
        Realiza un cruce entre dos rutas.
        """
        punto_cruce = random.randint(1, len(padre1) - 2)
        hijo1 = padre1[:punto_cruce] + [nodo for nodo in padre2 if nodo not in padre1[:punto_cruce]]
        hijo2 = padre2[:punto_cruce] + [nodo for nodo in padre1 if nodo not in padre2[:punto_cruce]]
        return hijo1, hijo2

    def mutar_ruta(ruta, probabilidad_mutacion=0.1):
        """
        Realiza una mutación en una ruta con cierta probabilidad.
        """
        if random.random() < probabilidad_mutacion:
            idx1, idx2 = random.sample(range(1, len(ruta)), 2)
            ruta[idx1], ruta[idx2] = ruta[idx2], ruta[idx1]

    # Crear la población inicial
    poblacion = crear_poblacion_inicial()

    for _ in range(generaciones):
        nueva_poblacion = []
        for _ in range(tam_poblacion // 2):
            # Seleccionar padres y cruzar
            padre1, padre2 = seleccionar_padres(poblacion)
            hijo1, hijo2 = cruzar_rutas(padre1, padre2)
            
            # Mutar hijos
            mutar_ruta(hijo1)
            mutar_ruta(hijo2)
            
            # Agregar los hijos a la nueva población
            nueva_poblacion.extend([hijo1, hijo2])
        
        # Reemplazar la población antigua por la nueva
        poblacion = nueva_poblacion

    # Obtener la mejor ruta de la población final
    mejor_ruta = min(poblacion, key=evaluar_ruta)
    return mejor_ruta
