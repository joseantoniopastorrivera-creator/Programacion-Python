import csv

ventas_enero = 0
ventas_febrero = 0
ventas_marzo = 0

datos_ventas = [
    ["mes", "producto", "unidades_vendidas"],
    ["Enero", "Celeste", 5],
    ["Enero", "Portal 2", 10],
    ["Febrero", "Hades", 20],
    ["Febrero", "Celeste", 8],
    ["Marzo", "Stardew Valley", 15],
]

with open("ventas2.csv", mode="w", encoding="utf-8", newline="") as archivo_escritura:
    escritor = csv.writer(archivo_escritura)
    escritor.writerows(datos_ventas)

    print("Archivo ventas2.csv creado con éxito.")

with open("ventas2.csv", mode="r", encoding="utf-8") as archivo_lectura:
    lector = csv.reader(archivo_lectura)
    next(lector)
    for fila in lector:
        mes = fila[0]
        producto = fila[1]
        unidades_vendidas = int(fila[2])
        if mes == "Enero":
            ventas_enero += unidades_vendidas
        elif mes == "Febrero":
            ventas_febrero += unidades_vendidas
        elif mes == "Marzo":
            ventas_marzo += unidades_vendidas

print(f"Ventas Enero: {ventas_enero} unidades.")
print(f"Ventas Febrero: {ventas_febrero} unidades.")
print(f"Ventas Marzo: {ventas_marzo} unidades.")

ranking = [
    (ventas_enero, "Enero"),
    (ventas_febrero, "Febrero"),
    (ventas_marzo, "Marzo"),
]

ranking.sort(reverse=True)
mes_top = ranking[0][1]
ventas_top = ranking[0][0]

for venta, mes in ranking:
    print(f"{mes} - {venta} unidades.")