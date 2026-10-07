from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, cantidad):
        pass
    
class Tarjeta(MetodoPago):
    def pagar(self, cantidad):
        return f"Descontado {cantidad} euros de la tarjeta."    

class PayPal(MetodoPago):
    def pagar(self, cantidad):
        return f"Transferido {cantidad} euros de su cuenta de Paypal."    
    
class Efectivo(MetodoPago):
    def pagar(self, cantidad):
        return f"Recibidos {cantidad} euros en efectivo, pago realizado."
    

total_carrito = 100
pago_tarjeta = Tarjeta()
pago_paypal= PayPal()
pago_efectivo = Efectivo()

print("Procediendo al pago del carrito..")
print(f"Total cantidad a pagar: {total_carrito}")

print(pago_tarjeta.pagar(total_carrito))
print(pago_paypal.pagar(total_carrito))
print(pago_efectivo.pagar(total_carrito))
       
    
        

