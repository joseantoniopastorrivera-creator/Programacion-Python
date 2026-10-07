import json

# json.dump() - escribir
# json.load() - leer

config_inicial = {
    "tema": "oscuro",
    "idioma": "en",
    "autoguardado": True,
    "tamano_fuente": 14,
}

with open("config_app.json", mode="w", encoding="utf-8") as archivo_escritura:
    json.dump(config_inicial, archivo_escritura, indent=4)

print("Archivo 'config_app.json' creado con la configuración en inglés.")

with open("config_app.json", mode="r", encoding="utf-8") as archivo_lectura:
    config_cargada = json.load(archivo_lectura)

config_cargada["idioma"] = "es"
print(f"Idioma cambiado a : {config_cargada['idioma']}")

with open("config_app.json", mode="w", encoding="utf-8") as archivo_escritura_final:
    json.dump(config_cargada, archivo_escritura_final, indent=4)
    
print("Archivo 'config_app.json' actualizado y guardado correctamente.")    
