class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular      # público
        self._saldo = saldo         # protegido
        self.__clave = "1234"       # privado

    def mostrar(self):
        print(f"Titular: {self.titular}, Saldo: {self._saldo}")
        
    def cambiar_clave(self, clave_antigua, clave_nueva):
            if clave_antigua == self.__clave:
                self.__clave= clave_nueva
                print("Clave cambiada con éxito.")
            else:
                print("ERROR, la clave antigua no coincide.")    
                
cuenta1 = Cuenta("Paco", 1000)   

cuenta1.cambiar_clave("0000", "4321")
cuenta1.cambiar_clave("1234", "4321")             