import csv

precio_juegos = {}
ventas_por_juego = {}

#Conseguimos los precios de los videojuegos
with open("videojuegos.csv", mode="r", encoding="utf-8") as archivo_videojuegos:
    lector_videojuegos = csv.reader(archivo_videojuegos)
           
    next(lector_videojuegos)
    print("---LISTA DE VIDEOJUEGOS Y PRECIOS---")
    for fila in lector_videojuegos:
        titulo=fila[0]
        precio =float(fila[2])
        precio_juegos[titulo] = precio       
        print(f"{titulo} - {precio} euros.")
                
#Ventas
with open("ventas.csv", mode="r", encoding="utf-8") as archivo_ventas:
    lector_ventas = csv.reader(archivo_ventas)
    
    next(lector_ventas)
    for fila in lector_ventas:
        producto = fila[1]
        unidades_vendidas = int(fila[2]) 
        if producto in ventas_por_juego:
            ventas_por_juego[producto]+=unidades_vendidas
        else:
            ventas_por_juego[producto] = unidades_vendidas  
        
    print("\n---LISTA DE PRODUCTOS Y VENTAS---")    
    for juego, total_unidades in ventas_por_juego.items():
        print(f"{juego} - {total_unidades}")         
                   
            
#Calcular
ingreso_total = 0
producto_top = ""
max_ventas = 0

with open("informe.txt", mode="w", encoding="utf-8") as archivo_informe:
    archivo_informe.write("---INFORME FINAL DE VENTAS---\n")      
    for juego, unidades_vendidas in ventas_por_juego.items():
        if unidades_vendidas > max_ventas:
            max_ventas=unidades_vendidas
            producto_top=juego
    
    archivo_informe.write(f"Producto más vendido: {producto_top} - Ventas: {max_ventas}\n")  
    
    archivo_informe.write("INGRESOS POR PRODUCTO:\n")     
    for juego, unidades_vendidas in ventas_por_juego.items():
        precio_unitario = precio_juegos[juego]
        ingresos_juego = precio_unitario * unidades_vendidas      
        ingreso_total += ingresos_juego
        archivo_informe.write(f"{juego} : {unidades_vendidas} unidades | Ingresos: {ingresos_juego:.2f} euros.\n")
    
    archivo_informe.write(f"Ingresos totales: {ingreso_total} euros.")
       
    print(f"Informe generado con éxito.")       