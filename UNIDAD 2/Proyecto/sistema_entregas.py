from ubicacion import (  CentroDistribucion,  PuntoEntrega )

from arbol_zonas import ArbolZonas
from grafo_entregas import GrafoEntregas


class SistemaEntregas:

    # Constructor
    def __init__(self):

        self.arbol = ArbolZonas()
        self.grafo = GrafoEntregas()

    # Cargar información inicial
    def cargar_datos(self):

        ubicaciones = [
            CentroDistribucion("Centro Logistico"),
            PuntoEntrega("Buenavista"),
            PuntoEntrega("Riomar"),
            PuntoEntrega("Alto Prado"),
            PuntoEntrega("Villa Carolina")
        ]

        for ubicacion in ubicaciones:
            self.arbol.insertar(  ubicacion )
            self.grafo.agregar_ubicacion( ubicacion.nombre )

        self.grafo.conectar( "Centro Logistico", "Alto Prado", 4 )
        self.grafo.conectar( "Alto Prado", "Buenavista", 3 )
        self.grafo.conectar( "Buenavista", "Villa Carolina", 2 )
        self.grafo.conectar( "Villa Carolina", "Riomar", 2 )

    # Mostrar ubicaciones
    def mostrar_zonas(self):
        self.arbol.mostrar()

    # Calcular una entrega
    def calcular_ruta( self, origen, destino ):
        self.grafo.mejor_ruta(  origen, destino )