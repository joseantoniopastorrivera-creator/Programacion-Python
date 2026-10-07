import sqlite3

# Creación de la base de datos
conexion = sqlite3.connect("biblioteca2.bd")
cursor = conexion.cursor()

# Creamos la tabla
cursor.execute("""create table if not exists libros(
    id integer primary key autoincrement,
    titulo text,
    autor text, 
    anio integrer,
    unique (titulo, autor) 
)""")

conexion.commit()

# Libros de prueba iniciales
libros_prueba = [
    ("1984", "George Orwell", 1949),
    ("Dune", "Frank Herbert", 1965),
    ("Fundación", "Isaac Asimov", 1951),
]

# Insertamos los tres libros de prueba iniciales
for libro in libros_prueba:
    try:
        cursor.execute("insert into libros (titulo, autor, anio) values (?,?,?)", libro)
        print(f"Libro {libro[0]} insertado con éxito.")
    except sqlite3.IntegrityError:
        print(
            f"Error, el libro {libro[0]} de {libro[1]} ya existe en la base de datos."
        )

conexion.commit()

# Inserción con listas y executemany
libros_nuevos = [
    ("El Quijote", "Cervantes", 1605),
    ("Cien años de soledad", "García Márquez", 1967),
    ("La sombra del viento", "Zafón", 2001),
]

try:
    cursor.executemany(
        "insert into libros (titulo, autor, anio) values (?,?,?)", libros_nuevos
    )
    print("Lista de libros insertada correctamente con executemany.")
except sqlite3.IntegrityError:
    print(f"Error, lista de libros ya insertada.")
    
conexion.commit()

#Consultas parametrizadas de selección
autor_buscar = "Cervantes"
anio_minimo = 1700

cursor.execute("select * from libros where autor = ? and anio >= ?", (autor_buscar, anio_minimo))
resultados = cursor.fetchall()
for fila in resultados:
    print(f"{fila}")
    
#Actualización y borrado con parámetros
nuevo_anio = 1950
titulo_actualizar = "1984"
cursor.execute("update libros set anio = ? where titulo = ?", (nuevo_anio, titulo_actualizar))
print(f"El libro {titulo_actualizar} ha sido actualizado al año {nuevo_anio}.")

cursor.execute("delete from libros where titulo = ?", ("1984",))    
anio_corte = 1800
cursor.execute("delete from libros where anio < ?", (anio_corte,))

conexion.commit()

#Mostrar todos los registros
cursor.execute("select * from libros")
todas_las_filas = cursor.fetchall()
for fila in todas_las_filas:
    print(f"{fila}")
    
cursor.execute("select * from libros")    
for fila in cursor:
    print(f"{fila}")    