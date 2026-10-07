# 1. Definimos la lista inicial de 5 números
numeros = [10, 3, 7, 2, 5]
nuevo = 8

# 2. Añadir un número al inicio (índice 0)
numeros.insert(0, nuevo) 
# Ahora la lista es: [8, 10, 3, 7, 2, 5]

# 3. Ordenar la lista (modifica la lista original)
numeros.sort()
# Ahora la lista es: [2, 3, 5, 7, 8, 10]

# 4. Eliminar el elemento del medio
# Usamos la fórmula exacta que da el enunciado (corrigiendo sus paréntesis):
indice_medio = (len(numeros) - 1) // 2 - 1 
# Cálculo: (6 - 1) // 2 - 1  =>  5 // 2 - 1  =>  2 - 1 = 1 (Índice 1)

elemento_borrado = numeros.pop(indice_medio) 
# Elimina el elemento en el índice 1 (que es el número 3)

# 5. Mostrar resultado
print(f"Elemento eliminado: {elemento_borrado}")
print(f"Lista final: {numeros}")