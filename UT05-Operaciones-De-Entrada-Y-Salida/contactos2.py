import json

datos_contactos = [
    {"nombre": "Ana", "telefono": "600111222", "favorito": True},
    {"nombre": "Luis", "telefono": "600333444", "favorito": False},
    {"nombre": "Marta", "telefono": "600555666", "favorito": True},
    {"nombre": "Alberto", "telefono": "600777888", "favorito": True},
]

with open("contactos2.json", mode="w", encoding="utf-8") as archivo_escritura:
    json.dump(datos_contactos, archivo_escritura, indent=4)

with open("contactos2.json", mode="r", encoding="utf-8") as archivo_lectura:
    agenda = json.load(archivo_lectura)

lista_favoritos = []
for contacto in agenda:
    if contacto["favorito"] == True:
        lista_favoritos.append(contacto)

lista_favoritos.sort(key=lambda x: x["nombre"])
for contacto in agenda:
    print(f"{contacto["nombre"]} - Telf: {contacto["telefono"]}")
