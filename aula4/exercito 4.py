class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = None
        self.set_temperatura(temperatura)

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, temperatura):
        if -50 <= temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print(f"Erro: temperatura {temperatura} fora do limite do sensor (-50 a 150)")

    def status(self):
        if self.__temperatura is None:
            return "Sem leitura"
        elif self.__temperatura <= 80:
            return "Normal"
        elif self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"


sensor1 = Sensor(25)
print(f"Temperatura: {sensor1.get_temperatura()} | Status: {sensor1.status()}")

sensor1.set_temperatura(95)
print(f"Temperatura: {sensor1.get_temperatura()} | Status: {sensor1.status()}")

sensor1.set_temperatura(135)
print(f"Temperatura: {sensor1.get_temperatura()} | Status: {sensor1.status()}")

sensor1.set_temperatura(-30)
print(f"Temperatura: {sensor1.get_temperatura()} | Status: {sensor1.status()}")

sensor1.set_temperatura(200)
