def aplicar_descuento(total, porcentaje):
    descuento = total * porcentaje / 100
    total_final = total - descuento
    return total_final