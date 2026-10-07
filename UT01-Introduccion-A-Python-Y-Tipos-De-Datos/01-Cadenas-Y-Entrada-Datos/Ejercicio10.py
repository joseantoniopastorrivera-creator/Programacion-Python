resolucion = input("Introduzca la resolución:")
x = resolucion.find("x")
ancho = resolucion[:x]
alto = resolucion[x+1:]
pixeles = int(ancho)*int(alto)
aspect_ratio = round(float(ancho)/float(alto), 2)
print("Ancho de pantalla:",ancho)
print("Alto de la pantalla:", alto)
print("Pixeles de la pantalla:", pixeles)
print("Aspect Ratio de la pantalla:", aspect_ratio)
if aspect_ratio>1.5:
    print("Formato Panorámico.")
elif aspect_ratio<1.5 and aspect_ratio>1.2:
    print("Formato Estándar.")
else:
    print("Formato cuadrado.")

