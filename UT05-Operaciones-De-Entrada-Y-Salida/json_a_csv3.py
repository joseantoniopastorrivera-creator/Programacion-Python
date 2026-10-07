import csv
import json

with open("contactos3.json", mode="r", encoding="utf-8") as archivo_json:
    agenda = json.load(archivo_json)
    
with open ("contactos3.csv", mode="w", encoding="utf-8", newline="") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(["nombre", "telefono", "favorito"])
    for contacto in agenda:
        escritor.writerow([contacto["nombre"], contacto["telefono"], contacto["favorito"]])   
        
with open ("contactos3.csv", mode="r", encoding="utf-8") as archivo_csv_definitivo:
    lector = csv.reader(archivo_csv_definitivo)
    contador=0
    next(lector)
    for contacto in lector:
        contador+=1    
    print(f"Contactos en la agenda: {contador}.")    
              