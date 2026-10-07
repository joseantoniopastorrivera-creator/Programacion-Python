from utilidades.producto import Producto
from utilidades.carrito import Carrito
from utilidades.descuentos import aplicar_descuento

mi_carrito = Carrito()
producto1 = Producto("Pantalla", 400)
producto2 = Producto("Ratón", 20)
producto3 = Producto("Teclado", 50)

mi_carrito.añadir_productos(producto1)
mi_carrito.añadir_productos(producto2)
mi_carrito.añadir_productos(producto3)

mi_carrito.mostrar_contenido()

total_sin_descuento = mi_carrito.calcular_total()
print(f"Total sin descuento: {total_sin_descuento} euros.")

print(f"Aplicando un 10% de descuento..")
total_con_descuento = aplicar_descuento(total_sin_descuento, 10)
print(f"Total con descuento: {total_con_descuento} euros.")