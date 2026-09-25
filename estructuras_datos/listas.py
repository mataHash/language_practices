L = [3, -1, 7, 0, 3, 7, 2, -4, 10, 10]
NEST = [[1, 2], [3, 4], [5, 6]]
sumaTotal = 0
promedio = 0


print("Los valores de la Lista L son:\n", L)
# ------------------------------------------------------------A1------------------------------------------------------


# sumatotal
for i in L:
    sumaTotal += i

print("La suma total equivale a:\n", sumaTotal)
# bucle para promedio
for i in L:
    promedio += i / len(L)
print("El promedio equivale a: \n", promedio)


# Minimo
def encontrarMinimo(numeros):
    if not numeros:
        raise ValueError("No puedo encontrar un Minimo en una lista vacia")

    ActualMinimo = numeros[0]
    for numeros in numeros[1:]:
        if numeros < ActualMinimo:
            ActualMinimo = numeros

    return ActualMinimo


valorMinimo = encontrarMinimo(L)
print("El valor minimo de la lista L equivale a \n", valorMinimo)


# Maximo
def encontrarMaximo(Lista):
    if not Lista:
        raise ValueError("No puedo encontrar un Maximo en un lista vacia")

    ActualMaximo = Lista[0]
    for Lista in Lista[1:]:
        if Lista > ActualMaximo:
            ActualMaximo = Lista
    return ActualMaximo


valorMaximo = encontrarMaximo(L)
print("El valor maximo de la lista L equivale a \n", valorMaximo)

# Conteo de Maximo
conteoMaximo = L.count(valorMaximo)
print("La cantidad de veces que se encuentra el Valor Maximo en la lista L es:\n", conteoMaximo)


# --------------------------------------------------------A2---------------------------------------


# Cuadrados
Cuadrados = [x ** 2 for x in L]
print("La lista L al cuadrado es igual a:\n", Cuadrados)


# Solo Pares
soloPares = [x for x in L if x % 2 == 0]
print("La lista L extraidos los pares equivale a:\n", soloPares)

# No negativos
noNegativos = [x for x in L if x >= 0]
print("Lista L extraidos los no-negativos equivale a: \n", noNegativos)

# --------------------------------------------------------A3---------------------------------------


# Posiciones
Numeroaencontrar = 10
posiciones = [i for i in range(len(L)) if L[i] == Numeroaencontrar]
print("Las posiciones donde se encuentra el numero 10 son:\n", posiciones)
