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

#Crear y escribir el archivo.csv
with open(
    "videojuegos.csv", mode="w", newline="", encoding="utf-8"
) as archivo_escritura:
    escritor = csv.writer(archivo_escritura)
    escritor.writerows(datos_juegos)

print("Archivo 'videojuegos.csv' creado correctamente.\n")

#Leer y filtrar el archivo.csv
with open("videojuegos.csv", mode = "r", encoding="utf-8") as archivo_lectura:
    lector = csv.reader(archivo_lectura)
    
    #Saltamos primera fila porque es la cabecera
    next(lector)
    
    #Recorremos el resto de líneas una a una
    for fila in lector:
        titulo = fila[0]
        #Al leer un .csv todo llega como cadena de texto, por eso convertimos a número para poder usar < o >
        precio = float(fila[2])
        stock = int(fila[3])
        
        #Aplicamos el filtro pedido por el ejercicio
        if stock > 0 and precio < 30:
            print(f"{titulo} | Precio: {precio} euros. | Stock: {stock} uds")
