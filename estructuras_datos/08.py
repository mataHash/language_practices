from collections import deque

cola = deque()


def mostrar_menu():
    print("\n1. agregar clientes")
    print("2. Atender Clientes")
    print("3. Mostrar Cola")
    print("4. Salir")


while True:
    mostrar_menu()
    opcion = input("Elija una opción:")
    if opcion == "1":
        nombre = input("Nombre del Cliente:")
        cola.append(nombre)
        print(f" {nombre} fue agregado a la cola\n")
    elif opcion == "2":
        if cola:
            atendido = cola.popleft()
            print("Atendiendo a:", atendido)
        else:
            print("No hay clientes en espera.")
    elif opcion == "3":
        print("Los clientes por atender son:", list(cola))
    elif opcion == "4":
        break
