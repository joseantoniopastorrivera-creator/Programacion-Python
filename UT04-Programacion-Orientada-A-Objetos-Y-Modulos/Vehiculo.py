class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo}"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def tocar_timbre(self):
        return f"¡Ring ring!"

    def descripcion(self):
        info_padre = super().descripcion()
        return f"{info_padre} | Tipo: {self.tipo}"


# PRUEBAS
vehiculo1 = Vehiculo("Renault", "Arkana")
print(vehiculo1.descripcion())

bicicleta_montana = Bicicleta("Orbea", "Model-1", "Montana")
print(bicicleta_montana.descripcion())
print(bicicleta_montana.tocar_timbre())
bicicleta_carretera= Bicicleta("Scott", "No Speed Limit", "Carretera")
print(bicicleta_carretera.descripcion())
