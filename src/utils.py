# import osmnx as ox
# import pandas as pd

# def cargar_grafo(ciudad, tipo_red="drive"):
#     return ox.graph_from_place(ciudad, network_type=tipo_red)

# def cargar_sucursales(ruta_archivo):
#     return pd.read_csv(ruta_archivo)[['latitud', 'longitud']].values

# def guardar_grafo(grafo, ruta_archivo):
#     ox.save_graphml(grafo, ruta_archivo)

# def obtener_nodos_mas_cercanos(grafo, sucursales):
#     return [ox.distance.nearest_nodes(grafo, suc[1], suc[0]) for suc in sucursales]

# src/utils.py
import csv
import osmnx as ox
import pandas as pd

def obtener_nodo_cercano(lat, lon, grafo):
    return ox.distance.nearest_nodes(grafo, lon, lat)

# def cargar_sucursales(filepath):
#     sucursales = []
#     with open(filepath, 'r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             sucursal = {
#                 "id_sucursal": int(row['id_sucursal']),
#                 "nombre": row['nombre'],
#                 "latitud": float(row['latitud']),
#                 "longitud": float(row['longitud']),
#                 "capacidad": int(row['capacidad']),
#                 "almacenamiento_especial": row['almacenamiento_especial'].lower() == 'si'
#             }
#             sucursales.append(sucursal)
#     return sucursales

# def cargar_sucursales(filepath, grafo):
#     df = pd.read_csv(filepath)
#     nodos = []
#     for _, row in df.iterrows():
#         nodo_cercano = obtener_nodo_cercano(row['latitud'], row['longitud'], grafo)
#         nodos.append(nodo_cercano)
#     return nodos

def cargar_sucursales(archivo_csv, grafo):
    try:
        df = pd.read_csv(archivo_csv)
        print("Datos del archivo CSV: \n", df.head())  # Muestra las primeras filas del DataFrame

        # Devuelve una lista de diccionarios
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {e}")
        return []


def cargar_medicamentos(filepath):
    medicamentos = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            medicamento = {
                "id_medicamento": int(row['id_medicamento']),
                "nombre": row['nombre'],
                "tipo": row['tipo'],
                "cantidad": int(row['cantidad']),
                "refrigeracion": row['refrigeracion'].lower() == 'si',
                "prioridad": row['prioridad'].lower(),
                "fecha_caducidad": row['fecha_caducidad']
            }
            medicamentos.append(medicamento)
    return medicamentos

def cargar_factores(filepath):
    factores = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            factor = {
                "id_factor": int(row['id_factor']),
                "tipo_factor": row['tipo_factor'],
                "ubicacion": (float(row['ubicacion_lat']), float(row['ubicacion_lon'])),
                "impacto": row['impacto'].lower(),
                "fecha_inicio": row['fecha_inicio'],
                "fecha_fin": row['fecha_fin']
            }
            factores.append(factor)
    return factores

def afecta_ruta(factor, nodo_actual, nodo_siguiente):
    # Verificar si la ruta se ve afectada por un factor externo (manifestación, clima, etc.)
    return False  # Puedes definir lógica más avanzada aquí

def obtener_nodos_mas_cercanos(grafo, ubicaciones):
    return [ox.distance.nearest_nodes(grafo, lon, lat) for lat, lon in ubicaciones]
