texto = input("Introduzca la cadena de caracteres deseada: ")
primero = texto[:3]
segundo = texto[len(texto)-3:]
texto_final = primero + segundo
print(texto_final)