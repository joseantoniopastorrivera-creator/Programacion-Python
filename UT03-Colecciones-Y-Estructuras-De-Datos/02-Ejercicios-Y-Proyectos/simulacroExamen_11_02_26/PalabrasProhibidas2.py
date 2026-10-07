# Autor: JAPR
# Fecha: 18/02/26
# Simulacro de examen Python
# Ejercicio 1: Palabras prohibidas

lista_palabras_prohibidas=["joder", "mierda", "coño"]

texto_teclado=input("Introduzca una frase: ")

texto_teclado_minusculas=texto_teclado.lower()

lista_palabras_teclado = texto_teclado_minusculas.split()

pizarra_votos = {}

for palabra in lista_palabras_teclado:
    if palabra in lista_palabras_prohibidas:
        if palabra in pizarra_votos:
         pizarra_votos[palabra]=pizarra_votos[palabra]+1
        else:
            pizarra_votos[palabra]=1
        
        
if len(pizarra_votos)==0:
    print("No se ha localizado ninguna palabra prohibida")
else:      
    for palabra, cantidad in pizarra_votos.items():
     print(f"La palabra {palabra} aparece {cantidad} veces.")