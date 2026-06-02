# Estudiante : NICK CYRUS LEMUS DUQUE
# Email      : nick.lemus1910@unisalamanca.edu.co
# Clase      : Estructura de detos
# Docente    : MAURICIO JAVIER BERTEL DOMINGUEZ


# Importa el módulo heapq para implementar una cola de prioridad mediante un heap
import heapq

# Clase ColaPrioridad representa una cola de prioridad
class ColaPrioridad:

    # Constructor de la clase
    def __init__(self):
        # Lista que almacenará los clientes y sus prioridades
        self.cola = []

    # Método para agregar un cliente a la cola
    def agregar_cliente(self, nombre, prioridad):

        # Inserta una tupla (prioridad, nombre) en el heap
        # El cliente con menor número de prioridad será atendido primero
        heapq.heappush(self.cola, (prioridad, nombre))

        # Muestra un mensaje confirmando el registro del cliente
        print(f"Cliente {nombre} agregado con prioridad {prioridad}")

    # Método para atender al siguiente cliente
    def atender_cliente(self):

        # Verifica si la cola está vacía
        if not self.cola:
            print("No hay clientes en espera.")
            return

        # Extrae el elemento con mayor prioridad (menor número)
        prioridad, nombre = heapq.heappop(self.cola)

        # Muestra el cliente que será atendido
        print(f"Atendiendo a: {nombre} (Prioridad {prioridad})")
        input("Pulse cualquier tecla para continuar ")

    # Método para visualizar todos los clientes en espera
    def mostrar_cola(self):

        # Comprueba si la cola está vacía
        if not self.cola:
            print("La cola está vacía.")
            input("Pulse cualquier tecla para continuar ")
            return

        # Encabezado de la lista de espera
        print("\n\nClientes en espera:")

        # sorted() permite mostrar los clientes ordenados por prioridad
        for prioridad, nombre in sorted(self.cola):

            # Imprime cada cliente y su prioridad
            print(f"- {nombre} (Prioridad {prioridad})")
        
        print("\n")  
        input("Pulse cualquier tecla para continuar ")
          
 
def limpiar_consola():
    print("\033[H\033[J", end="")


# Crea una instancia de la cola de prioridad
cola = ColaPrioridad()

# Ciclo infinito para mostrar el menú continuamente
while True:
    
    limpiar_consola()
    # Menú de opciones
    print("\n--- SISTEMA DE ATENCIÓN ---")
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Mostrar cola")
    print("4. Salir")

    # Solicita una opción al usuario
    opcion = input("Seleccione una opción: ")
    
    
    # Opción para agregar clientes
    if opcion == "1":
        # Solicita el nombre del cliente
        nombre = input("Nombre del cliente: ")

        # Muestra las prioridades disponibles
        print("\nTipos de prioridad:")
        print("1. VIP")
        print("2. Preferencial")
        print("3. Regular")

        # Solicita la prioridad
        prioridad = int(input("Ingrese la prioridad: "))

        # Verifica que la prioridad sea válida
        if prioridad not in [1, 2, 3]:
            print("Prioridad inválida.")
            continue

        # Agrega el cliente a la cola
        cola.agregar_cliente(nombre, prioridad)

    # Opción para atender al siguiente cliente
    elif opcion == "2":

        # Llama al método de atención
        cola.atender_cliente()

    # Opción para visualizar la cola
    elif opcion == "3":

        # Llama al método que muestra la cola
        cola.mostrar_cola()

    # Opción para finalizar el programa
    elif opcion == "4":

        # Mensaje de despedida
        print("Programa finalizado.")

        # Sale del ciclo while
        break

    # Si el usuario ingresa una opción incorrecta
    else:
        # Muestra un mensaje de error
        print("Opción no válida.")