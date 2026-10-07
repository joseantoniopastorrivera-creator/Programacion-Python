import csv

lineas_informe = []
total_unidades = 0

#Leer el csv
with open("videojuegos.csv", "r", encoding = "utf-8") as f_csv:
    reader = csv.reader(f_csv)
    
    #Saltamos la cabecera
    next(reader)
    
    for fila in reader:
        titulo = fila[0]
        genero = fila[1]
        stock = int(fila[3])
        
        #Vamos sumando el stock al total
        total_unidades += stock
        
        #Preparamos la frase y la guardamos en nuestra lista
        frase = f"{titulo} - {genero} - {stock} unidades\n"
        lineas_informe.append(frase)
        
with open("resumen_inventario.txt", "w", encoding="utf-8") as f_txt:
    for linea in lineas_informe:
        f_txt.write(linea)
        
    f_txt.write(f"Total de unidades en el inventario: {total_unidades}\n")
    
print("Archivo 'resumen_inventario.txt' generado con éxito.")        