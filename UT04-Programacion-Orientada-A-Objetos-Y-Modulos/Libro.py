class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def resumen(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Páginas: {self.paginas}"


libro1 = Libro("El Señor de los Anillos", "Tolkien", 650)
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1000)
libro3 = Libro("El Lazarillo de Tormes", "Anónimo", 150)
lista_libros = [libro1, libro2, libro3]

for titulos in lista_libros:
    print(titulos.resumen())
