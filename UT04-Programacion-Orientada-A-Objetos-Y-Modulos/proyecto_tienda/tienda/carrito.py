class Carrito:
    def __init__(self):
        self.lista_productos = []

    def añadir_productos(self, producto):
        self.lista_productos.append(producto)
        print(f"Producto: {producto.nombre} añadido al carrito")

    def calcular_total(self):
        total = 0
        for producto in self.lista_productos:
            total += producto.precio
        return total

    def mostrar_contenido(self):
        for producto in self.lista_productos:
            print (f"{producto.nombre} - {producto.precio}€")