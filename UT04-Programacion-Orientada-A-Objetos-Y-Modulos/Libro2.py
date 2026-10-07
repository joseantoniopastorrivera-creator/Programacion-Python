class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def resumen(self):
        return f"{self.titulo} - {self.autor} - {self.paginas}"


lista_libros = []
libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 600)
libro2 = Libro("El Lazarillo de Tormes", "Anónimo", 150)
libro3 = Libro("Juego de Tronos: A Song of Ice and Fire", "George R. R. Martin", 500)

lista_libros.append(libro1)
lista_libros.append(libro2)
lista_libros.append(libro3)

for libro in lista_libros:
    print(libro.resumen())
