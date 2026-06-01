class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Erro: valor de deposito deve ser positivo")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Erro: saldo insuficiente")

    def extrato(self):
        print(f"Titular: {self.__titular} | Saldo: R$ {self.__saldo:.2f}")


conta1 = ContaBancaria("Ana")
conta1.depositar(500)
conta1.depositar(200)
conta1.extrato()

conta1.sacar(100)
conta1.extrato()

conta1.sacar(700)
conta1.depositar(-50)
