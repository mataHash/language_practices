# Crea un programa que genere automáticamente la tabla de multiplicar
print("Iniciando programa.....")
lista = []
for i in range(11):
    lista.append(i * 5)
print(lista)
print("Finalizando programa.....")
pares = [i for i in lista if i % 2 == 0]
for i in lista:
    print(i)
