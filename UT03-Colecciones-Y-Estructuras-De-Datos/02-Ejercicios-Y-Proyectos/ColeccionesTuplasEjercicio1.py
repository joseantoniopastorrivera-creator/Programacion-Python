# --- ENUNCIADO: Desempaquetado y Mutabilidad ---

def obtener_punto():
    return (3.5, 4.2, "Punto A")

# 1. Desempaquetar
x, y, nombre = obtener_punto()
print(f"1. Desempaquetado: El {nombre} esta en ({x}, {y})")

# 2. Intentar modificar (Demostracion del error)
tupla_original = obtener_punto()
try:
    tupla_original[0] = 5
except TypeError as e:
    print(f"2. Error esperado capturado: {e}")
    print("   (No se puede asignar items a una tupla)")

# 3. Truco de conversion (Tupla -> Lista -> Tupla)
lista_temp = list(tupla_original) # Convertir a lista
lista_temp.append("Coordenada Z") # Añadir
tupla_modificada = tuple(lista_temp) # Volver a tupla
print(f"3. Tupla modificada: {tupla_modificada}")

# 4. Count e Index
tupla_nums = (1, 2, 1, 3, 1)
primer_uno = tupla_nums.index(1) # Posicion del primer 1
total_unos = tupla_nums.count(1) # Cuantos 1 hay
print(f"4. El numero 1 aparece {total_unos} veces. La primera en indice {primer_uno}.")