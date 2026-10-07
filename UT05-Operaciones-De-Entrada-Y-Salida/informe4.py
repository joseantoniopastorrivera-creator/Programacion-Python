import csv

videojuegos_precio = {}
videojuegos_venta = {}

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
        if producto in videojuegos_venta:
            videojuegos_venta[producto] += unidades_vendidas
        else:
            videojuegos_venta[producto] = unidades_vendidas

# RESULTADOS
producto_top = ""
total_ventas = 0
max_ventas = 0

with open("informe4.txt", mode="w", encoding="utf-8") as archivo_informe:
    archivo_informe.write("---INFORME---")
    for juego, unidades_vendidas in videojuegos_venta.items():
        if unidades_vendidas > max_ventas:
            max_ventas = unidades_vendidas
            producto_top = juego

        precio_unitario = videojuegos_precio[juego]
        ganancia_unitaria_por_juego = precio_unitario * unidades_vendidas
        total_ventas += ganancia_unitaria_por_juego
        archivo_informe.write(
            f"\n{juego} - Ventas: {unidades_vendidas} - Ganancia estimada: {ganancia_unitaria_por_juego}"
        )
    archivo_informe.write(f"\nProducto más vendido: {producto_top}.")
    archivo_informe.write(f"\nTotal ventas: {total_ventas} euros.")