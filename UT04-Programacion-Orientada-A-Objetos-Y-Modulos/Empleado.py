class Empleado:
    empresa = "Google"

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def __str__(self):
        return f"Nombre: {self.nombre} | Salario: {self.salario} euros | Empresa: {self.empresa}"


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def aumentar_salario(self, porcentaje):
        aumento = self.salario * (porcentaje / 100)
        self.salario += aumento
        print(f"El salario de {self.nombre} ha aumentado en {porcentaje}%")

    def __str__(self):
        return f"Nombre: {self.nombre} | Salario: {self.salario} euros | Empresa: {self.empresa}"


# Zona de pruebas
empleado1 = Empleado("Jose", 1200)
print(empleado1)
empleado2 = Empleado("Ivan", 1300)
print(empleado2)
gerente1 = Gerente("Pablo", 1500, "IT")
print(gerente1)
gerente1.aumentar_salario(10)
print(gerente1)
