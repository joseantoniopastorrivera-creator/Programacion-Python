import json

# Tus datos iniciales (que son un diccionario normal y corriente)
config_inicial = {
    "tema": "oscuro",
    "idioma": "en",
    "autoguardado": True,
    "tamano_fuente": 14,
}

# 1. Crear y guardar el archivo JSON
with open("config_app.json", "w", encoding="utf-8") as f:
    json.dump(config_inicial, f)
print("1. Archivo 'config_app.json' creado con el idioma original (en).")

#2. Cargar el JSON y modificar el diccionario
with open("config_app.json", "r", encoding="utf-8") as f:
    config_leida=json.load(f)

config_leida["idioma"] = "es"
print(f"2. Idioma modificado en la memoria a: {config_leida['idioma']}")

#3. Guardar el fichero actualizado
with open("config_app.json", "w", encoding = "utf-8") as f:
    json.dump(config_leida, f)
print("3. Archivo JSON actualizado y guardado con éxito.")