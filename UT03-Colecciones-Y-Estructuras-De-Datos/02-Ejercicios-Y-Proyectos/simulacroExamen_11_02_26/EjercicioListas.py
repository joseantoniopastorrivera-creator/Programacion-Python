# Autor: JAPR
# Fecha: 18/02/26
# Simulacro Listas: Juez de Competición


print("--SISTEMA DE PUNTUACIÓN--")

# Captura de datos
notas = []

# Pedimos las 5 notas y las añadimos a la lista con append
for i in range(5):
    puntuacion = float(input(f"Introduce la nota del juez {i+1}:"))
    notas.append(puntuacion)

# Mostramos las notas originales
print(f"-NOTAS ORIGINALES: {notas}-")

# Ordenamos la lista de menor a mayor
notas.sort()

# Borramos la nota del índice 0(la menor)
nota_borrada = notas.pop(0)

# La mejor nota está ahora al final de la lista
mejor_nota = notas[-1]

# Sumamos las notas que quedan en la lista
suma_total = 0
for nota in notas:
    suma_total = suma_total + nota

# Calculamos la media
promedio = suma_total / len(notas)

#Resutados
print("\n--RESULTADOS--")
print(f"Nota eliminada(la más baja): {nota_borrada}")
print(f"Nota más alta: {mejor_nota}")
print(f"Notas válidas: {notas}")
print(f"Nota media final: {round(promedio, 2)}")
