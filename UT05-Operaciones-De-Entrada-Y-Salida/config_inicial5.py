import json

config_inicial = {
    "tema": "oscuro",
    "idioma": "en",
    "autoguardado": True,
    "tamano_fuente": 14,
}

with open("config_app5.json", mode="w", encoding="utf-8") as archivo_escritura:
    json.dump(config_inicial, archivo_escritura, indent=4)
    
with open("config_app5.json", mode="r", encoding="utf-8") as archivo_lectura:
    config_nueva = json.load(archivo_lectura) 
    config_nueva["idioma"] = "ES"

with open("config_app5.json", mode="w", encoding="utf-8") as archivo_escritura_nuevo:
    json.dump(config_nueva, archivo_escritura_nuevo, indent=4)