def procesar_lista(numeros: list, nuevo: float) -> list:
    """
    Añade `nuevo` al inicio, ordena, elimina el elemento central 
    según fórmula y devuelve la lista.
    """
    
    # 1. Chequear requisitos (Validación)
    if len(numeros) != 5:
        print("Error: La lista debe tener exactamente 5 elementos.")
        return numeros # Devolvemos la lista sin tocar
    
    # Trabajamos sobre una copia para no romper la lista original fuera de la función
    # (Esto es buena práctica, aunque el enunciado no lo pida explícitamente)
    lista_trabajo = numeros.copy()
    
    # 2. Añadir al inicio
    lista_trabajo.insert(0, nuevo)
    
    # 3. Ordenar
    lista_trabajo.sort()
    
    # 4. Eliminar el del medio (fórmula del enunciado)
    # Longitud ahora es 6. (5//2) - 1 = Índice 1.
    indice_medio = (len(lista_trabajo) - 1) // 2 - 1
    
    # Usamos pop para sacar por índice
    if indice_medio >= 0:
        lista_trabajo.pop(indice_medio)
        
    return lista_trabajo

# --- PROBAMOS LA FUNCIÓN ---
lista_inicial = [10, 3, 7, 2, 5]
resultado = procesar_lista(lista_inicial, 8)

print("Lista Original:", lista_inicial) # Se mantiene intacta gracias al .copy()
print("Lista Procesada:", resultado)