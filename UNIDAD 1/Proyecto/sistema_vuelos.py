from lista_reservas import ListaReservas
from cola_espera import ColaEspera
from pila_cancelaciones import PilaCancelaciones

# -----------------------------------------------------
# Clase principal del sistema
# -----------------------------------------------------
class SistemaVuelos:

    def __init__(self, capacidad):

        # Número máximo de pasajeros permitidos
        self.capacidad = capacidad

        # Reservas confirmadas
        self.reservas = ListaReservas()

        # Lista de espera
        self.espera = ColaEspera()

        # Historial de cancelaciones
        self.cancelaciones = PilaCancelaciones()

    # Registrar una nueva reserva
    def reservar(self, nombre):

        if self.reservas.cantidad() < self.capacidad:

            self.reservas.agregar(nombre)
            print(f"Reserva confirmada para {nombre}")

        else:

            self.espera.encolar(nombre)
            print(
                f"Vuelo lleno. {nombre} agregado a la lista de espera."
            )

    # Cancelar una reserva
    def cancelar(self, nombre):

        eliminado = self.reservas.eliminar(nombre)

        if eliminado:

            self.cancelaciones.apilar(nombre)

            print(f"Reserva cancelada para {nombre}")

            # Si existe alguien esperando, ocupa el lugar libre
            if not self.espera.esta_vacia():

                siguiente = self.espera.desencolar()

                self.reservas.agregar(siguiente)

                print(
                    f"{siguiente} salió de la lista de espera y obtuvo una reserva."
                )

        else:
            print("Reserva no encontrada.")

    # Mostrar toda la información
    def mostrar_estado(self):

        print("\n===== ESTADO DEL VUELO =====")

        self.reservas.mostrar()
        self.espera.mostrar()
        self.cancelaciones.mostrar()

        print("============================")