class funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self  .salario = 0
        self .set_salario(salario)
    def get_salario(self):
        return self.salario
    def set_salario(self, valor):
        if valor >= 0:
            self.salario = valor
        else:
            print("erro: o salario nao pode ser negativo")

class CLT(funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)
    def calcular_salario(self):
        return self.get_salario()
    def exibir(self):
        print(f"nome: {self.nome} matricula: {self.matricula} tipo: CLT salario: R$ {self.calcular_salario(): .2f} ")
class gerente(funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)
    def calcular_salario(self):
        return self.get_salario() + 1500
    def exibir(self):
        print(f"nome: {self.nome} matricula: {self.matricula} tipo: gerente salario: R$ {self.calcular_salario(): .2f}")
class vendedor(funcionario):
    def __init__(self, nome, matricula, salario, vendas):
        super().__init__(nome, matricula, salario)
        self.vendas = vendas
    def calcular_salario(self):
        comissao = self.vendas * 0.10
        return self.get_salario() + comissao
    def exibir(self):
        print(f"nome: {self.nome} matricula: {self.matricula} tipo: vendedor salario: R$ {self.calcular_salario(): .2f} ")
                      

ana = CLT("ana", "001", 3000.00)
bruno = vendedor("bruno", "002", 2000.00, 12000.00)
carla = gerente("carla", "003", 5000.00)
lista_funcionarios = [ana, bruno, carla]
for f in lista_funcionarios:
        f.exibir()
    