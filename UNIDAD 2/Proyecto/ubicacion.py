# estructuradedatos
# Estudiante : NICK CYRUS LEMUS DUQUE
# Email      : nick.lemus1910@unisalamanca.edu.co
# Clase      : Estructura de detos
# Docente    : MAURICIO JAVIER BERTEL DOMINGUEZ

class Ubicacion:

    # Constructor de la ubicación
    def __init__(self, nombre):
        # Guarda el nombre de la ubicación
        self.nombre = nombre


# CLASE CentroDistribucion
# @Ubicacion objeto de la clase Ubicación

class CentroDistribucion(Ubicacion):

    # Constructor
    def __init__(self, nombre):
        # Ejecuta el constructor de la clase Ubicacion
        super().__init__(nombre)
        # Tipo de ubicación
        self.tipo = "Centro de Distribución"

# CLASE PuntoEntrega
# @Ubicacion objeto de la clase Ubicación

class PuntoEntrega(Ubicacion):

    # Constructor
    def __init__(self, nombre):
        # Ejecuta el constructor de la clase padre
        super().__init__(nombre)
        # Tipo de ubicación
        self.tipo = "Punto de Entrega"