from abc import ABC, abstractmethod


class Dispositivo(ABC):
    @abstractmethod
    def encender(self):
        pass
    
    @abstractmethod
    def apagar(self):
        pass
    
class Televisor(Dispositivo):
   
    def encender(self):
        return "Encendiendo televión con el mando."  
    
    def apagar(self):
        return "Apagando televisión con el mando."


class Altavoz(Dispositivo):
    def encender(self):
        return "Encendiendo altavoz con el interruptor."
    
    def apagar(self):
        return "Apagando altavoz con el interruptor."
    
#Pruebas
televisor1 = Televisor()
televisor2=Televisor()
altavoz1= Altavoz()
lista_dispositivos=[televisor1, televisor2, altavoz1]
for dispositivo in lista_dispositivos:
    print(dispositivo.encender())
    print(dispositivo.apagar())
    
