import csv

# Los datos iniciales
datos_ventas = [
    ["mes", "producto", "unidades_vendidas"],
    ["Enero", "Celeste", 5],
    ["Enero", "Portal 2", 10],
    ["Febrero", "Hades", 20],
    ["Febrero", "Celeste", 8],
    ["Marzo", "Stardew Valley", 15],
]

# Escribir el csv
with open("ventas.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(datos_ventas)
print("Archivo 'ventas.csv' creado.")

ventas_por_mes = {}

with open("ventas.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    # Saltamos la cabecera
    next(reader)

    for fila in reader:
        mes = fila[0]
        unidades = int(fila[2])

        # Si el mes ya existe en nuestro diccionario le sumamos las unidades
        if mes in ventas_por_mes:
            ventas_por_mes[mes] += unidades
        else:
            ventas_por_mes[mes] = unidades

# Resultados
print("--Resumen resultados--")
mes_top = ""
ventas_top = 0

# Recorremos el diccionario mes a mes
for mes in ventas_por_mes:
    unidades_del_mes = ventas_por_mes[mes]

    if unidades_del_mes > ventas_top:
        ventas_top = unidades_del_mes
        mes_top = mes

print(f"El mes con más ventas fue: {mes_top} ({ventas_top} unidades)")


# Hacemos el ranking
print("\nRanking:")
lista_para_ordenar = []
for mes in ventas_por_mes:
    lista_para_ordenar.append([unidades, mes])

    lista_para_ordenar.sort(reverse=True)

    # Imprimimos
    posicion = 1
    for elemento in lista_para_ordenar:
        unidades = elemento[0]
        mes = elemento[1]

        print(f"{posicion} - {mes}: {unidades} unidades")
        posicion += 1
