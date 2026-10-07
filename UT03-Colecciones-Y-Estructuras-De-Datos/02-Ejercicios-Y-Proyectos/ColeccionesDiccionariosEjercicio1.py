# --- ENUNCIADO: Gestion de una factura ---

factura = {
    "Laptop": 899.99,
    "Monitor": 299.50,
    "Teclado": 79.99,
    "Raton": 29.99,
    "Cable HDMI": 12.50
}

# 1. Acceder al precio del Monitor
# Usamos acceso directo porque sabemos que existe
precio_monitor = factura["Monitor"]
print(f"1. El precio del Monitor es: {precio_monitor} euros")

# 2. Añadir nuevo producto (Auriculares)
factura["Auriculares"] = 149.99
print(f"2. Auriculares añadidos.")

# 3. Modificar precio del Raton (Sobrescritura)
factura["Raton"] = 34.99
print(f"3. Precio del Raton actualizado.")

# 4. Iterar usando .items() (Formato clave => valor)
print("\n--- LISTA DE PRODUCTOS ---")
for producto, precio in factura.items():
    print(f"- {producto}: {precio} euros")

# 5. Calcular total usando .values()
# .values() nos da una lista con [899.99, 299.50, ...], sum() lo suma todo
total_factura = sum(factura.values())
# Redondeamos a 2 decimales para que quede bonito
print(f"\n5. Total de la factura: {round(total_factura, 2)} euros")

# 6. Uso seguro de .get()
# Buscamos "Webcam", como no esta, devuelve el segundo valor
precio_webcam = factura.get("Webcam", "No disponible")
print(f"6. Precio Webcam: {precio_webcam}")

# 7. Eliminar producto con .pop()
# .pop() borra la clave y nos guarda el valor en la variable
precio_eliminado = factura.pop("Cable HDMI")
print(f"7. Hemos eliminado el Cable HDMI que costaba: {precio_eliminado} euros")

# Comprobacion final
print(f"\nDiccionario final: {factura}")