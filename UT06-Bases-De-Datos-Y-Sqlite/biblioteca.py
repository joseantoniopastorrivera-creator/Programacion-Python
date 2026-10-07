import sqlite3

# Creación de la Base de Datos
conexion = sqlite3.connect("biblioteca.bd")
cursor = conexion.cursor()

# Creamos la tabla
cursor.execute("""create table if not exists libros(
    id integer primary key autoincrement,
    titulo text,
    autor text, 
    anio integer,
    unique (titulo, autor) 
    )""")

conexion.commit()

# Libros de prueba iniciales
libros_prueba = [
    ("1984", "George Orwell", 1949),
    ("Dune", "Frank Herbert", 1965),
    ("Fundación", "Isaac Asimov", 1951),
]

# Inserción inicial
for libro in libros_prueba:
    try:
        cursor.execute(
            "insert into libros (titulo, autor, anio) values (?, ?, ?)", libro
        )
        print(f"Libro {libro[0]} añañdido correctamente.")
    except sqlite3.IntegrityError:
        print(f"ERROR, Libro {libro[0]} de {libro[1]} ya existe en la base de datos.")

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
    print(f"Lote de {len(libros_nuevos)} libros insertado con executemany.")
except sqlite3.IntegrityError:
    print(f"ERROR, Lote insertado anteriormente.")

conexion.commit()

# Consultas parametrizadas de selección
autor_buscar = "Frank Herbert"
anio_minimo = 1960

cursor.execute(
    "select * from libros where autor = ? and anio >= ?", (autor_buscar, anio_minimo)
)
resultados = cursor.fetchall()
for fila in resultados:
    print(f"{fila}")
    
#Actualización y borrado con parámetros
nuevo_anio = 1950
titulo_actualizar = "1984"
cursor.execute("update libros set anio = ? where titulo = ?", (nuevo_anio, titulo_actualizar))
print(f"Libro '{titulo_actualizar}' actualizado al año {nuevo_anio}.")

cursor.execute("delete from libros where titulo = ?", ("1984",))
print("Libro '1984' borrado.")

anio_corte = 1700
cursor.execute("delete from libros where anio < ?", (anio_corte,))
print(f"Libros anteriores a {anio_corte} eliminados.")

conexion.commit()

#Mostrar todos los registros
cursor.execute("select * from libros")

print("Método con fetchall.")
todas_las_filas = cursor.fetchall()
for fila in todas_las_filas:
    print(f"{fila}")
    
cursor.execute("select * from libros")    
print("Método itinerando directamente con el cursor.")    
for fila in cursor:
    print(f"{fila}")
