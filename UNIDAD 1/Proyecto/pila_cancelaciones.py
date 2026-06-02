# -----------------------------------------------------
# Pila para registrar cancelaciones
# -----------------------------------------------------
class PilaCancelaciones:
    def __init__(self):
        self.pila = []

    # Guarda una cancelación
    def apilar(self, nombre):
        self.pila.append(nombre)

    # Obtiene la última cancelación realizada
    def desapilar(self):

        if len(self.pila) == 0:
            return None

        return self.pila.pop()

    # Muestra el historial de cancelaciones
    def mostrar(self):

        if len(self.pila) == 0:
            print("No existen cancelaciones.")
            return

        print("\nHistorial de cancelaciones:")

        for pasajero in reversed(self.pila):
            print("-", pasajero)