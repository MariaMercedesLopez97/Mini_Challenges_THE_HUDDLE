class Figura:
    def imprimir(self):
        print("Esta es una figura")

class Circulo(Figura):
    def imprimir(self):
        print("Este es un círculo")

figura = Figura()
circulo = Circulo()

figura.imprimir()
circulo.imprimir()