nums = [10, 20, 30, 50, 40]
estudiantes = ["Juan", "Ana", "Pedro"]
mixto = [10, "Hola", 25.6, True]
print(nums[2])
print(estudiantes[1])
print(nums[-1])
print(nums[1:4])
# Mutacion de listas
print(nums[1])
nums.append(60)
print(nums)
nums.insert(2, 25)
print(nums)
nums.pop()
print(nums)
nums.pop(0)
print(nums)
# superficial vs referencial
lista1 = [1, 2, 3]
lista2 = lista1  # referencial
lista3 = lista1[:]  # superficial copia
lista1[0] = 100
print("Lista2", lista2)
print("Lista3", lista3)
