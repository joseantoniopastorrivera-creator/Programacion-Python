# Autor: JAPR
# Fecha: 18/02/26
# Simulacro de examen Python
# Ejercicio 2: Lista de diccionarios

# Creamos una lista vacía
lista_estudiantes = []

# Pedimos datos
for i in range(3):
    print(f"Estudiante {i+1}: ")

    nombre_pedido = input("Nombre: ")
    edad_pedida = int(input("Edad:"))
    nota_pedida = float(input("Nota: "))

    # Diccionario de ese estudiante
    estudiante_temp = {
        "nombre": nombre_pedido,
        "edad": edad_pedida,
        "nota": nota_pedida,
    }

    # Lo añadimos a la lista
    lista_estudiantes.append(estudiante_temp)

# Imprimimos
print(f"\n--RESULTADOS--")

suma_notas = 0

for alum in lista_estudiantes:
    print(f"Nombre: {alum['nombre']}, Edad: {alum['edad']} años, Nota: {alum['nota']}")

    suma_notas = suma_notas + alum["nota"]

promedio = suma_notas / len(lista_estudiantes)
print(f"La nota media es {round(promedio, 2) }")
