import random

from genetic_algorithm import (
    generar_ruta_aleatoria, evaluar_ruta, seleccion_por_torneo, cruce_rutas, mutacion_ruta
)
from config import CRUCE_PROBABILIDAD, MUTACION_PROBABILIDAD, POBLACION_TAMANO, GENERACIONES, SELECCION_TORNEO_K

def algoritmo_genetico(grafo, aduana, sucursales):
    poblacion = [generar_ruta_aleatoria(aduana, sucursales) for _ in range(POBLACION_TAMANO)]

    for _ in range(GENERACIONES):
        poblacion = sorted(poblacion, key=lambda ruta: evaluar_ruta(ruta, grafo))
        nueva_poblacion = seleccion_por_torneo(poblacion, grafo, SELECCION_TORNEO_K)

        for i in range(0, len(nueva_poblacion) - 1, 2):
            if random.random() < CRUCE_PROBABILIDAD:
                nueva_ruta1 = cruce_rutas(nueva_poblacion[i], nueva_poblacion[i + 1])
                nueva_ruta2 = cruce_rutas(nueva_poblacion[i + 1], nueva_poblacion[i])
                nueva_poblacion[i], nueva_poblacion[i + 1] = nueva_ruta1, nueva_ruta2

        nueva_poblacion = [mutacion_ruta(ruta, MUTACION_PROBABILIDAD) for ruta in nueva_poblacion]
        poblacion = nueva_poblacion

    return min(poblacion, key=lambda ruta: evaluar_ruta(ruta, grafo))
