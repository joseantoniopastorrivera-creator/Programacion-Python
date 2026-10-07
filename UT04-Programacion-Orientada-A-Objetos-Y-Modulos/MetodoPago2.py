from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, cantidad):
        pass
    
class Tarjeta(MetodoPago):
    def pagar(self, cantidad):
        return f"Descontando {cantidad} euros de la tarjeta."
    
class PayPal(MetodoPago):
    def pagar(self, cantidad):
        return f"Descontando {cantidad} de la cuenta de PayPal."
    
class Efectivo(MetodoPago):
    def pagar (self, cantidad):
        return f"Recibidos {cantidad} euros en efectivo, pago procesado."
    
#Pruebas
total_carrito = 100
pago_tarjeta=Tarjeta()
pago_paypal=PayPal()
pago_efectivo=Efectivo()

print("Zona de procesamiento de pagos..")
print(f"Total a pagar: {total_carrito}")   
print(pago_tarjeta.pagar(total_carrito))
print(pago_efectivo.pagar(total_carrito))
print(pago_paypal.pagar(total_carrito))           