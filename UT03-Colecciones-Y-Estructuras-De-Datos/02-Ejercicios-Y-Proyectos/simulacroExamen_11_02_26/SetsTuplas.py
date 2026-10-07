# Autor: JAPR
# Fecha: 11/02/26
# Simulacro de examen Python
# Ejercicio 3: Sets y tuplas

#Pedimos la frase al usuario
frase_usuario = input("Introduce una frase: ")

# Convertimos la frase en lista para tener orden
# Usamos split() que corta por los espacios
lista_palabras = frase_usuario.split()

# Convertimos la lista a set para quitar duplicados automáticamente
set_unico = set(lista_palabras)

# Guardamos la "ficha técnica" de la frase
# Usamos len() para contar, [0] para la primera y [-1] para la última
cantidad = len(lista_palabras)
primera = lista_palabras[0]
ultima = lista_palabras[-1]

# Guardamos todo en una tupla inmutable
tupla_datos = (cantidad, primera, ultima)

#  RESULTADOS
print(f"Palabras únicas: {set_unico}")

# Para mostrar los datos, los sacamos de la tupla por su posición
print(f"Cantidad de palabras: {tupla_datos[0]}")
print(f"Primera palabra: {tupla_datos[1]}")
print(f"Última palabra: {tupla_datos[2]}")