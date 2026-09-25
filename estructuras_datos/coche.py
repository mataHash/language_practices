class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self, cantidad):
        self.velocidad += cantidad

    def frenar(self, cantidad):
        self.velocidad -= cantidad

    def mostrar_estado(self):
        print(f"Marca:{self.marca}\n Modelo:{
              self.modelo}\n Velocidad:{self.velocidad}")


mi_coche = Coche("Toyota", "Corolla")
mi_coche.acelerar(25)
mi_coche.frenar(10)
mi_coche.mostrar_estado()
