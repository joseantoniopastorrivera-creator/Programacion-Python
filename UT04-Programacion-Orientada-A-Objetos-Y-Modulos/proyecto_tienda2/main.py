from utilidades import Producto, Carrito, aplicar_descuento

mi_carrito = Carrito()

producto1 = Producto("Pantalla", 400)
producto2 = Producto("Lámpara", 15)
producto3 = Producto("Vaper", 5)


print("Iniciando caja registradora..")
mi_carrito.añadir_producto(producto1)
mi_carrito.añadir_producto(producto2)
mi_carrito.añadir_producto(producto3)

print("\nMostrando el contenido del carrito..")
mi_carrito.mostrar_contenido()

print("\nCalculando el subtotal..")
total_sin_descuento = mi_carrito.calcular_total()
print(f"Total sin descuento: {total_sin_descuento} euros.")

print(f"Aplicando 10% de descuento..")
total_final=aplicar_descuento(total_sin_descuento, 10)
print(f"Precio final con descuento aplicado: {total_final} euros.")





