class CuentaBancaria:
    def __init__(self):
        self.saldo = 0
    
    def depositar(self, cantidad):
        self.saldo += cantidad
    
    def consultar_saldo(self):
        return self.saldo

cuenta = CuentaBancaria()
cuenta.depositar(100)
print(cuenta.consultar_saldo())