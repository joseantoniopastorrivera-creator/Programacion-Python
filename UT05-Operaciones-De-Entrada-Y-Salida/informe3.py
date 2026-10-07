import csv

videojuegos_precio = {}
videojuegos_ventas = {}

with open("videojuegos.csv", mode="r", encoding="utf-8") as archivo_videojuegos:
    lector_videojuegos = csv.reader(archivo_videojuegos)
    next(lector_videojuegos)
    for fila in lector_videojuegos:
        titulo = fila[0]
        precio = float(fila[2])
        videojuegos_precio[titulo] = precio

with open("ventas.csv", mode="r", encoding="utf-8") as archivo_ventas:
    lector_ventas = csv.reader(archivo_ventas)
    next(lector_ventas)
    for fila in lector_ventas:
        producto = fila[1]
        unidades_vendidas = int(fila[2])
        if producto in videojuegos_ventas:
            videojuegos_ventas[producto] += unidades_vendidas
        else:
            videojuegos_ventas[producto] = unidades_vendidas

# Resultados
producto_top = ""
max_ventas = 0
total_ventas = 0

with open("informe3.txt", mode="w", encoding="utf-8") as archivo_informe:
    archivo_informe.write("---INFORME---")

    for juego, unidades_vendidas in videojuegos_ventas.items():
        if unidades_vendidas > max_ventas:
            max_ventas = unidades_vendidas
            producto_top = juego

        precio_unitario = videojuegos_precio[juego]
        ingreso_por_videojuego = precio_unitario * unidades_vendidas
        total_ventas += ingreso_por_videojuego
        archivo_informe.write(
            f"\n{juego} - Unidades vendidas: {unidades_vendidas} - Ingreso estimado: {ingreso_por_videojuego}"
        )
    archivo_informe.write(f"\nProducto más vendido: {producto_top}.")
    archivo_informe.write(f"\nTotal ventas: {total_ventas} euros.")