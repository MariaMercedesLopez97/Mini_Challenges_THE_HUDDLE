class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir_coordenadas(self):
        print(f"({self.x}, {self.y})")

punto = Punto2D(3, 4)
punto.imprimir_coordenadas()