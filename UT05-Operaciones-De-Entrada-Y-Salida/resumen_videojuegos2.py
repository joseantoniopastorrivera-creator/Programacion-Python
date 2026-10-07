import csv

total_unidades = 0

with open("videojuegos.csv", mode="r", encoding="utf-8") as archivo_csv,\
    open("resumen_inventario2.txt", mode="w", encoding="utf-8") as archivo_txt:
        lector =csv.reader(archivo_csv)
        next(lector)
        for fila in lector:
            titulo = fila[0]
            genero = fila[1]
            precio = fila[2]
            stock = int(fila[3])
            
            archivo_txt.write(f"{titulo} - {genero} - {precio} euros - {stock} unidades.\n")
            total_unidades+=stock
        archivo_txt.write(f"Total stock: {total_unidades}.")    