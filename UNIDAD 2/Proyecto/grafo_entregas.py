# estructuradedatos
# Estudiante : NICK CYRUS LEMUS DUQUE
# Email      : nick.lemus1910@unisalamanca.edu.co
# Clase      : Estructura de detos
# Docente    : MAURICIO JAVIER BERTEL DOMINGUEZ

# Aqui aplicamos el concepto de Algoritmo de Dijkstra

import heapq

class GrafoEntregas:

    # Constructor
    def __init__(self):
        # Aquí se guardan las rutas
        self.grafo = {}

    # Agregar una ubicación
    def agregar_ubicacion(self, nombre):

        if nombre not in self.grafo:
            self.grafo[nombre] = {}

    # Crear conexión entre dos puntos
    def conectar( self, origen, destino, distancia ):
        self.grafo[origen][destino] = distancia
        self.grafo[destino][origen] = distancia

    # Calcular la mejor ruta
    def mejor_ruta( self,  origen,  destino  ):

        distancias = {
            nodo: float("inf")
            for nodo in self.grafo
        }

        distancias[origen] = 0
        anteriores         = {}
        cola               = [(0, origen)]

        while cola:
            distancia_actual, actual = (  heapq.heappop(cola) )

            for vecino, distancia in ( self.grafo[actual].items() ):

                nueva_distancia = ( distancia_actual + distancia )

                if ( nueva_distancia < distancias[vecino] ):
                    distancias[vecino] = ( nueva_distancia )
                    anteriores[vecino] = actual
                    heapq.heappush( cola, ( nueva_distancia, vecino))

        ruta   = []
        actual = destino
        while actual != origen:
            ruta.append(actual)
            actual = anteriores[actual]

        ruta.append(origen)
        ruta.reverse()

        print("\nMEJOR RUTA")
        print(" -> ".join(ruta))
        print( f"Distancia total: " f"{distancias[destino]} km" )