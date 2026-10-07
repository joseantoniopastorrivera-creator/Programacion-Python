#Autor JAPR
#Fecha 18/02/26
#Ejercicio 2: Diccionarios y bucles

#Cogemos los datos del enunciado
factura = {
    "Laptop": 899.99,
    "Monitor": 299.50,
    "Teclado": 79.99,
    "Ratón": 29.99,
    "Cable HDMI": 12.50
}

# Mostrar precio del Monitor
print(f"Precio Monitor: {factura['Monitor']}")

#Lista Original
print("---LISTA ORIGINAL---")
for producto, precio in factura.items():
    print(f"{producto}:{precio}")

# Añadir Auriculares
factura["Auriculares"] = 149.99

# Modificar precio del Ratón
factura["Ratón"] = 34.99

# Mostrar todos los productos y precios utilizando .items()
print(f"\n--LISTA DE TODOS LOS PRODUCTOS---\n-AURICULARES AÑADIDOS Y PRECIO RATÓN MODIFICADO-")
for producto, precio in factura.items():
    print(f"{producto}: {precio}")

# CalculaMOS total de la factura
total = sum(factura.values())
print(f"\nTotal factura: {total:.2f}")

# Uso de 'get()' para Webcam y mostrar "No disponible"
print(f"\nPrecio Webcam: {factura.get('Webcam', 'No disponible')}")

#Eliminamos el producto "Cable HDMI" y muestra su precio eliminado
precio_eliminado = factura.pop("Cable HDMI")

#Comprobamos que se ha eliminado el producto "Cable HDMI"
print("\n---TODOS LOS PRODUCTOS (SIN CABLE HDMI)---")
for producto, precio in factura.items():
    print(f"{producto}: {precio}")











