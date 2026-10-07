def aplicar_descuentos(total, porcentaje):
    descuento = total * porcentaje /100
    total_con_descuento = total - descuento
    return total_con_descuento