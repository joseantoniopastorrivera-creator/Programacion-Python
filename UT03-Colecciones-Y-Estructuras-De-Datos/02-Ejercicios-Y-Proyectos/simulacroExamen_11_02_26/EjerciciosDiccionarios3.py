# Fecha 18/02/26
# Autor JAPR
# Diccionarios3.py

# Pedimos las palabras
texto_palabras = input("Introduzca la cadena de texto y un espacio")
# Minusculas
texto_palabras_minuscula = texto_palabras.lower()
# Separamos con split
lista_palabras = texto_palabras_minuscula.split()
# Creamos la pizarra de votos y elementos
pizarra_votos = {}
# Recorremos la lista de palabras
for cadenaTexto in lista_palabras:
    if cadenaTexto in pizarra_votos:
        pizarra_votos[cadenaTexto] += 1
    else:
        pizarra_votos[cadenaTexto] = 1
#Resultado
for cadenaTexto, cantidad in pizarra_votos.items():
    print(f"La cadena de texto {cadenaTexto} se repite {cantidad} veces.")