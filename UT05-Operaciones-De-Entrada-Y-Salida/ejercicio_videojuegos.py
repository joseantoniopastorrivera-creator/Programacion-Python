import csv

# Los datos iniciales
datos_juegos = [ 
    ["titulo", "genero", "precio", "stock"], 
    ["Celeste", "Plataformas", 19.99, 8], 
    ["Hades", "Accion", 24.50, 0], 
    ["Stardew Valley", "Simulacion", 14.99, 15], 
    ["Portal 2", "Puzzle", 9.99, 6], 
    ["Forza Horizon", "Carreras", 39.99, 3]
]

#1. Crear el archivo videojuegos.csv y meterle los datos.
with open("videojuegos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(datos_juegos)
    
print("Archivo 'videojuegos.csv' creado con éxito.\n")    

#2. Leer ese mismo archivo e imprimir solo los juegos que se puedan comprar 
# (stock mayor que 0) y que sean baratos (precio menor a 30€).
with open("videojuegos.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    
    #Nos saltamos la primera fila que es la cabecera
    next(reader)
    
    for fila in reader:
        titulo = fila[0]
        precio = float(fila[2])
        stock = int(fila[3])
        
        if stock > 0 and precio < 30:
            print(f"{titulo} | {precio}€ | {stock}")