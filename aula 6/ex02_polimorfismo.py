class Instrumento:
    def tocar(self):
        print("Som genérico")
class Violao(Instrumento):
    def tocar(self):
        print("Plim plim")
class Bateria(Instrumento):
    def tocar(self):
        print("Bum bum")
class Piano(Instrumento):
    def tocar(self):
        print("Til til")
feliposo = Violao()
enzolabubu = Bateria()
dambrosgay = Piano()
instrumentos = [feliposo, enzolabubu, dambrosgay]
for i in instrumentos:
    i.tocar()