import json

config_inicial = {
    "tema": "oscuro",
    "idioma": "en",
    "autoguardado": True,
    "tamano_fuente": 14,
}

with open("config_app3.json", mode="w", encoding="utf-8") as archivo_escritura:
    json.dump(config_inicial, archivo_escritura, indent=4)

with open("config_app3.json", encoding="utf-8", mode="r") as archivo_lectura:
    config_nueva = json.load(archivo_lectura)
    config_nueva["idioma"] = "es"
    
with open("config_app3.json", mode="w", encoding="utf-8") as archivo_escritura_final:
    json.dump(config_nueva, archivo_escritura_final, indent=4)    
