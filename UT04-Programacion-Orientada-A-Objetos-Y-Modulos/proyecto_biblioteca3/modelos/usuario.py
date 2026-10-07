class Usuario:
    def __init__(self, id_usuario, nombre, contacto):
        self.id_usuario=id_usuario
        self.nombre=nombre
        self.contacto=contacto
        self.libros_prestados = []