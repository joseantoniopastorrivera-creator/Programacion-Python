
persona = {
    "nombre" : "Luis",
    "edad" : 30,
    "ciudad" : "Granada"
}

print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])
print(persona)
print(persona.keys())
print(persona.values())
print(persona.items())

#'del' borra un campo de la 
del persona["edad"]
print(persona)

#'k' de key 'v' de value
for k, v in persona.items():
    print(f"La clave es {k} y el valor es {v}")

