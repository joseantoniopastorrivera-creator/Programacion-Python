# Autor: JAPR
# Fecha: 11/02/26
# Simulacro de examen Python
# Ejercicio 2: Lista de diccionarios

#Creamos lista vacia
lista_estudiantes = []

#Recogemos datos
for i in range(2):
    print(f"Estudiante{i+1}:")
    
    nombre_pedido=input("Nombre:")
    edad_pedida=int(input("Edad:"))
    nota_pedida=float(input("Nota:"))
    
    estudiante_temp={
        "nombre":nombre_pedido,
        "edad":edad_pedida,
        "nota":nota_pedida,
    }
    
    lista_estudiantes.append(estudiante_temp)
    
suma_notas=0
for alum in lista_estudiantes:
    print(f"Nombre: {alum['nombre']}, Edad: {alum['edad']} años, Nota: {alum['nota']}")
    
    suma_notas=suma_notas+alum["nota"]
    
promedio=suma_notas/len(lista_estudiantes)

print(f"La media es: {promedio}")
    