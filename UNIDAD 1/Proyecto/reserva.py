# -----------------------------------------------------
# Clase que representa una reserva
# -----------------------------------------------------
class Reserva:
    def __init__(self, nombre):
        # Guarda el nombre del pasajero
        self.nombre = nombre

        # Apunta al siguiente elemento de la lista
        self.siguiente = None
