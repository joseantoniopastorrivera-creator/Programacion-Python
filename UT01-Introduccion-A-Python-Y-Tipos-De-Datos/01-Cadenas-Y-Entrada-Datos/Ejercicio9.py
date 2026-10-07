nombre = input("Introduzca el nombre del archivo multimedia con extensión:")
punto = nombre.find(".")
nombre_sin_ext = nombre[:punto]
extension = nombre[punto+1:]
nombre_nuevo = "MULTIMEDIA_AÑO_ACTUAL_"+nombre_sin_ext+"."+extension
tamano = len(str(nombre_sin_ext)*2)
print("Nombre:",nombre_sin_ext,"Exensión:",extension,"Nuevo nombre:",nombre_nuevo,"Tamaño estimado en bytes:",tamano)

