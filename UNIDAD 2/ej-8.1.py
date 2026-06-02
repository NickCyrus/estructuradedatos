# estructuradedatos
# Estudiante : NICK CYRUS LEMUS DUQUE
# Email      : nick.lemus1910@unisalamanca.edu.co
# Clase      : Estructura de detos
# Docente    : MAURICIO JAVIER BERTEL DOMINGUEZ

# ==========================================================
# TIENDA CON ARBOL BINARIO DE BÚSQUEDA
# ----------------------------------------------------------
# Se utiliza un arbol binario de búsqueda para organizar los productos según su código.
# ==========================================================

# Definición de apoyo 
# Árbol de búsqueda binaria (ABB): 
# El hijo izquierdo siempre contiene valores menores que su padre, 
# y el hijo derecho valores mayores. 
# Esto permite encontrar elementos muy rápidamente dividiendo el grupo por mitades.

# Ilustración : https://www.luisllamas.es/images/20296/programacion-arbol-binario.webp


# Clase producto 

class Producto:

    def __init__(self, codigo, nombre, precio):

        # Código único del producto
        self.codigo = codigo

        # Nombre del producto
        self.nombre = nombre

        # Precio del producto
        self.precio = precio

        # Producto ubicado a la izquierda
        self.izquierda = None

        # Producto ubicado a la derecha
        self.derecha = None


# Clase arbol de productos

class ArbolProductos:

    def __init__(self):

        # Primer producto del arbol
        self.raiz = None

    
    # Agregar un producto
    
    def insertar(self, codigo, nombre, precio):

        if self.buscar(codigo):
            print( f"Ya existe un producto con el código {codigo}. El producto {nombre} no fue agregado." )
            return False
        

        nuevo_producto = Producto(codigo,nombre,precio)

        # Si no existe ningún producto,
        # el nuevo será la raíz
        if self.raiz is None:
            self.raiz = nuevo_producto

        else:
            self.insertar_recursivo(self.raiz,nuevo_producto)
        return True
    
    # Busca la posición correcta para el producto
    def insertar_recursivo(self, actual, nuevo):

        # Si el código es menor, va a la izquierda
        if nuevo.codigo < actual.codigo:

            if actual.izquierda is None:
                actual.izquierda = nuevo
            else:
                self.insertar_recursivo(actual.izquierda,nuevo)

        # Si el código es mayor, va a la derecha
        elif nuevo.codigo > actual.codigo:

            if actual.derecha is None:
                actual.derecha = nuevo
            else:
                self.insertar_recursivo(actual.derecha,nuevo)

    
    # Buscardor
 
    def buscar(self, codigo):

        return self.buscar_recursivo(
            self.raiz,
            codigo
        )

    # Recorre el arbol buscando el código indicado
    def buscar_recursivo(self, actual, codigo):

        # Si no existe el producto
        if actual is None:
            return None

        # Si encontramos el código
        if actual.codigo == codigo:
            return actual

        # Buscar hacia la izquierda
        if codigo < actual.codigo:
            return self.buscar_recursivo(actual.izquierda,codigo)

        # Buscar hacia la derecha
        return self.buscar_recursivo(actual.derecha,codigo )

    
    # Eliminar un producto
   
    def eliminar(self, codigo):
        self.raiz = self.eliminar_recursivo(self.raiz,codigo)

    # Busca el producto y lo elimina
    def eliminar_recursivo(self, nodo, codigo):

        if nodo is None:
            return nodo

        # Buscar a la izquierda
        if codigo < nodo.codigo:
            nodo.izquierda = self.eliminar_recursivo(nodo.izquierda,codigo)

        # Buscar a la derecha
        elif codigo > nodo.codigo:
            nodo.derecha = self.eliminar_recursivo(nodo.derecha,codigo)

        else:

            # Caso 1:
            # No tiene hijos
            if nodo.izquierda is None and nodo.derecha is None:
                return None

            # Caso 2:
            # Tiene solamente hijo derecho
            if nodo.izquierda is None:
                return nodo.derecha

            # Caso 3:
            # Tiene solamente hijo izquierdo
            if nodo.derecha is None:
                return nodo.izquierda

            # Caso 4:
            # Tiene dos hijos
            reemplazo = self.obtener_menor(
                nodo.derecha
            )

            nodo.codigo = reemplazo.codigo
            nodo.nombre = reemplazo.nombre
            nodo.precio = reemplazo.precio

            nodo.derecha = self.eliminar_recursivo(nodo.derecha,reemplazo.codigo)

        return nodo

    # Busca el código más pequeño del lado derecho
    def obtener_menor(self, nodo):

        while nodo.izquierda:
            nodo = nodo.izquierda

        return nodo

    # ------------------------------------------------------
    # Mostrar productos ordenados
    # ------------------------------------------------------
    def mostrar(self):

        if self.raiz is None:
            print("\nNo hay productos registrados.")
            return

        print("\nPRODUCTOS REGISTRADOS")
        self.mostrar_recursivo(self.raiz)

    # Recorre los productos en orden
    def mostrar_recursivo(self, nodo):

        if nodo:

            self.mostrar_recursivo(nodo.izquierda)

            print(f"Código: {nodo.codigo} | "
                f"Nombre: {nodo.nombre} | "
                f"Precio: ${nodo.precio}"
            )

            self.mostrar_recursivo( nodo.derecha )



# Crear el arbol de productos
tienda = ArbolProductos()

while True:

    print("\n===== TIENDA =====")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Mostrar productos")
    print("5. Salir")

    opcion = input("\nSeleccione una opción: ")

    match opcion:

        case "1":
            codigo = int(input("Código del producto: "))
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            if tienda.insertar(codigo,nombre,precio) :
                print("Producto agregado correctamente.")

        case "2":
            codigo = int(input("Código a buscar: "))
            producto = tienda.buscar(codigo)

            if producto:
                print("\nProducto encontrado")
                print(f"Código: {producto.codigo}")
                print(f"Nombre: {producto.nombre}")
                print(f"Precio: ${producto.precio}")
            else:
                print("No existe un producto con ese código.")

        case "3":
            codigo = int(input("Código a eliminar: "))
            tienda.eliminar(codigo)
            print("Proceso completado.")

        case "4":
            tienda.mostrar()

        case "5":
            print("Programa finalizado.")
            break

        case _:
            print("Opción inválida.")