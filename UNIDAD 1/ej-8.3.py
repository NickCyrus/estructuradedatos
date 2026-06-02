# Estudiante : NICK CYRUS LEMUS DUQUE
# Email      : nick.lemus1910@unisalamanca.edu.co
# Clase      : Estructura de detos
# Docente    : MAURICIO JAVIER BERTEL DOMINGUEZ


# CLASE NODO
# Cada nodo representa un contacto de la agenda
class Nodo:

    # Constructor de la clase Nodo
    def __init__(self, nombre, telefono):
        # Almacena el nombre del contacto
        self.nombre = nombre
        # Almacena el teléfono del contacto
        self.telefono = telefono
        # Referencia al siguiente nodo de la lista
        self.siguiente = None


 
# CLASE LISTA ENLAZADA
class AgendaContactos:

    # Constructor de la lista enlazada
    def __init__(self):

        # La lista inicia vacía
        self.nodo = None

    
    # INSERTAR CONTACTO
    def insertar(self, nombre, telefono):

        # Crear un nuevo nodo
        nuevo_contacto = Nodo(nombre, telefono)

        # Si la lista está vacía
        if self.nodo is None:
            # El nuevo nodo se convierte en la nodo
            self.nodo = nuevo_contacto
            print("Contacto agregado correctamente.")
            wait()
            return

        # Variable auxiliar para recorrer la lista
        actual = self.nodo

        # Avanza hasta el último nodo
        while actual.siguiente is not None:
            actual = actual.siguiente

        # Enlaza el último nodo con el nuevo contacto
        actual.siguiente = nuevo_contacto
        print("Contacto agregado correctamente.")
        wait()

    
    # MOSTRAR CONTACTOS
    def mostrar(self):

        # Verifica si la lista está vacía
        if self.nodo is None:
            print("La agenda está vacía.")
            return

        print("\n--- LISTA DE CONTACTOS ---")

        # Comienza desde la nodo
        actual = self.nodo

        # Recorre toda la lista
        while actual is not None:

            # Muestra los datos del nodo actual
            print(f"Nombre: {actual.nombre}")
            print(f"Teléfono: {actual.telefono}")
            print("---------------------")

            # Avanza al siguiente nodo
            actual = actual.siguiente

    # BUSCAR CONTACTO
    def buscar(self, nombre):

        # Empieza desde la nodo
        actual = self.nodo

        # Recorre la lista
        while actual is not None:
            # Compara el nombre buscado convirtiendo los valores en menuscula
            if actual.nombre.lower() == nombre.lower():
                print("\nContacto encontrado:")
                print(f"Nombre: {actual.nombre}")
                print(f"Teléfono: {actual.telefono}")
                wait()
                return

            # Avanza al siguiente nodo
            actual = actual.siguiente

        print("Contacto no encontrado.")
        wait()
    # ELIMINAR CONTACTO
    def eliminar(self, nombre):

        # Apunta al primer nodo
        actual = self.nodo

        # Variable para guardar el nodo anterior
        anterior = None

        # Recorre la lista
        while actual is not None:

            # Si encuentra el contacto
            if actual.nombre.lower() == nombre.lower():

                # Si es el primer nodo
                if anterior is None:

                    # La nodo pasa a ser el siguiente nodo
                    self.nodo = actual.siguiente

                else:

                    # El nodo anterior apunta al siguiente
                    anterior.siguiente = actual.siguiente

                print("Contacto eliminado correctamente.")
                wait()
                return

            # Guarda el nodo actual como anterior
            anterior = actual

            # Avanza al siguiente nodo
            actual = actual.siguiente

        print("Contacto no encontrado.")
        wait()

# Crear la agenda
agenda = AgendaContactos()

def limpiar_consola():
    print("\033[H\033[J", end="")

def wait():
    input("Presione cualquier tecla para continuar")    
# Menú principal
while True:
    
    limpiar_consola()
    
    print("\n===== AGENDA DE CONTACTOS =====")
    print("1. Insertar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar contactos")
    print("5. Salir")

    # Solicita una opción al usuario
    opcion = input("Seleccione una opción: ")

    # Insertar contacto
    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agenda.insertar(nombre, telefono)

    # Buscar contacto
    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        agenda.buscar(nombre)

    # Eliminar contacto
    elif opcion == "3":
        nombre = input("Nombre a eliminar: ")
        agenda.eliminar(nombre)

    # Mostrar todos los contactos
    elif opcion == "4":
        agenda.mostrar()

    # Salir del programa
    elif opcion == "5":

        print("Programa finalizado.")
        break

    # Opción inválida
    else:

        print("Opción no válida.")