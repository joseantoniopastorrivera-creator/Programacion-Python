from typing import Any


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def descripcion(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Puertas: {self.puertas}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def descripcion(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Cilindrada: {self.cilindrada}"


coche1 = Coche("Renault", "Clio", 5)
coche2 = Coche("BMW", "F18", 3)
moto1 = Moto("Yamaha", "MT-07", 250)
lista_vehiculos = [coche1, coche2, moto1]

for vehiculo in lista_vehiculos:
    print(vehiculo.descripcion())