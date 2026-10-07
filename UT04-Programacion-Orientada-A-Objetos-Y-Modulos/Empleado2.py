class Empleado2:
    empresa = "Contesta"

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def __str__(self):
        return (
            f"Nombre: {self.nombre} | Salario: {self.salario} | Empresa: {self.empresa}"
        )


class Gerente(Empleado2):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def aumentar_salario(self, porcentaje):
        aumento = self.salario * (porcentaje / 100)
        self.salario += porcentaje
        print(f"El salario de {self.nombre} ha aumentado {porcentaje}%")

    def __str__(self):
        return f"Nombre: {self.nombre} | Salario: {self.salario} | Empresa: {self.empresa} | Departamento: {self.departamento}"


#PRUEBAS
empleado1 = Empleado2("Jose", 1000)
print(empleado1)
gerente1 = Gerente("Kike", 1200, "IT")
print(gerente1)
gerente1.aumentar_salario(10)
print(gerente1)