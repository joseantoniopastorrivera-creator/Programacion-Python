from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje, usuario):
      pass
        
class EmailNotificacion(Notificacion):
    def enviar(self, mensaje, usuario):
        print(f"Enviando Email a {usuario.nombre}: {mensaje}")
        
class SMSNotificacion(Notificacion):
    def enviar(self, mensaje, usuario):
        print(f"Enviando SMS a {usuario.nombre}: {mensaje}")
                        