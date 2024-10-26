# src/models/sucursal.py

class Sucursal:
    def __init__(self, id_sucursal, nombre, latitud, longitud, capacidad, almacenamiento_especial=False):
        """
        Inicializa una sucursal de farmacia.

        :param id_sucursal: ID único de la sucursal.
        :param nombre: Nombre o referencia de la sucursal.
        :param latitud: Latitud de la ubicación de la sucursal.
        :param longitud: Longitud de la ubicación de la sucursal.
        :param capacidad: Capacidad de almacenamiento de la sucursal.
        :param almacenamiento_especial: Indica si la sucursal tiene capacidad de almacenamiento especial (por ejemplo, refrigeración).
        """
        self.id_sucursal = id_sucursal
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.capacidad = capacidad
        self.almacenamiento_especial = almacenamiento_especial

    def __repr__(self):
        return f"Sucursal({self.id_sucursal}, {self.nombre}, {self.latitud}, {self.longitud}, Capacidad: {self.capacidad}, Almacenamiento Especial: {self.almacenamiento_especial})"
