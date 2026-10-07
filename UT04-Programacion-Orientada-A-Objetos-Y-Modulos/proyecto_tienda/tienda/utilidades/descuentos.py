def aplicar_descuento(total, porcentaje):
    rebaja = total * (porcentaje / 100)
    total_final = total - rebaja
    return total_final
