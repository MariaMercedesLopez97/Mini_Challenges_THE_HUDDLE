class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def describir(self):
        return f"Motor de tipo {self.tipo}"

class Auto:
    def __init__(self, modelo, tipo_motor):
        self.modelo = modelo
        self.motor = Motor(tipo_motor)
    
    def describir_motor(self):
        return f"El {self.modelo} tiene un {self.motor.describir()}"

auto = Auto("Sedán", "gasolina")
print(auto.describir_motor())