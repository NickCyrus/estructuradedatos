# estructuradedatos
# Estudiante : NICK CYRUS LEMUS DUQUE
# Email      : nick.lemus1910@unisalamanca.edu.co
# Clase      : Estructura de detos
# Docente    : MAURICIO JAVIER BERTEL DOMINGUEZ

# ==========================================================
# COLA DE PRIORIDAD PARA TAREAS DE DESARROLLO
# ----------------------------------------------------------
# Ejercicio similar al de la UNIDAD 1 ejercicio ej-8.2.py

import heapq

# Lista que almacenará las tareas
cola_tareas = []

# Contador para mantener el orden de llegada
contador = 0

# Agregar una nueva tarea
def agregar_tarea(nombre, prioridad):

    global contador

    # Urgente tiene mayor prioridad
    if prioridad.lower() == "urgente":
        nivel = 1
    # Normal tiene menor prioridad , cualquier otro concepto que no se URGENTE se interpretara como NORMAL 
    else:
        nivel = 2

    # Se agrega al heap
    heapq.heappush( cola_tareas,  (nivel, contador, nombre) )
    contador += 1
    print("Tarea registrada correctamente.")


# Procesar la siguiente tarea

def procesar_tarea():

    if len(cola_tareas) == 0:
        print("No hay tareas pendientes.")
        return

    prioridad, orden, tarea = heapq.heappop( cola_tareas )

    if prioridad == 1:
        tipo = "URGENTE"
    else:
        tipo = "NORMAL"

    print("\nProcesando tarea:")
    print(f"Tarea: {tarea}")
    print(f"Prioridad: {tipo}")


# Mostrar tareas pendientes

def mostrar_tareas():

    if len(cola_tareas) == 0:
        print("No existen tareas pendientes.")
        return

    print("\nTAREAS PENDIENTES")

    for prioridad, orden, tarea in sorted( cola_tareas ):
        if prioridad == 1:
            tipo = "URGENTE"
        else:
            tipo = "NORMAL"

        print(f"- {tarea} ({tipo})")


# MENÚ PRINCIPAL

while True:

    print("\n===== TASK CONTROL =====")
    print("1. Agregar tarea")
    print("2. Procesar tarea")
    print("3. Mostrar pendientes")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:

        case "1":
            nombre    = input("Nombre de la tarea: ")
            prioridad = input("Prioridad (Urgente/Normal): ")
            agregar_tarea( nombre,  prioridad)

        case "2":
            procesar_tarea()

        case "3":
            mostrar_tareas()

        case "4":
            print("Programa finalizado.")
            break
        case _:
            print("Opción inválida.")