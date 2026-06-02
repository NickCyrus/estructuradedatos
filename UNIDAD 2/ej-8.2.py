# estructuradedatos
# Estudiante : NICK CYRUS LEMUS DUQUE
# Email      : nick.lemus1910@unisalamanca.edu.co
# Clase      : Estructura de detos
# Docente    : MAURICIO JAVIER BERTEL DOMINGUEZ
# ==========================================================
# RED DE BUSES DE BARRANQUILLA
# Cada estación está conectada con otras estaciones mediante en kilómetros.
# Se utiliza el algoritmo de Dijkstra para encontrar la ruta más corta entre dos estaciones.
# ==========================================================
# Definición de apoyo 
# https://es.wikipedia.org/wiki/Algoritmo_de_Dijkstra


import heapq


class RedBuses:

    def __init__(self):
        # Diccionario que almacena la Red de Buses
        self.estaciones = {}

    # Agrega una nueva estación
    
    def agregar_estacion(self, nombre):

        if nombre not in self.estaciones:
            self.estaciones[nombre] = {}

    
    # Conecta dos estaciones
    
    def agregar_ruta(self,origen, destino,distancia):

        self.estaciones[origen][destino] = distancia
        self.estaciones[destino][origen] = distancia

    
    # Muestra todas las estaciones y conexiones
    
    def mostrar_red(self):

        print("\nRED DE BUSES")

        for estacion, conexiones in self.estaciones.items():

            print(f"\n{estacion}")

            for destino, distancia in conexiones.items():
                print( f"  -> {destino}" f" ({distancia} km)" )

    
    # Busca la ruta más corta usando Dijkstra
    # Aqui sucede la magia :)
    def ruta_mas_corta( self,  inicio,  destino ):

        # Se valida que exista debe coincidir exactamente con con almenos 1 elemento de la variable estaciones Ln: 122
        if inicio not in self.estaciones:
            print("La estación inicial no existe.")
            return

         # Se valida que exista debe coincidir exactamente con con almenos 1 elemento de la variable estaciones Ln: 122
        if destino not in self.estaciones:
            print("La estación destino no existe.")
            return

        # Distancia inicial
        distancias = {
            estacion: float("inf")
            for estacion in self.estaciones
        }

        distancias[inicio] = 0

        # Se guarda el recorrido
        anteriores = {}

        # Cola de prioridad
        cola = [(0, inicio)]

        while cola:

            distancia_actual, actual = (  heapq.heappop(cola) )

            if actual == destino:
                break

            for vecino, distancia in ( self.estaciones[actual].items() ):
                nueva_distancia = ( distancia_actual + distancia )

                if ( nueva_distancia < distancias[vecino] ):
                    distancias[vecino] = (  nueva_distancia  )
                    anteriores[vecino] = actual
                    heapq.heappush( cola, (  nueva_distancia, vecino ) )

        if distancias[destino] == float("inf"):
                print("No existe una ruta.")
                return

        # Establecer el recorrido
        ruta   = []
        actual = destino

        while actual != inicio:
            ruta.append(actual)
            actual = anteriores[actual]

        ruta.append(inicio)
        ruta.reverse()

        print("\nRUTA MÁS CORTA")
        # Se muestra lo elementos de ruta, separados por - >
        print(" -> ".join(ruta))

        #Finalmente mostramos la ruta mas corta encontrada
        print(
            f"Distancia total: "
            f"{distancias[destino]} km"
        )


red = RedBuses()
 
# Estaciones principales de Barranquilla

estaciones = [
    "Portal Joe Arroyo",
    "Murillo Cra 21",
    "Murillo Cra 38",
    "Murillo Cra 46",
    "Murillo Cra 54",
    "Murillo Cra 71",
    "Calle 84",
    "Buenavista",
    "Universidad del Norte",
    "Gran Malecon"
]

for estacion in estaciones:
    red.agregar_estacion(estacion)

 
# Registro relaciones y distancia aproximada 
 
red.agregar_ruta( "Portal Joe Arroyo", "Murillo Cra 21", 2 )
red.agregar_ruta( "Murillo Cra 21", "Murillo Cra 38",  2 )
red.agregar_ruta( "Murillo Cra 38", "Murillo Cra 46", 1 )
red.agregar_ruta( "Murillo Cra 46", "Murillo Cra 54", 1 )
red.agregar_ruta( "Murillo Cra 54", "Murillo Cra 71", 2 )
red.agregar_ruta( "Murillo Cra 71", "Calle 84", 2 )
red.agregar_ruta( "Calle 84", "Buenavista", 2)
red.agregar_ruta( "Buenavista", "Universidad del Norte", 3)
red.agregar_ruta( "Universidad del Norte", "Gran Malecon", 4)
red.agregar_ruta( "Murillo Cra 46",  "Calle 84", 5 )
red.agregar_ruta( "Murillo Cra 54", "Buenavista", 4)
red.agregar_ruta( "Murillo Cra 38" , "Gran Malecon", 10 )

while True:

    print("\n===== RED DE BUSES =====")
    print("1. Mostrar red")
    print("2. Calcular ruta más corta")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:

        case "1":
            red.mostrar_red()

        case "2":
            origen  = input("Estación de salida: ")
            destino = input("Estación de destino: ")
            red.ruta_mas_corta(origen, destino )

        case "3":
            print("Programa finalizado.")
            break

        case _:
            print("Opción inválida.")