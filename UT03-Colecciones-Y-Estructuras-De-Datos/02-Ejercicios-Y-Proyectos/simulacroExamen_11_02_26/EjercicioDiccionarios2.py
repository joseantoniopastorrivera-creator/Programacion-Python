# Fecha 18/02/26
# Autor JAPR
# Diccionarios2.py

# Declaramos la cadena de texto que guarda los votos individualmente y separados con espacios
texto_votos = input("Introduce los votos separados por un espacio:")

# Convertimos a minúsculas
texto_votos_minuscula = texto_votos.lower()

# Creamos una coleccion
lista_votos = texto_votos_minuscula.split()

# Creamos la pizarra en blanco
pizarra_votos = {}

# for recorriendo la lista de votos y pizarra
for voto in lista_votos:
    if voto in pizarra_votos:
        #Si el voto ya estaba le sumamos uno
        pizarra_votos[voto] += 1
    else:
        #Si el voto no esta, ponemos a 1 y lo creamos
        pizarra_votos[voto] = 1

#Resultado
for voto, cantidad in pizarra_votos.items():
    print(f"El voto {voto} ha obtenido una puntuación de {cantidad}.")
