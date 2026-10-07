import csv

precio_videojuegos = {}
ventas_por_videojuego = {}

with open("videojuegos.csv", encoding="utf-8", mode="r") as archivo_videojuegos:
    lector_videojuegos = csv.reader(archivo_videojuegos)
    next(lector_videojuegos)
    for lista in lector_videojuegos:
        titulo = lista[0]
        precio = float(lista[2])
        precio_videojuegos[titulo] = precio

with open("ventas.csv", mode="r", encoding="utf-8") as archivo_ventas:
    lector_ventas = csv.reader(archivo_ventas)
    next(lector_ventas)
    for fila in lector_ventas:
        producto = fila[1]
        unidades_vendidas = int(fila[2])
        if producto in ventas_por_videojuego:
            ventas_por_videojuego[producto] += unidades_vendidas
        else:
            ventas_por_videojuego[producto] = unidades_vendidas

# Resultados
ingreso_total = 0
producto_top = ""
max_ventas = 0

with open("informe2.txt", mode="w", encoding="utf-8") as archivo_informe:
    archivo_informe.write("---INFORME---")

    for juego, unidades_vendidas in ventas_por_videojuego.items():
        if unidades_vendidas > max_ventas:
            max_ventas = unidades_vendidas
            producto_top = juego

        precio_unitario = precio_videojuegos[juego]
        ingreso_por_videojuego = precio_unitario * unidades_vendidas
        ingreso_total += ingreso_por_videojuego
        archivo_informe.write(f"\n{producto} - Ventas: {unidades_vendidas} | Ganancia estimada: {ingreso_por_videojuego}")

    archivo_informe.write(
        f"\nProducto más vendido: {juego} - Unidades vendidas: {max_ventas}"
    )
    archivo_informe.write(f"\nIngreso total estimado: {ingreso_total} euros.")
