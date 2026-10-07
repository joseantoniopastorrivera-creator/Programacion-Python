#Autor JAPR
#Fecha 18/02/26
#Ejercicio 1: Listas

#Definimos la función pedida por el enunciado
def procesar_lista(numeros, nuevo):

    #Validamos que la lista tenga 5 elementos, si no que devuelva la lista original sin cambios
    if len(numeros) != 5:
        return numeros
    
    #Añadimos el número nuevo al inicio de la lista
    numeros.insert(0, nuevo)

#Ordenar de menor a mayor
    numeros.sort()
    
    #Eliminar el elemento del medio
    medio = (len(numeros) - 1) // 2
    numeros.pop(medio)

   # Devolvemos la lista resultante ahora que ya hemos quitado el elemento del medio
    return numeros

# RESULTADO
entrada = [10, 3, 7, 2, 5]
nuevo_num = 8
print("\n--RESULTADO--")
#Solución 1
resultado = procesar_lista(entrada, nuevo_num)
print(f"SOLUCIÓN 1: {resultado}")
#Solución 2
resultado2 = procesar_lista([10, 3, 7, 2 ,5], 8)
print(f"SOLUCIÓN 2: {resultado2}")
#Solución 3(Con otra entrada diferente, no lo pide el enunciado)
resultado3 = procesar_lista([5, 3 ,8, 7, 9], 11)
print(f"SOLUCIÓN 3: {resultado3}")