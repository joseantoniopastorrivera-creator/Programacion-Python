from abc import ABC, abstractmethod

class HardwareDJ(ABC):
    
    @abstractmethod
    def conectar_software(self):
        pass
    
class DenomSCLive(HardwareDJ):
    def conectar_software(self):
        print("Conectando con DenomSCLive por USB...LISTO")
        
class TarjetaSonido(HardwareDJ):
    def conectar_software(self):
        print("Tarjeta de sonido reconocida en Traktor Pro 4.")  
        
#Zona de pruebas
print("Configurando la cabina..")

#Creamos nuestros objetos
mi_controladora = DenomSCLive()
mi_tarjeta = TarjetaSonido()

#Usamos los métodos
mi_controladora.conectar_software()
mi_tarjeta.conectar_software()        
             