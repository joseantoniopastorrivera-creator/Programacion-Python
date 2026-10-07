class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas=puertas
    
    def descripcion(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Puertas: {self.puertas}."    

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada=cilindrada     
        
    def descripcion(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Cilindrada: {self.cilindrada}"             
    
lista_vehiculos = []
coche1 = Coche("Mercedes Benz", "Clase C", 5)
coche2 = Coche("Opel", "Corsa", 3)
moto1 =  Moto("Kawasaki", "Ninja", 250)   

lista_vehiculos.append(coche1)
lista_vehiculos.append(coche2)
lista_vehiculos.append(moto1)
for vehiculo in lista_vehiculos:
    print(vehiculo.descripcion())