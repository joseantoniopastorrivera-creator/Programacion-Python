#Autor JAPR
#Fecha 18/02/26
#Ejercicio 3: Listas de diccionarios

posts = [
    {"user": "ana", "likes": 10, "hashtag": "#python"},
    {"user": "juan", "likes": 55, "hashtag": "#python"},
    {"user": "ana", "likes": 30, "hashtag": "#dev"},
    {"user": "lucas", "likes": 20, "hashtag": "#python"}
]

# Mostramos el total de posts y los usuarios diferentes que hayan publicado
total_posts = len(posts)

#Utilizamos para ello un set ya que no pueden repetir elementos de la colección
usuarios_unicos = len(set(p["user"] for p in posts))

print("---SOLUCIONES---")
#Imprimimos el total de posts
print(f"Total posts: {total_posts}")

#Imprimimos los usuarios únicos desde el set usuarios_unicos
print(f"\nUsuarios diferentes: {usuarios_unicos}")

#  Imprimimos cada post con formato pedido por el enunciado
print("\n")
for persona in posts:
    print(f"usuario: {persona['user']} - likes: {persona['likes']} - hashtag: {persona['hashtag']}")

#Calculamos y mostramos los likes totales de cada usuario, indicando el más popular
print("\n")
#Creamos la pizarra de likes en blanco
pizarra_likes_por_usuario = {}

for persona in posts:
    usuario = persona["user"]
    pizarra_likes_por_usuario[usuario] = pizarra_likes_por_usuario.get(usuario, 0) + persona["likes"]

popular = max(pizarra_likes_por_usuario, key=pizarra_likes_por_usuario.get)
print(f"Likes por usuario: {pizarra_likes_por_usuario}")
print(f"Usuario más popular: {popular} con {pizarra_likes_por_usuario[popular]} likes.")

# Crea un diccionario donde la clave sea el hashtag, el número total de likes recibidos en posts que lo contienen.
# Muestra el hashtag más influyente
print("\n--NUEVO DICCIONARIO 'HASHTAG-LIKES'--")





