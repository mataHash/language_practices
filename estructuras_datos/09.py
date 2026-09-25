class Persona:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Ahora tengo {self.edad} anios de edad")


persona1 = Persona("Ana", 25)
persona2 = Persona("Victor", 20)

print(persona1.nombre)
print(persona2.nombre)
