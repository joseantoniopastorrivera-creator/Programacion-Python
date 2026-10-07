# --- 1. DATOS DE ENTRADA ---

# Gustos del usuario (SET: sin orden, sin repetidos)
gustos_usuario = {"Acción", "Sci-Fi"}

# Catálogo de películas (LISTA de TUPLAS)
# Cada tupla es: ("Título", {Set de Géneros})
peliculas = [
    ("Matrix", {"Sci-Fi"}),
    ("Titanic", {"Romance"}),
    ("Avatar", {"Acción", "Sci-Fi"}),
    ("Gladiator", {"Acción", "Drama"}), # Añado una extra para probar
    ("Notting Hill", {"Romance", "Comedia"})
]

# --- 2. LÓGICA DE FILTRADO ---

print(f"El usuario busca géneros: {gustos_usuario}\n")

# Creamos una lista vacía para guardar las recomendaciones
# (Necesario para el reto de ordenar después)
recomendaciones = []

for titulo, generos_pelicula in peliculas:
    # LA MAGIA DE LOS SETS: Intersección (&)
    # Crea un set nuevo solo con los géneros que coinciden
    coincidencias = gustos_usuario & generos_pelicula
    
    # Si el set de coincidencias NO está vacío, hay match
    # Pista del enunciado: if coincidencias != set():
    if len(coincidencias) > 0:
        print(f"Match encontrado: '{titulo}' (Coincide en: {coincidencias})")
        recomendaciones.append(titulo)

# --- 3. RETO OPCIONAL: ORDENAR Y MOSTRAR ---
print("-" * 30)
print("RESULTADOS FINALES (Ordenados A-Z):")

# Ordenamos la lista alfabéticamente
recomendaciones.sort()

for peli in recomendaciones:
    print(f"Te puede gustar: {peli}")