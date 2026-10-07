from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje, destinatario):
        pass
    
class EmailNotificacion(Notificacion):
    def enviar(self, mensaje, destinatario):
        print(f"Enviando email a {destinatario}: {mensaje}")
        
class SMSNotificacion(Notificacion):
    def enviar (self, mensaje, destinatario):
        print(f"Enviando SMS a {destinatario}: {mensaje}")            