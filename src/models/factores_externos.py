# src/models/factores_externos.py
class FactorExterno:
    def __init__(self, id_factor, tipo_factor, ubicacion, impacto, fecha_inicio, fecha_fin):
        self.id_factor = id_factor
        self.tipo_factor = tipo_factor
        self.ubicacion = ubicacion
        self.impacto = impacto
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
