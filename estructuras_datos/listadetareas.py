tarea = []


def menu_principal():
    print("seleccione una opción")
    print("\n1. Insertar tarea")
    print("2. Terminar tarea")
    print("3. mostrar tareas")
    print("4. Salir")


def insertar_tarea():
    tar = input("Inserte nombre de tarea\n")
    tarea.append(tar)
    print(f"tarea {tar} insertada\n")


def terminar_tarea():
    print("verifique el nombre de la tarea a terminar\n")
    tareas_pendientes()
    index_tarea = int(input(
        "para eliminar las tareas, escriba el numero de tarea que desee terminar:"))
    ter_tar = tarea.pop(index_tarea-1)
    print(f"Tarea {ter_tar} eliminada")


def tareas_pendientes():
    print(f"las tareas pendientes son: \n {tarea}")


while True:
    menu_principal()
    opcion = int(input("Inserte solo el numero de opción:"))
    if opcion == 1:
        insertar_tarea()
    elif opcion == 2:
        terminar_tarea()
    elif opcion == 3:
        tareas_pendientes()
    else:
        print("¡Programa Terminado!")
        break
