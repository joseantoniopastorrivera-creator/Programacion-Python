import csv

datos_juegos = [
    ["titulo", "genero", "precio", "stock"],
    ["Celeste", "Plataformas", 19.99, 8],
    ["Hades", "Accion", 24.50, 0],
    ["Stardew Valley", "Simulacion", 14.99, 15],
    ["Portal 2", "Puzzle", 9.99, 6],
    ["Forza Horizon", "Carreras", 39.99, 3],
]

with open(
    "videojuegos4.csv", mode="w", encoding="utf-8", newline=""
) as archivo_escritura:
    escritor = csv.writer(archivo_escritura)
    escritor.writerows(datos_juegos)

print("Archivo videojuegos4.csv creado con éxito.")

with open("videojuegos4.csv", encoding="utf-8", mode="r") as archivo_lectura:
    lector = csv.reader(archivo_lectura)
    next(lector)
    for fila in lector:
        titulo = fila[0]
        precio = float(fila[2])
        stock = int(fila[3])
        if stock > 0 and precio < 30:
            print(f"{titulo} | Precio: {precio} euros | Stock: {stock} uds.")
