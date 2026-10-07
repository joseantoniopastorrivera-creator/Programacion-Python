nombre = input("Introduzca su nombre completo:")
diseno = input("Introduzca la nota de la asignatura Diseño:")
programacion = input("Introduzca la nota de la asignatura Programación:")
audio = input("Introduzca la nota de la asignatura Audio:")
media = (float(diseno)+float(audio)+float(programacion))/3
partes = nombre.split()
codigo = partes[0][:2].upper()+partes[1][:2].upper()+str(media).replace(".", "")[4:]
print("Su nombre es:", nombre,"Su media es:",str(media),"Su cógigo es:",codigo)