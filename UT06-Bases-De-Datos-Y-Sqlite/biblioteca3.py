import sqlite3

#Creacion de la bbdd
conexion = sqlite3.connect("biblioteca3.bd")
cursor = conexion.cursor()

#Creamos la tabla
cursor.execute("""create table if not exists libros(
    id integer primary key autoincrement,
    titulo text,
    autor text, 
    anio integrer,
    unique (titulo, autor) 
    )""")

conexion.commit()

libros_prueba = [
    ("1984", "George Orwell", 1949),
    ("Dune", "Frank Herbert", 1965),
    ("Fundación", "Isaac Asimov", 1951),
]

for libro in libros_prueba:
    try:
        cursor.execute("insert into libros (titulo, autor, anio) values (?,?,?)", libro)
        print(f"Libro {libro[0]} insertado con éxito.")
    except sqlite3.IntegrityError:      
        print(f"ERROR, Libro {libro[0]} ya existe en el sistema.")
        
conexion.commit()

libros_nuevos = [
    ("El Quijote", "Cervantes", 1605),
    ("Cien años de soledad", "García Márquez", 1967),
    ("La sombra del viento", "Zafón", 2001),
]

try:
    cursor.executemany("insert into libros (titulo, autor, anio) values (?,?,?)", libros_nuevos)
    print("Lista de libros insertada con éxito.")
except sqlite3.IntegrityError:
    print("ERROR, lista de libros insertada anteriormente.")

conexion.commit()

autor_buscar = "George Orwell"
anio_minimo = 1900
cursor.execute("select * from libros where autor = ? and anio >= ?", (autor_buscar, anio_minimo))
resultados = cursor.fetchall()
for fila in resultados:
    print(f"{fila}")    

nuevo_anio = 1950    
titulo_actualizar = "1984"
cursor.execute("update libros set anio = ? where titulo = ?", (nuevo_anio, titulo_actualizar))

cursor.execute("delete from libros where titulo = ?", ("1984",))
cursor.execute("delete from libros where anio <= =", (anio_minimo,))

conexion.commit()   

cursor.execute("select * from libros")
registros = cursor.fetchall()
for lista in registros:
    print(f"{registros}")
    
cursor.execute("select * from libros")
for fila in cursor:
    print(f"{fila}")
                                                          


