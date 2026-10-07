import csv

# Datos iniciales
datos_juegos = [
    ["titulo", "genero", "precio", "stock"],
    ["Celeste", "Plataformas", 19.99, 8],
    ["Hades", "Accion", 24.50, 0],
    ["Stardew Valley", "Simulacion", 14.99, 15],
    ["Portal 2", "Puzzle", 9.99, 6],
    ["Forza Horizon", "Carreras", 39.99, 3],
]

# Creamos y escribimos el archivo.csv
with open(
    "videojuegos2.csv", mode="w", encoding="utf-8", newline=""
) as archivo_escritura:
    escritor = csv.writer(archivo_escritura)
    escritor.writerows(datos_juegos)
    
print("Archivo videojuegos2.csv creado con éxito.\n")   

#Leer y filtrar el archivo.csv
print("Juegos disponibles con stock > 0 y precio > 30 euros.")
with open("videojuegos2.csv", mode="r", encoding="utf-8") as archivo_lectura:
    lector = csv.reader(archivo_lectura)
    
    #Saltamos primera línea al ser la cabecera
    next(lector)
    for fila in lector:
        titulo = fila[0]
        precio = float(fila[2])
        stock = int(fila[3])
        
        #Añadimos el filtro pedido por el ejercicio
        if stock > 0 and precio<30:
            print(f"{titulo} | Precio: {precio} euros | Stock: {stock}")
        
 
