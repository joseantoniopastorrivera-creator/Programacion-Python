import csv
import json

with open("contactos.json", mode="r", encoding="utf-8") as archivo_json:
    agenda =json.load(archivo_json)
    
with open ("contactos.csv", mode="w", encoding="utf-8", newline="") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    
    escritor.writerow(["nombre", "telefono" ,"favorito"])
    
    for contacto in agenda:
        fila = [contacto["nombre"], contacto["telefono"], contacto["favorito"]]
        escritor.writerow(fila)   
        
with open("contactos.csv", mode="r", encoding="utf-8") as archivo_csv_definitivo:
    lector = csv.reader(archivo_csv_definitivo)
    next(lector)
    contador = 0
    for fila in lector:
         contador+=1
    print(f"Filas totales del 'contactos.csv' sin contar la cabecera: {contador}.")     