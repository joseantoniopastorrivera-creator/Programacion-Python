from cabina.hardware import Altavoz
from cabina.software import TraktorPRO

print("Encendiendo la cabina..")

#Creamos la dependencia
mis_altavoces = Altavoz()

mi_traktor = TraktorPRO(mis_altavoces)

mi_traktor.mezclar("Charlotte de Witte - Doppler")