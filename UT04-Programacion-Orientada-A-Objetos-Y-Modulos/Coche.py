class Coche:
    ruedas = 4
    
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
    
    def mostrar_info(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Nº ruedas: {self.ruedas}")
        
#PRUEBAS
coche1 = Coche("Renault", "Clio")
coche1.mostrar_info()    
coche2 = Coche("Mercedes Benz", "AMG")
coche2.mostrar_info()       

Coche.ruedas = 6
coche3=Coche("BMW", "M4")
coche3.mostrar_info()