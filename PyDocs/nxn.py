"""
Encontrar el determinante de una matriz por el metodo de cofactores
es equivalente a multiplicar el signo, la columna o fila principal
y luego recursir encontrando la matriz usando la regla de  sarrus

"""


def signo(matriz):
    for i in range(1, len(matriz)):
        signo = (-1) ** (1 + i)
        return signo


def columna_principal(matriz):
    return matriz[0]


def regla_determinante(matriz):
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]


def determinante_total(matriz):
