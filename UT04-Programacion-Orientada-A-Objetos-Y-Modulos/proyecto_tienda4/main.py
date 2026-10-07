from utilidades import Producto, Carrito, aplicar_descuentos

mi_carrito = Carrito()

producto1 = Producto("Ratón", 10)
producto2 = Producto("Teclado", 30)
producto3 = Producto("USB", 20)

print("Iniciando caja registradora..")
mi_carrito.añadir_productos(producto1)
mi_carrito.añadir_productos(producto2)
mi_carrito.añadir_productos(producto3)

print("\nMostrando el contenido del carrito..")
mi_carrito.mostrar_contenido()

print("\nCalculando el total sin descuentos..")
total_sin_descuentos = mi_carrito.calcular_total()
print(f"Total sin descuentos: {total_sin_descuentos} euros.")

print(f"\nTotal con descuento del 10% aplicado..")
total_con_descuento=aplicar_descuentos(total_sin_descuentos, 10)
print(total_con_descuento)
    