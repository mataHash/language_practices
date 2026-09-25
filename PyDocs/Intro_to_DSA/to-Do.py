"""
This is  a Basic To-Do implementation made by hand in python
this app will have the oportunity of making
insertions/editions, searching and deleting elements.
"""
lista = []


def menu_principal():
    print("Saludos, compañer@!",
          "¿Cómo se siente? Espero que bien", "esto es un gestor de tareas")
    print("inserte un número para realizar una acción: ",
          "1. agregar tarea",
          "2. eliminar tarea",
          "3. buscar tarea",
          "4. editar tarea", sep="\n")


def agregar_elementos(elemento):
    elemento = input("Inserte una tarea")
    lista.append(elemento)
    print("tarea agregada")


def eliminar_elementos(index):
    index = int(input("Inserte el indice del elemento a eliminar: "))
    lista.pop(index)
    print(f"elemento no.{index} eliminado")


def editar_elementos(index, tarea_a_editar):
    index = int(input("Inserte el indice de la tarea a editar: "))
    tarea_a_editar = input("inserte la tarea editada: ")
    tarea_a_editar = lista[index]
    print("tarea editada correctamente")


def buscar_elementos_por_indice(index):
    print("Inserte el indice del elemento a buscar: ")
    print(lista[index + 1])


def buscar_elementos_por_nombre(elemento):
    print("Inserte el elemento a buscar: ")
    busqueda = lista.index(elemento)
    print("elemento encontrado en la posicion ", busqueda)


if __name__ == "__main__":
    while True:
        menu_principal()
        main_input = int(input())
        if main_input == 1:
            agregar_elementos()
        elif main_input == 2:
            eliminar_elementos()
        elif main_input == 3:
            buscar_elementos_por_indice():
        elif main_input == 4:
            buscar_elementos_por_nombre():
        elif main_input == 5:
            False
