import json

datos_contactos = [
    {"nombre": "Ana", "telefono": "600111222", "favorito": False},
    {"nombre": "Luis", "telefono": "600333444", "favorito": False},
    {"nombre": "Marta", "telefono": "600555666", "favorito": False},
    {"nombre": "Alberto", "telefono": "600777888", "favorito": True},
]

with open("contactos4.json", encoding="utf-8", mode="w") as archivo_lectura:
    json.dump(datos_contactos, archivo_lectura, indent=4)
    
with open("contactos4.json", mode="r", encoding="utf-8") as archivo_escritura:
   agenda= json.load(archivo_escritura)   
   
lista_antifavs = []    
for contacto in agenda:
    if contacto["favorito"] == False:
        lista_antifavs.append(contacto)
        
lista_antifavs.sort(key=lambda x:x["telefono"])
for contacto in lista_antifavs:
    print(f"{contacto["nombre"]} - Telf: {contacto["telefono"]}")