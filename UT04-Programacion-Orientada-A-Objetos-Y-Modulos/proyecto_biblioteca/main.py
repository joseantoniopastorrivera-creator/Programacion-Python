from interfaces.notificacion import EmailNotificacion
from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.gestorBiblioteca import GestorBiblioteca

print("Iniciando sistema de gestión de la biblioteca..")

libro1 = Libro("ID1", "Don Quijote de la Mancha", "Miguel de Cervantes", True)
libro2 = Libro("ID2", "El Lazarillo de Tormes", "Anónimo", True)
libro3 = Libro(
    "ID3", "Juego de Tronos: A Song of Ice and Fire", "George R. R. Martin", True
)
usuario1 = Usuario("ID_Usuario1", "Jose", "jose@jose.es")

mi_email = EmailNotificacion()
mi_gestor = GestorBiblioteca(mi_email)

print("\nDando de alta usuario..")
mi_gestor.registrar_usuario(usuario1)

print("\nDando de alta libros en el sistema..")
mi_gestor.agregar_libro(libro1)
mi_gestor.agregar_libro(libro2)
mi_gestor.agregar_libro(libro3)

print("\nIniciando préstamos de libro..")
mi_gestor.prestar_libro(libro1, usuario1)
libro2.disponible = False
mi_gestor.prestar_libro(libro2, usuario1)
mi_gestor.devolver_libro(libro1, usuario1)




