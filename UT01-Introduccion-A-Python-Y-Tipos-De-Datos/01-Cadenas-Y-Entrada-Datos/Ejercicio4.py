frase = input("Introduzca una frase: ")
posicion = int(input("Introduzca la posición desde la que desea cortar la frase: "))
longitud = int(input("Introduzca la longitud de la nueva frase deseada: "))
print("Su frase es: ", frase[posicion:posicion+longitud])
