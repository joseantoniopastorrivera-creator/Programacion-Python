class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular=titular
        self.saldo=saldo
        
    def ingresar(self, cantidad):
        if cantidad <= 0:
            print("Error, introduzca una cantidad mayor que cero.")  
        else:
            self.saldo+=cantidad
            print(f"Ingreso realizado con éxito, su saldo acutal es {self.saldo} euros.")      
            
    def retirar (self, cantidad):
        if cantidad > self.saldo:
            print(f"Error, no puede retirar una cantidad mayor que su saldo actual ({self.saldo} euros.)"
                  )     
        else:
            self.saldo -= cantidad
            print(f"Retirada realizada con éxito, su saldo actual es de {self.saldo} euros.")    
            
mi_cuenta=CuentaBancaria("Jose", 100)    
mi_cuenta.ingresar(10)
mi_cuenta.ingresar(-1)
mi_cuenta.retirar(10)
mi_cuenta.retirar(100)        