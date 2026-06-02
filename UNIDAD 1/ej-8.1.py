# Estudiante : NICK CYRUS LEMUS DUQUE
# Email      : nick.lemus1910@unisalamanca.edu.co
# Clase      : Estructura de detos
# Docente    : MAURICIO JAVIER BERTEL DOMINGUEZ


# Definimos la clase pila para procesar la operación
class Pila:
    # Inicialiamos la clase definiendo que es un items es un arreglo "array"
    def __init__(self):
        self.items = []
    
    # Function para agregar lo elementos a la variable items
    def apilar(self, valor):
        self.items.append(valor)

    # Función para remover elementos de la variable items y valida que no esté vacio
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        raise Exception("Error: faltan operandos.")

    # Función para verificar si el arreglo está vacio o es igual a cero "0"
    def esta_vacia(self):
        return len(self.items) == 0


def calcular_postfija(expresion):
    #Defino los o peradores permitidos
    operadores = ['+', '-', '*', '/']

    #Se instancia la clase pila
    pila = Pila()

    # Recorro la expresión dada por el usuario separando sus elementos
    for token in expresion.split():

        # Verificar si es número y lo agrego a la pila
        try:
            numero = float(token)
            pila.apilar(numero)
            continue
        except ValueError:
            pass

        # Se valida si el elemento iterado no es un operador permitido 
        if token not in operadores:
            print(f"Error: operador '{token}' no permitido.")
            return

        try:
            b = pila.desapilar()
            a = pila.desapilar()
        except Exception as e:
            print(e)
            return

        # Validamos la operaciones de los dos últimos números de la pila. 
        if token == '+':
            resultado = a + b
        elif token == '-':
            resultado = a - b
        elif token == '*':
            resultado = a * b
        elif token == '/':
            if b == 0:
                print("Error: división por cero.")
                return
            resultado = a / b
        #Mostramos por pantalla la operación en curso
        print(f"{a} {token} {b} = {resultado}")
        # Agregamos el resultado a la pila 
        pila.apilar(resultado)
    
    # El ultimo elemento 
    if len(pila.items) != 1:
        print("Error: Expresión postfija inválida.")
        return
    #Mostramos el resultado    
    print("\nResultado final:", pila.desapilar())


# Pedimos por pantalla los valores de la calculadora
expresion = input("Ingrese los valores de la calculadora postfija (elementos separados por espacios): ")

calcular_postfija(expresion)