from abc import ABC, abstractmethod


class Cliente:
    def __init__(self, nombre, edad, cuota_mensual):
        self.nombre = nombre
        self.edad = edad
        self.cuota_mensual = cuota_mensual

    def mostrar_info(self):
        return f"{self.nombre} | {self.edad} años | Cuota: {self.cuota_mensual} €."

    def cuota_final(self):
        return self.cuota_mensual

    def es_senior(self):
        return self.edad >= 60


# Zona de pruebas A
print("--- PRUEBA APARTADO A ---")
lista_clientes = [
    Cliente("Carlos López", 35, 45.50),
    Cliente("María Gómez", 65, 45.50),
    Cliente("Luis Pérez", 40, 50.00),
]

for cliente in lista_clientes:
    print(f"{cliente.mostrar_info()} - ¿Es Senior?: {cliente.es_senior()}")


class ClienteVIP(Cliente):
    def __init__(self, nombre, edad, cuota_mensual, descuento):
        super().__init__(nombre, edad, cuota_mensual)
        self.descuento = descuento

    def mostrar_info(self):
        info_padre = super().mostrar_info()
        return f"{info_padre} - [VIP: {self.descuento}% descuento.]"

    def cuota_final(self):
        descuento_dinero = self.cuota_mensual * (self.descuento / 100)
        return self.cuota_mensual - descuento_dinero
    
    def zona_vip(self):
        return "Acceso a zona VIP disponible."
    
#Zona de Pruebas B
print("--- PRUEBA APARTADO B ---")
lista_mixta = [
    Cliente("Ana", 30, 40.00),
    Cliente("Pedro", 25, 40.00),
    ClienteVIP("Ana García", 28, 45.50, 20),
    ClienteVIP("Roberto", 45, 60.00, 10)
]    

for cliente in lista_mixta:
    print(f"{cliente.mostrar_info()} - Cuota a pagar: {cliente.cuota_final()}€.")
    
vip_test = ClienteVIP("Elena", 35, 50.00, 15)  
print(f"Prueba método exclusivo: {vip_test.zona_vip()}")  


class Servicio(ABC):
    @abstractmethod
    def describir(self):
        pass
    
class Entrenamiento(Servicio):
    def describir(self):
        return "Servicio de Entrenamiento: Sesiones personalizadas 1 a 1."
    
class Nutricion(Servicio):
    def describir(self):
        return "Servicio de Nutrición: Planes alimenticios a medida."    
    
#Zona de Pruebas C
print("--- PRUEBA APARTADO C ---")  
servicios_gym = [Entrenamiento(), Nutricion()]
for servicio in servicios_gym:
    print(servicio.describir())  