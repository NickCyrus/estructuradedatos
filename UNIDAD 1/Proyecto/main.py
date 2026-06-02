from sistema_vuelos import SistemaVuelos

# =====================================================
# SISTEMA DE RESERVAS DE VUELOS AVIANCA ✈️ 
# Manejo de conceptos:
# - Lista enlazada para reservas confirmadas
# - Cola para lista de espera
# - Pila para cancelaciones
# =====================================================

def CupoAvion():
    return 3

# Creamos un vuelo con capacidad para 3 pasajeros
sistema = SistemaVuelos(CupoAvion())

while True:

    print("\n--- ✈️  AVIANCA RESERVAS ✈️ ---")
    print("Puede utilizar los numero o letras para selecionar la opción del menú \n ")
    print("1. (R) Reservar vuelo")
    print("2. (C) Cancelar reserva")
    print("3. (M) Mostrar estado")
    print("4. (S) Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1" or opcion.lower() == "r":
        nombre = input("Nombre del pasajero: ")
        sistema.reservar(nombre)

    elif opcion == "2" or opcion.lower() == "c":
        nombre = input("Nombre a cancelar: ")
        sistema.cancelar(nombre)

    elif opcion == "3" or opcion.lower() == "m":
        sistema.mostrar_estado()

    elif opcion == "4" or opcion.lower() == "s":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida.")