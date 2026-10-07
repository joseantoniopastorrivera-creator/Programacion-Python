class GestorBiblioteca:
    def __init__(self, sistema_de_notificaciones):
        self.sistema_de_notificaciones=sistema_de_notificaciones
        self.lista_libros = []
        self.lista_usuarios = []
        
    def agregar_libro(self, libro):
        self.lista_libros.append(libro)
        print(f"{libro.titulo} agregado con éxito a la colección de la biblioteca.")
        
    def registrar_usuario(self, usuario):
        self.lista_usuarios.append(usuario)    
        print(f"Nuevo usuario dado de alta en el sistema: {usuario.nombre}.")
        
    def prestar_libro(self, libro, usuario):
        if libro.disponible:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            mensaje = f"{libro.titulo} prestado correctamente a {usuario.nombre}."
            self.sistema_de_notificaciones.enviar(mensaje, usuario)
        else:
            print("Error, el libro no se encuentra disponible.")     
            
    def devolver_libro(self, libro, usuario):
        if libro in usuario.libros_prestados:
            libro.disponible = True
            usuario.libros_prestados.remove(libro)
            mensaje = f"Libro {libro.titulo} devuelto con éxito por el usuario {usuario.nombre}."
            self.sistema_de_notificaciones.enviar(mensaje, usuario)
        else:
            print(f"Error, el libro {libro.titulo} no había sido prestado al usuario {usuario.nombre}.")  