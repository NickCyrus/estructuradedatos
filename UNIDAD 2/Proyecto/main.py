# estructuradedatos
# Estudiante : NICK CYRUS LEMUS DUQUE
# Email      : nick.lemus1910@unisalamanca.edu.co
# Clase      : Estructura de detos
# Docente    : MAURICIO JAVIER BERTEL DOMINGUEZ

from sistema_entregas import SistemaEntregas

# Definición de lo que hace cada archivo
# sistema_entregas.py :: Carga la información inicial de centro de distribución y punto de entrega
# arbol_zonas.py      :: Contiene la funciones para crear la estructura de arbol de busqueda binaria 
# grafo_entregas.py   :: Contiene la funciones para evaluar los datos y establecer los calculos de la ruta mas corta
# nodo_arbol.py       :: Clase basica de definición de nodo para la clase ArbolZonas en arbol_zonas.py
# ubicacion.py        :: Clase que define la estructura de las ubiciones y herencia , centros de distribución y puntos de entregas    

sistema = SistemaEntregas()
sistema.cargar_datos()

while True:

    print("\n===== SISTEMA DE ENTREGAS =====")
    print("1. Mostrar zonas")
    print("2. Calcular ruta")
    print("3. Salir")

    opcion = input("Seleccione: ")

    match opcion:
        case "1":
            sistema.mostrar_zonas()

        case "2":
            origen = input("Origen: ")
            destino = input("Destino: ")
            # Se ejecuta la llamada al metodo que calcula la ruta de la clase SistemaEntregas heredada de la clase GrafoEntregas
            sistema.calcular_ruta( origen, destino )

        case "3":
            print("Programa finalizado.")
            break

        case _:
            print("Opción inválida.")