def aplicar_descuento(total, porcentaje):
    descuento = total * porcentaje / 100
    total_carrito_con_descuento = total - descuento
    return total_carrito_con_descuento