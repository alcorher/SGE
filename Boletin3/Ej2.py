class CuentaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"{cantidad} depositados. Nuevo saldo: {self.saldo}")
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No tienes tanto dinero")
        else:
            self.saldo -= cantidad
            print(f"{cantidad} retirados. Nuevo saldo: {self.saldo}")

    def consultar(self):
        print(f"Saldo: {self.saldo}")


cuenta1 = CuentaBancaria("Juan Perez", 1000)
cuenta1.consultar()
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.retirar(2000)
cuenta1.consultar()