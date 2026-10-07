class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def __str__(self):
        return f"Cuenta Bancaria de {self.titular} | Saldo: {self.saldo} euros."    

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print("Ingreso realizado con éxito.")
        else:
            print("Error, introduzca una cantidad mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print(
                "Error, introduzca una cantidad menor o igual que su saldo para poder retirar."
            )
        elif cantidad < 0:
            print("Error, introduzca una cantidad mayor que cero.")
        else:
            self.saldo -= cantidad
            print("Retirada realizada con éxito.")
            
#PRUBAS
cuenta_personal= CuentaBancaria("Jose", 1200)
print(cuenta_personal)
cuenta_personal.ingresar(100)
print(cuenta_personal)
cuenta_personal.retirar(1301)
print(cuenta_personal)
cuenta_personal.retirar(1111)
print(cuenta_personal)
            
