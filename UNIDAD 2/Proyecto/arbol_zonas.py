# estructuradedatos
# Estudiante : NICK CYRUS LEMUS DUQUE
# Email      : nick.lemus1910@unisalamanca.edu.co
# Clase      : Estructura de detos
# Docente    : MAURICIO JAVIER BERTEL DOMINGUEZ

# Aqui aplicamos el concepto de Arbol de búsqueda binaria (ABB)

from nodo_arbol import NodoArbol

class ArbolZonas:

    # Constructor
    def __init__(self):

        # Nodo principal
        self.raiz = None

    # Agregar una ubicación
    def insertar(self, ubicacion):

        nuevo = NodoArbol(ubicacion)

        if self.raiz is None:
            self.raiz = nuevo
            return

        self._insertar(self.raiz, nuevo)

    # Busca la posición correcta
    def _insertar(self, actual, nuevo):

        if nuevo.ubicacion.nombre < actual.ubicacion.nombre:

            if actual.izquierda is None:
                actual.izquierda = nuevo
            else:
                self._insertar( actual.izquierda, nuevo )

        else:

            if actual.derecha is None:
                actual.derecha = nuevo
            else:
                self._insertar( actual.derecha,  nuevo )

    # Mostrar ubicaciones en orden
    def mostrar(self):
        self._mostrar(self.raiz)

    def _mostrar(self, nodo):

        if nodo:
            self._mostrar(nodo.izquierda)
            print(  f"{nodo.ubicacion.nombre}" f" ({nodo.ubicacion.tipo})" )
            self._mostrar(nodo.derecha)