class GestorBiblioteca:
    def __init__(self, sistema_notificaciones):
        self.sistema_notificaciones = sistema_notificaciones
        self.lista_libros = []
        self.lista_usuarios = []

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)
        print(f"{libro.titulo} agregado con éxito a la colección.")

    def registrar_usuario(self, usuario):
        self.lista_usuarios.append(usuario)
        print(f"{usuario.nombre} añadido con éxito.")

    def prestar_libro(self, libro, usuario):
        if libro.disponible:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            mensaje = f"{libro.titulo} prestado con éxito a {usuario.nombre}."
            self.sistema_notificaciones.enviar(mensaje, usuario.contacto)
        else:
            print(f"El libro {libro.titulo} no se encuentra disponible actualmente.")

    def devolver_libro(self, libro, usuario):
        if libro in usuario.libros_prestados:
            libro.disponible = True
            usuario.libros_prestados.remove(libro)
            mensaje = f"Libro {libro.titulo} devuelto con éxito."
            self.sistema_notificaciones.enviar(mensaje, usuario.contacto)
        else:
            print(
                f"El usuario {usuario.nombre} no tenía el libro {libro.titulo} entre sus préstamos. "
            )
