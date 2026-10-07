import csv
import json

with open("contactos.json", encoding="utf-8", mode="r") as archivo_json:
    agenda = json.load(archivo_json)
    
with open ("contactos5.csv", encoding="utf-8", mode="w", newline="") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(["nombre", "telefono", "favorito"])
    for contacto in agenda:
        escritor.writerow([contacto["nombre"], contacto["telefono"], contacto["favorito"]])  
        
with open("contactos5.csv", mode="r", encoding="utf-8") as archivo_csv_definitivo:
    lector = csv.reader(archivo_csv_definitivo)
    next(lector)
    lista_agenda=list(lector)
    print(f"Total agenda: {len(lista_agenda)}")