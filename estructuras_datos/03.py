# notacion O grande (Big 0 Notation - Analisis de algoritmos)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def obtener_elemento(listaEntrada):
    return listaEntrada[0]  # O(1) - tiempo constante -- Algoritmo de ccontante


# O(n) - Tiempo lineal - crecimiento lineal (costo variable)


def sumar_elementos(listaEntrada):

    suma = 0
    for elemento in listaEntrada:
        suma += elemento
    return suma
# O(log - n) - Tiempo logaritmico - crecimiento logaritmico (costo variable)


def busqueda_binaria(listaEntrada, objetivo):
    izquierda = 0
    derecha = len(listaEntrada) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if listaEntrada[medio] == objetivo:
            return medio
        elif listaEntrada[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


# o(n^2) - tiempo cuadratico - crecimiento cuadratico (Costo variable)


def pares(listaEntrada):
    for i in range(len(listaEntrada)):
        for j in range(len(listaEntrada)):
            print(listaEntrada[i], listaEntrada[j])


# O(n*m) - tiempo multiplicativo - crecimiento multiplicativo (costo variable)


def combinaciones(listaA, listaB):
    for elementoA in listaA:
        for elementoB in listaB:
            if elementoA == elementoB:
                print((elementoA, elementoB))


print(obtener_elemento(lista))
print(sumar_elementos(lista))
print(busqueda_binaria(lista, 7))
pares(lista)
combinaciones(lista, lista)
