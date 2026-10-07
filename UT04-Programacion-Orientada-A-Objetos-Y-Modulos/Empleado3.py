class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_datos(self):
        return f"Nombre: {self.nombre} | Salario: {self.salario}"


class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def mostrar_datos(self):
        datos_base = super().mostrar_datos()
        return f"{datos_base} | Lengüaje: {self.lenguaje}"


# PRUEBAS
empleado1 = Empleado("Jose", 1200)
print(empleado1.mostrar_datos())
programador1 = Programador("Saúl", 1500, "JAVA")
print(programador1.mostrar_datos())
