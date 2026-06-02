from reserva import Reserva

# -----------------------------------------------------
# Lista enlazada para reservas confirmadas
# -----------------------------------------------------
class ListaReservas:
    def __init__(self):
        # Inicio de la lista
        self.cabeza = None

    # Agrega una nueva reserva al final de la lista
    def agregar(self, nombre):

        nueva_reserva = Reserva(nombre)

        # Si la lista está vacía, la reserva será la primera
        if self.cabeza is None:
            self.cabeza = nueva_reserva
            return

        # Recorremos hasta llegar al último elemento
        actual = self.cabeza

        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nueva_reserva

    # Elimina una reserva por nombre
    def eliminar(self, nombre):

        actual = self.cabeza
        anterior = None

        while actual:

            if actual.nombre == nombre:

                # Si es el primer elemento
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                return True

            anterior = actual
            actual = actual.siguiente

        return False

    # Cuenta cuántas reservas existen
    def cantidad(self):

        contador = 0
        actual = self.cabeza

        while actual:
            contador += 1
            actual = actual.siguiente

        return contador

    # Muestra las reservas registradas
    def mostrar(self):

        actual = self.cabeza

        if actual is None:
            print("No hay reservas confirmadas.")
            return

        print("\nReservas confirmadas:")

        while actual:
            print("-", actual.nombre)
            actual = actual.siguiente