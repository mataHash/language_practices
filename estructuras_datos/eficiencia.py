import random  # Importar funcion de aleatoriedad
import time  # Importar funcion tiempo

lista = []  # Declaracion de lista
numero = 8128  # Numero a encontrar

# Generacion de lista aleatoria
numeros_random = random.sample(range(1000000), k=10000)

lista.append(numeros_random)

print("La lista ramdom es:\n", lista)


# O(n)
def on(Lista):
    for i in Lista:
        if numero == i:
            return True
    return False


Inicio = time.time()  # Inicio de conteo

on(lista)
print("El resultado de O(n) \n", on(lista))

fin = time.time()  # Fin de conteo

tiempo_tardado = fin - Inicio

print("La Complejidad de este bucle O(n) en segundos equivale a: \n ", tiempo_tardado)


# O(n^2)
def on2(Lista):
    for i in Lista:
        for y in Lista:
            if numero == i == y:
                return True

    return False


Inicio2 = time.time()

on2(lista)
print("El resultado de On^2 es: \n", on2(lista))

fin2 = time.time()

tiempo_tardado2 = fin2 - Inicio2

print("La Complejidad de este bucle O(n^2) en segundos equivale a: \n ", tiempo_tardado2)
