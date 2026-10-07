# --- 1. CONFIGURACION (Diccionario de Riesgos) ---
# Clave: Palabra sospechosa
# Valor: Puntos de riesgo (entero)
diccionario_riesgo = {
    "increible": 5,
    "impactante": 3,
    "milagro": 8,
    "secreto": 4,
    "urgente": 2,
    "viral": 3,
    "jamás": 4
}

# --- 2. ENTRADA DE DATOS ---
titular = input("Introduce el titular de la noticia para analizar: ")

# --- 3. PROCESAMIENTO ---
# Paso A: Convertir a minúsculas para que "Milagro" coincida con "milagro"
titular_minusculas = titular.lower()

# Paso B: Dividir la frase en una lista de palabras sueltas
# "El secreto increíble" -> ["el", "secreto", "increíble"]
lista_palabras = titular_minusculas.split()

# Variables para el resultado
puntuacion_total = 0
palabras_encontradas = [] # Lista para el reto opcional

# Paso C: Recorrer y calcular
for palabra in lista_palabras:
    # Limpiamos signos de puntuacion basicos por si acaso (ej: "milagro!")
    palabra_limpia = palabra.strip(".,!¡?")
    
    # Verificamos si la palabra está en nuestro "diccionario negro"
    if palabra_limpia in diccionario_riesgo:
        # Obtenemos el valor de riesgo
        puntos = diccionario_riesgo[palabra_limpia]
        
        # Sumamos al total
        puntuacion_total += puntos
        
        # Guardamos la palabra y sus puntos para el reporte final
        # La guardamos como tupla (puntos, palabra) para ordenar facil despues
        palabras_encontradas.append((puntos, palabra_limpia))

# --- 4. SALIDA DE RESULTADOS ---
print("\n" + "-"*30)
print(f"ANALISIS DE: '{titular}'")
print("-"*30)
print(f"Riesgo Total: {puntuacion_total}")

# Conclusion basica
if puntuacion_total > 10:
    print("CONCLUSION: ¡PELIGRO! Altamente sospechoso (Clickbait extremo)")
elif puntuacion_total > 0:
    print("CONCLUSION: Precaución. Contiene lenguaje sensacionalista.")
else:
    print("CONCLUSION: Parece un titular neutral.")

# --- 5. RETO OPCIONAL (Detalle y Orden) ---
if puntuacion_total > 0:
    print("\n--- DETALLES DEL RETO ---")
    print("Palabras sospechosas encontradas (Ordenadas por gravedad):")
    
    # Ordenamos la lista. Al poner (puntos, palabra), sort() ordena por puntos.
    # reverse=True hace que salgan primero las mas altas (descendente).
    palabras_encontradas.sort(reverse=True)
    
    for puntos, palabra in palabras_encontradas:
        print(f"- '{palabra.upper()}': suma {puntos} puntos")