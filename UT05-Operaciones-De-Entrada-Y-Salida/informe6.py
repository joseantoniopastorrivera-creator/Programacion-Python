import csv

videojuego_precio = {}
videojuego_venta = {}

with open("videojuegos.csv", mode="r", encoding="utf-8") as archivo_videojuegos:
    lector_videojuegos = csv.reader(archivo_videojuegos)
    next(lector_videojuegos)
    for fila in lector_videojuegos:
        titulo = fila[0]
        precio = float(fila[2])
        videojuego_precio[titulo] = precio

with open("ventas.csv", mode="r", encoding="utf-8") as archivo_ventas:
    lector_ventas = csv.reader(archivo_ventas)
    next(lector_ventas)
    for fila in lector_ventas:
        producto = fila[1]
        unidades_vendidas = int(fila[2])
        if producto in videojuego_venta:
            videojuego_venta[producto] += unidades_vendidas
        else:
            videojuego_venta[producto] = unidades_vendidas

max_ventas = 0
total_ventas = 0
producto_top = ""

with open("informe6.txt", mode="w", encoding="utf-8") as archivo_informe:
    archivo_informe.write("---INFORME---")
    for juego, unidades_vendidas in videojuego_venta.items():
        if unidades_vendidas > max_ventas:
            max_ventas = unidades_vendidas
            producto_top = juego
        precio_unitario = videojuego_precio[juego]
        ganancia_por_juego = precio_unitario * unidades_vendidas
        total_ventas += ganancia_por_juego
        archivo_informe.write(f"\n{juego} - Ventas: {unidades_vendidas} - Ganancia estimada: {ganancia_por_juego} euros.")
    archivo_informe.write(f"\nProducto más vendido: {producto_top} con {max_ventas} unidades vendidas.")
    archivo_informe.write(f"\nTotal ventas: {total_ventas} euros.")    
