class Funcionario:
    def calcular_salario(self):
        return 0
class Vendedor(Funcionario):
    def __init__(self, fixo, comissao):
        self.fixo = fixo
        self.comissao = comissao
    def calcular_salario(self):
        return self.fixo + self.comissao
class Gerente(Funcionario):
    def __init__(self, fixo, bonus):
        self.fixo = fixo
        self.bonus = bonus
    def calcular_salario(self):
        return self.fixo + self.bonus
dambrosgay = Vendedor(2000, 500)
pyetrobumbum = Gerente(4000, 1000)
print(dambrosgay.calcular_salario())
print(pyetrobumbum.calcular_salario())