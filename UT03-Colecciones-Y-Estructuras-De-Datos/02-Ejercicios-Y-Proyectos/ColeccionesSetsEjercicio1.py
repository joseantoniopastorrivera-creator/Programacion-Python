# --- ENUNCIADO: Operaciones de Conjuntos ---

lista1 = [1, 2, 2, 3, 4, 4, 5]
lista2 = [3, 4, 5, 5, 6, 7, 7, 8]

# 1. Convertir a sets (Elimina duplicados automaticamente)
set1 = set(lista1)
set2 = set(lista2)
print(f"Sets limpios:\n S1: {set1}\n S2: {set2}")

# 2. Interseccion (&) - Numeros comunes
comunes = set1 & set2
print(f"Comunes: {comunes}")

# 3. Diferencia (-) - Solo en lista 1
solo_lista1 = set1 - set2
print(f"Solo en Lista 1: {solo_lista1}")

# 4. Union (|) - Todos los numeros diferentes
union_total = set1 | set2
print(f"Union total (todos los numeros): {union_total}")

# 5. Contar unicos
print(f"Cantidad de numeros unicos en total: {len(union_total)}")