from interfaces.notificacion import SMSNotificacion, EmailNotificacion
from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.gestorBiblioteca import GestorBiblioteca

mi_mensaje_SMS = SMSNotificacion()
mi_gestor_SMS = GestorBiblioteca(mi_mensaje_SMS)

mi_mensaje_Email = EmailNotificacion()
mi_gestor_Email = GestorBiblioteca(mi_mensaje_Email)

libro1 = Libro("ID1", "Don Quijote de la Mancha", "Miguel de Cervantes", True)
libro2 = Libro("ID2", "El Lazarillo de Tormes", "Anónimo", True)
libro3 = Libro(
    "ID3", "Juego de Tronos: A Song of Ice and Fire", "George R. R. Martin", True
)
usuario_Email = Usuario("ID_Usuario1", "Jose", "jose@jose.es")
usuario_SMS = Usuario("ID_Usuario2", "Paco", "666-666-666")

mi_gestor_SMS.registrar_usuario(usuario_SMS)
mi_gestor_Email.registrar_usuario(usuario_Email)

mi_gestor_SMS.agregar_libro(libro1)
mi_gestor_SMS.agregar_libro(libro2)
mi_gestor_Email.agregar_libro(libro3)

mi_gestor_SMS.prestar_libro(libro1, usuario_SMS)
mi_gestor_Email.prestar_libro(libro2, usuario_Email)
libro3.disponible=False
mi_gestor_SMS.prestar_libro(libro3, usuario_SMS)
mi_gestor_Email.prestar_libro(libro3, usuario_Email)
mi_gestor_SMS.devolver_libro(libro1, usuario_SMS)
mi_gestor_Email.devolver_libro(libro2, usuario_Email)
mi_gestor_SMS.devolver_libro(libro3, usuario_SMS)
mi_gestor_Email.devolver_libro(libro3, usuario_Email)


