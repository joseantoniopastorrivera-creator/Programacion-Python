from abc import ABC, abstractmethod

class Dispositivo(ABC):
    @abstractmethod
    def encender (self):
        pass
    
    def apagar(self):
        pass
    
class Televisor(Dispositivo):
    def encender(self):
        return "Encendiendo el televisor con el mando."
    
    def apagar(self):
        return "Apagando el televisor con el mando."
    
class Altavoz(Dispositivo):
    def encender(self):
        return "Encendiendo el altavoz.."
    
    def apagar (self):
        return "Apagando el altavoz.."
    
televisor1 = Televisor()
altavoz1 = Altavoz()
print(televisor1.encender())
print(televisor1.apagar())
print(altavoz1.encender())
print(altavoz1.apagar())            