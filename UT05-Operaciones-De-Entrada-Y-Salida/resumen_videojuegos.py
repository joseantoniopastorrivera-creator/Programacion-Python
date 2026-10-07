import csv

total_unidades = 0

print("Generando resumen del inventario..")

with open("videojuegos.csv", mode="r", encoding="utf-8") as archivo_csv, \
    open("resumen_inventario.txt", mode="w", encoding="utf-8") as archivo_txt:
    
    lector = csv.reader(archivo_csv)
    next(lector)
    for fila in lector:
        titulo = fila[0]
        genero = fila[1]
        precio = fila[2]
        #Lo convertimos para poder sumarlo con la calculadora
        stock = int(fila[3])
        
        archivo_txt.write(f"{titulo} - {genero} - {precio} - {stock} unidades\n")
        total_unidades+=stock
    archivo_txt.write(f"Total unidades en el inventario: {total_unidades}.")    
    print("Tu archivo resumen_inventario.txt ha sido generado con éxito.")