# -----------------------------------------------------
# Cola para pasajeros en espera
# -----------------------------------------------------
class ColaEspera:
    def __init__(self):
        self.cola = []

    # Agrega un pasajero al final de la cola
    def encolar(self, nombre):
        self.cola.append(nombre)

    # Atiende al primer pasajero de la cola
    def desencolar(self):

        if len(self.cola) == 0:
            return None

        return self.cola.pop(0)

    # Verifica si la cola está vacía
    def esta_vacia(self):
        return len(self.cola) == 0

    # Muestra la cola de espera
    def mostrar(self):

        if self.esta_vacia():
            print("No hay pasajeros en espera.")
            return

        print("\nPasajeros en espera:")

        for pasajero in self.cola:
            print("-", pasajero)