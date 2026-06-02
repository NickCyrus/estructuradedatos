# estructuradedatos
# Estudiante : NICK CYRUS LEMUS DUQUE
# Email      : nick.lemus1910@unisalamanca.edu.co
# Clase      : Estructura de detos
# Docente    : MAURICIO JAVIER BERTEL DOMINGUEZ

# CLASE NodoArbol
# @Ubicacion objeto de la clase Ubicación

class NodoArbol:

    # Constructor del nodo
    def __init__(self, ubicacion):
        # Información almacenada
        self.ubicacion = ubicacion
        # Hijo izquierdo
        self.izquierda = None
        # Hijo derecho
        self.derecha = None