from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, cantidad):
        pass
    
class Tarjeta(MetodoPago):
    def pagar(self, cantidad):
        return f"Procesando pago de {cantidad} euros con tarjeta.."    
    
class PayPal(MetodoPago):
    def pagar(self, cantidad):
        return f"Procensando pago de {cantidad} desde su cuenta de PayPal.."
    
class Efectivo(MetodoPago):
    def pagar(self, cantidad):
        return f"Procesando pago de {cantidad} con efectivo.."
    
mi_carrito = 100
mi_tarjeta = Tarjeta()
mi_PayPal = PayPal()
mi_efectivo= Efectivo()
print(mi_tarjeta.pagar(mi_carrito))
print(mi_PayPal.pagar(mi_carrito))
print(mi_efectivo.pagar(mi_carrito))
          
    
    