# Autor: JAPR
# Fecha: 18/02/26
# Simulacro de examen Python
# Ejercicio 2: Lista de diccionarios

# Creamos una lista vacia donde crearemos a los estudiantes
lista_estudiantes = []

for i in range(3):
    print(f"Estudiante {i+1}")

    nombre_pedido = input("Nombre: ")
    edad_pedido = int(input("Edad: "))
    nota_pedido = float(input("Nota: "))

    # Creamos el diccionario de ese estudiante en concreto
    estudiante_temp = {
        "nombre": nombre_pedido,
        "edad": edad_pedido,
        "nota": nota_pedido,
    }

    # Lo añadimos a nuestra lista general
    lista_estudiantes.append(estudiante_temp)

# Imprimimos
print("\n---RESULTADOS---")

suma_notas = 0

# Recorremos la lista para mostrar datos
for alum in lista_estudiantes:
    print(f"Nombre: {alum['nombre']}, Edad: {alum['edad']} años, Nota: {alum['nota']}")
    
    suma_notas = suma_notas + alum["nota"]
    
#Calculamos la media
promedio = suma_notas/len(lista_estudiantes)

#Redondeamos a dos decimales
print(f"La nota media es {round(promedio, 2)}")
