from utilidades import Producto, Carrito, aplicar_descuento

mi_carrito = Carrito()

producto1 = Producto("Casa", 10000)
producto2 = Producto("Camiseta", 15)
producto3 = Producto("Calcetines", 2.5)

print("Iniciando caja registradora..")
mi_carrito.añadir_productos(producto1)
mi_carrito.añadir_productos(producto2)
mi_carrito.añadir_productos(producto3)

print("\nMostrando el contenido del carrito..")
mi_carrito.mostrar_contenido()

print("\nMostrando el total sin descuentos..")
total_sin_descuento=mi_carrito.calcular_total()
print(f"Total sin descuento: {total_sin_descuento} euros.")

print(f"\nAplicando 10% de descuento..")
total_con_descuento = aplicar_descuento(total_sin_descuento, 10)
print(f"Total con descuento: {total_con_descuento} euros.")
