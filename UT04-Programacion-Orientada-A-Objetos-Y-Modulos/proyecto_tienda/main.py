from utilidades import Carrito, Producto, aplicar_descuento

print("Iniciando caja registradora...")
producto1 = Producto("Ordenador", 1000)
producto2 = Producto("Bicicleta", 600)
producto3 = Producto("Redmi 12 Note PRO", 350)

mi_carrito = Carrito()

print("\nEscaneando artículos...")
mi_carrito.añadir_productos(producto1)
mi_carrito.añadir_productos(producto2)
mi_carrito.añadir_productos(producto3)

print("\n")
mi_carrito.mostrar_contenido()


total_compra = mi_carrito.calcular_total()
print(f"\nTotal Sin Descuento: {total_compra} euros.")

total_final = aplicar_descuento(total_compra, 10)
print(f"Total Final: {total_final} euros.")