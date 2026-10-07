import csv

total_unidades = 0
total_valor_stock = 0

with open("videojuegos.csv", mode = "r", encoding="utf-8") as archivo_csv, \
    open("resumen_inventario3.txt", mode="w", encoding="utf-8") as archivo_txt:
        lector = csv.reader(archivo_csv)
        next(lector)
        for fila in lector:
            titulo = fila[0]
            genero = fila[1]
            precio = float(fila[2])
            stock = int(fila[3])
            
            archivo_txt.write(f"{titulo} - {genero} - {precio} euros - {stock} unidades.\n")
            total_unidades+=stock
            total_valor_stock+=(precio*stock)    
        
        archivo_txt.write(f"Total Stock: {total_unidades} unidades.")
        archivo_txt.write(f"\nValor del inventario: {total_valor_stock:.2f} euros.")    
            
            
            