# --- 1. DATOS (Tienes que crear la lista ANTES de usarla) ---
posts = [
    {"user": "ana", "likes": 10},
    {"user": "juan", "likes": 55},
    {"user": "ana", "likes": 30}
]

print("\n--- RETO OPCIONAL: EL GANADOR ---")

# Paso A: Agrupar (Sumar likes por usuario)
# Queremos conseguir algo así: {"ana": 40, "juan": 55}
conteo_likes = {} 

for post in posts:
    usuario = post["user"]
    likes = post["likes"]
    
    # Si el usuario ya existe en nuestro resumen, le sumamos los likes
    if usuario in conteo_likes:
        conteo_likes[usuario] += likes
    # Si es la primera vez que lo vemos, lo creamos
    else:
        conteo_likes[usuario] = likes

# Paso B: Buscar el máximo
usuario_top = ""
max_likes = 0

# Recorremos nuestro diccionario resumen .items() -> (clave, valor)
for usuario, total in conteo_likes.items():
    if total > max_likes:
        max_likes = total
        usuario_top = usuario

print(f"El usuario con más likes es {usuario_top.upper()} con {max_likes} likes.")

print("\n--- RETO OPCIONAL: EL GANADOR ---")

# Paso A: Agrupar (Sumar likes por usuario)
# Queremos conseguir algo así: {"ana": 40, "juan": 55}
conteo_likes = {} 

for post in posts:
    usuario = post["user"]
    likes = post["likes"]
    
    # Si el usuario ya existe en nuestro resumen, le sumamos los likes
    if usuario in conteo_likes:
        conteo_likes[usuario] += likes
    # Si es la primera vez que lo vemos, lo creamos
    else:
        conteo_likes[usuario] = likes

# Paso B: Buscar el máximo
usuario_top = ""
max_likes = 0

# Recorremos nuestro diccionario resumen .items() -> (clave, valor)
for usuario, total in conteo_likes.items():
    if total > max_likes:
        max_likes = total
        usuario_top = usuario

print(f"El usuario con más likes es {usuario_top.upper()} con {max_likes} likes.")