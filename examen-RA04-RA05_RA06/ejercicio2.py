import csv
import json

datos_csv = [
    ["actividad", "instructor", "plazas", "precio"],
    ["Yoga", "Laura", 15, 12.00],
    ["Spinning", "Pedro", 20, 10.00],
    ["Pilates", "Laura", 12, 14.00],
    ["Zumba", "María", 25, 8.00],
    ["CrossFit", "Pedro", 10, 18.00],
]

with open(
    "clases_gym.csv", mode="w", newline="", encoding="utf-8"
) as archivo_escritura_csv:
    escritor_csv = csv.writer(archivo_escritura_csv)
    escritor_csv.writerows(datos_csv)

with open("clases_gym.csv", mode="r", encoding="utf-8") as archivo_lectura_csv:
    lector_csv = csv.DictReader(archivo_lectura_csv)
    for fila in lector_csv:
        plazas = int(fila["plazas"])
        precio = float(fila["precio"])
        if plazas > 12 and precio < 15.00:
            print(f"Actividad: {fila['actividad']} - Instructor: {fila['instructor']}")

config = {
    "nombre_gym": "FitZone",
    "horario_apertura": "07:00",
    "horario_cierre": "22:00",
    "numero_vestuarios": 4,
}

with open("config_gym.json", mode="w", encoding="utf-8") as archivo_escritura_json:
    json.dump(config, archivo_escritura_json, indent=4)

with open("config_gym.json", mode="r", encoding="utf-8") as archivo_lectura_json:
    datos_json = json.load(archivo_lectura_json)
    datos_json["horario_cierre"] = "23:00"

with open(
    "config_gym.json", mode="w", encoding="utf-8"
) as archivo_escritura_json_final:
    json.dump(datos_json, archivo_escritura_json_final, indent=4)


print(datos_json)


total_plazas = 0
with open("clases_gym.csv", mode="r", encoding="utf-8") as archivo_lectura, open(
    "resumen_clases.txt", mode="w", encoding="utf-8"
) as archivo_escritura:
    lector = csv.DictReader(archivo_lectura)
    for fila in lector:
        plazas = int(fila["plazas"])
        total_plazas += plazas
        archivo_escritura.write(
            f"{fila['actividad']} - {fila['instructor']} - {fila['plazas']}\n"
        )
    archivo_escritura.write(f"Total plazas disponibles: {total_plazas}")
    