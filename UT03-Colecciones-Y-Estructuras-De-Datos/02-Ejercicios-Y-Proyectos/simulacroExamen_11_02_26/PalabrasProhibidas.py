# Autor: JAPR
# Fecha: 11/02/26
# Simulacro de examen Python
# Ejercicio 1: Palabras prohibidas

# Creamos la lista de palabras prohibidas
lista_palabras_prohibidas = ["increible", "milagro", "impactante"]

# Creamos el diccionario vacío
diccionario_vacio = {}

# Pedimos la frase en concreto
texto_usuario = input("Introduce el texto a analizar: ")

# Lo convertimos a minúsculas
texto_minusculas = texto_usuario.lower()

# Dividimos el texto en palabras para analizarlo
lista_palabras = texto_minusculas.split()

# Recorremos la lista de palabras
for palabra in lista_palabras:
    # Limpiamos los signos de puntuación
    palabra_limpia = palabra.strip(".,¿?!¡")

    # Comprobamos si está en la lista negra
    if palabra_limpia in lista_palabras_prohibidas:

        # Condición para conteo en el diccionario
        if palabra_limpia in diccionario_vacio:
            # Si ya existía le sumamos 1 al contador actual
            diccionario_vacio[palabra_limpia] += 1
        else:
            # Si es la primera vez que aparece, la inicializamos en 1
            diccionario_vacio[palabra_limpia] = 1

# RESULTADOS
print("\n---RESULTADOS---")

# Si el diccionario está vacío (len == 0), es que no hubo coincidencias
if len(diccionario_vacio) == 0:
    print("No se encontraron palabras prohibidas.")
else:
    print("Palabras prohibidas encontradas:")
    # Recorremos el diccionario para mostrar clave (palabra) y valor (cantidad)
    for palabra, cantidad in diccionario_vacio.items():
        print(f"- {palabra}: {cantidad} vez/veces")
