#Autor: JAPR
#Fecha: 27/01/26
#Mini-proyecto 1 — Social Media Analytics

#Crear una lista con 3 publicaciones. Cada una debe tener un usuario y número de “likes”
posts = [
    {"user": "jose", "likes": 10},
    {"user": "ivan", "likes": 20},
    {"user": "antonio", "likes": 15}
]

#Mostrar cuántos posts hay en total
#Opción A directa
print(len(posts))

#Opción B (con texto)
total = len(posts)
print(f"Hay un total de {total} posts.")

#Recorrer todos los posts e imprimir cada uno en el siguiente formato:
# usuario: ana - likes: 10
for post in posts:
    print(f"usuario: {post['user']} - likes: {post['likes']}")

#Contar los likes totales que tiene el usuario “ana”. Pista:
#Inicializar un acumulador: total = 0
#Si post["user"] == "ana" entonces sumar sus likes.

#Salida resultado:
#Resumen de likes por usuario:
#ana: 40 likes
#juan: 55 likes
total_ivan = 0
for post in posts:
    if post["user"] == "ivan":
        total_ivan += post["likes"]
print(f"ivan: {total_ivan} likes")

total_antonio = 0
for post in posts:
    if post["user"] == "antonio":
        total_antonio += post["likes"]
print(f"antonio: {total_antonio} likes")

total_jose = 0
for post in posts:
    if post["user"] == "jose":
        total_jose += post["likes"]
print(f"jose: {total_jose} likes")

#Mostrar el resumen de likes y el usuario con más likes
print("\nResumen de likes por usuario:")
print("-" * 30)

#Agrupamos y creamos el diccionario resumen
conteo_global = {}
for post in posts:
    usuario = post["user"]
    likes = post["likes"]

#Si el usuario ya existe en nuestra tabla, le sumamos los likes
    if usuario in conteo_global:
        conteo_global[usuario] += likes
#Si el usuario es nuevo, lo creamos
    else:
         conteo_global[usuario] = likes

#Imprimimos el resumen
for usuario, total in conteo_global.items():
    print(f"{usuario}: {total} likes")

#Encontramos al ganador con más likes
usuario_top = ""
max_likes = 0

for usuario, total in conteo_global.items():
    if total > max_likes:
        max_likes = total
        usuario_top = usuario

print("\nUsuario más popular:")
print(f"{usuario_top} con {max_likes} likes totales")