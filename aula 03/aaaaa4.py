class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor

    def extrato(self):
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)

conta1 = ContaBancaria("Ana", 1000.0)

conta1.depositar(500.0)
conta1.sacar(200.0)
conta1.sacar(2000.0)   # Saldo insuficiente
conta1.extrato()       # Titular: Ana
                       # Saldo: 1300.0
