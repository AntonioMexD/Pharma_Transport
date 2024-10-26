# src/models/medicamento.py
class Medicamento:
    def __init__(self, id_medicamento, nombre, tipo, cantidad, refrigeracion, prioridad, fecha_caducidad):
        self.id_medicamento = id_medicamento
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.refrigeracion = refrigeracion
        self.prioridad = prioridad
        self.fecha_caducidad = fecha_caducidad
