class Carrito:
    lista_carrito = []
    
    def añadir_productos(self, producto):
        self.lista_carrito.append(producto)
        print(f"{producto.nombre} con precio {producto.precio} euros añadido al carrito de compra.")
        
    def calcular_total(self):
        total = 0
        for producto in self.lista_carrito:
            total += producto.precio
        return total
        
    def mostrar_contenido(self):
        for producto in self.lista_carrito:
            return f"{producto.nombre} - {producto.precio} euros." 
            
                
                