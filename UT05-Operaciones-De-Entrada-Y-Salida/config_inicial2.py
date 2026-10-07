import json

config_inicial = {
    "tema": "oscuro",
    "idioma": "en",
    "autoguardado": True,
    "tamano_fuente": 14,
}

with open("config_app2.json", mode="w", encoding="utf-8") as archivo_escritura:
    json.dump(config_inicial, archivo_escritura, indent=4)

print("Archivo 'config_app.json' creado correctamente.")

with open("config_app2.json", mode="r", encoding="utf-8") as archivo_lectura:
    config_nueva = json.load(archivo_lectura)

config_nueva["idioma"] = "es"
print(f"Idioma cambiado a: {config_nueva['idioma']}")

with open ("config_app2.json", encoding="utf-8", mode="w") as archivo_escritura_nuevo:
    json.dump(config_nueva, archivo_escritura_nuevo, indent=4)

print("Archivo 'config_app2.json' actualizado y guardado correctamente.")