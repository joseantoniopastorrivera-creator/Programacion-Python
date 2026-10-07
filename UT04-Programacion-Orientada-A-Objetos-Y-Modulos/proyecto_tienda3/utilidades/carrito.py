class Carrito:
    def __init__(self):
        self.mi_carrito=[]
    
    def añadir_productos(self, producto):
        self.mi_carrito.append(producto)
        print(f"{producto.nombre} añadido al carrito.")
        
    def calcular_total(self):
        total = 0
        for producto in self.mi_carrito:
            total += producto.precio
        return total
    
    def mostrar_contenido(self):
        for producto in self.mi_carrito:
            print(f"{producto.nombre} - {producto.precio} euros.")        
            