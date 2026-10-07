from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje, destinatario):
        pass
    
class EmailNotificacion(Notificacion):
    def enviar (self, mensaje, destinatario):
        return f"{mensaje} enviado al email: {destinatario}."
    
class SMSNotificacion(Notificacion):
    def enviar(self, mensaje, destinatario):
        return f"{mensaje} enviado al número: {destinatario}."
      