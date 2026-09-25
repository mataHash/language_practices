"""def funcion_recursiva(valor):
    print(valor)
    if valor == 0:
        return print("fin")
    else:
        return funcion_recursiva(valor-1)


funcion_recursiva(100)


def contar_digitos(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + contar_digitos(n/10)


print(contar_digitos(52))
"""


def max(lista):

    if len(lista) == 1:
        return lista[0]
    max_resto = max(lista[1:])

    if lista[0] > max_resto:
        return lista[0]
    else:
        return max_resto


n = [5, 1, 9, 3]
print(max(n))
