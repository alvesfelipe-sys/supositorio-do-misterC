class Forma:
    def area(self):
        return 0
class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado
p1 = Triangulo(10, 5)
p2 = Quadrado(6)
p3 = Triangulo(8, 4)
formas = [p1, p2, p3]
for f in formas:
    print(f.area())