# Fecha 18/02/26
# Autor JAPR
# Diccionarios4.py

#Pedimos la lista de cadenas de texto por teclado
lista_texto=input("Introduce las votaciones separadas por un espacio: ")

#Lo convertimos a minúscula 
lista_texto_minuscula=lista_texto.lower()

#Lo convertimos en una lista con split
lista_palabras=lista_texto_minuscula.split()

#Creamos una pizarra en blanco para contar votos
pizarra_votos={}

#Recorremos la lista de palabras, si está repetida le sumamos un voto y si no creamos una nueva categoria
for voto in lista_palabras:
    if voto in pizarra_votos:
        pizarra_votos[voto]=pizarra_votos[voto]+1
    else:
        pizarra_votos[voto]=1
        
#Ahora que ya tenemos los votos imprimimos
for elemento, cantidad in pizarra_votos.items():
    print(f"El elemento de la lista {elemento} tiene {cantidad} votos.")