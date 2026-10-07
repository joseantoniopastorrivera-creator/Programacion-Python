class GestorBiblioteca:
    def __init__(self, sistema_notificacion):
        self.lista_libros = []
        self.lista_usuarios = []
        self.notificador = sistema_notificacion

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)
        print(f"{libro.titulo} agregado con éxito.")

    def registrar_usuario(self, usuario):
        self.lista_usuarios.append(usuario)
        print(f"{usuario.nombre} agregado con éxito.")

    def prestar_libro(self, libro, usuario):
        if libro.disponible:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            mensaje = f"Se ha prestado el libro: {libro.titulo} a {usuario.nombre}"
            print(self.notificador.enviar(mensaje, usuario.contacto))
        else:
            print(f"Error, {libro.titulo} ya está prestado a otro usuario.")

    def devolver_libro(self, libro, usuario):
        if libro in usuario.libros_prestados:
            libro.disponible = True
            usuario.libros_prestados.remove(libro)
            mensaje = f"{libro.titulo} devuelto con éxito"
            print(self.notificador.enviar(mensaje, usuario.contacto))
