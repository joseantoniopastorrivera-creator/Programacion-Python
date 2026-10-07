class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_datos(self):
        return f"Nombre: {self.nombre} | Salario: {self.salario} euros."


class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def mostrar_datos(self):
        datos_comunes = super().mostrar_datos()
        return f"{datos_comunes} | Lenguaje: {self.lenguaje}."


empleado1 = Empleado("Jose", 1000)
print(empleado1.mostrar_datos())
programador1 = Programador("Andrés", 1200, "Java")
print(programador1.mostrar_datos())
