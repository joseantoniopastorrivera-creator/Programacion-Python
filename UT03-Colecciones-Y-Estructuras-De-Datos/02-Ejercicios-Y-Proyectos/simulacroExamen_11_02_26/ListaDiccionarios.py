# Autor: JAPR
# Fecha: 11/02/26
# Simulacro de examen Python
# Ejercicio 2: Lista de diccionarios

# Creamos la lista vacía donde guardaremos a todos
lista_estudiantes = []

# Bucle para pedir los datos 3 veces
for i in range(3):
    print(f"Estudiante {i+1}:")

    # Pedimos datos y convertimos edad a int y nota a float
    nombre_pedido = input("Nombre: ")
    edad_pedido = int(input("Edad: "))
    nota_pedida = float(input("Nota: "))

    # Creamos el diccionario de este estudiante concreto
    estudiante_temp = {
        "nombre": nombre_pedido,
        "edad": edad_pedido,
        "nota": nota_pedida,
    }

    # Lo añadimos a nuestra lista general
    lista_estudiantes.append(estudiante_temp)

# RESULTADOS
print("\nLista de estudiantes:")

# Inicializamos el acumulador para sumar notas
suma_notas = 0

# Recorremos la lista para mostrar datos y sumar notas
for alum in lista_estudiantes:
    # Mostramos los datos con f-string accediendo a las claves
    print(f"- {alum['nombre']}, {alum['edad']} años, nota: {alum['nota']}")

    # Sumamos su nota al total
    suma_notas += alum["nota"]

# Calculamos la media
# Dividimos la suma total entre la cantidad de alumnos (len)
promedio = suma_notas / len(lista_estudiantes)

# Mostramos redondeando a 2 decimales para que quede limpio
print(f"Nota promedio: {round(promedio, 2)}")
