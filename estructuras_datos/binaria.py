def busquedabinaria(arr, x):
    min = 0
    max = len(arr) - 1
    while min <= max:

        mid = min + (max - min) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            min = mid + 1

        else:
            max = mid - 1

    return -1


arr = []
for i in range(100):
    i = i
    arr.append(i)
x = 10

resultado = busquedabinaria(arr, x)
if resultado != -1:
    print("Elemento presente en el arreglo", resultado)
else:
    print("Elemento no encontrado")
