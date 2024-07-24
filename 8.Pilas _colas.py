class Pila:
    def __init__(self):
        self.elementos = []
    
    def apilar(self, elemento):
        self.elementos.append(elemento)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def cima(self):
        if not self.esta_vacia():
            return self.elementos[-1]
    
    def tamaño(self):
        return len(self.elementos)

pila = Pila()
for i in range(1, 6):
    pila.apilar(i)

while not pila.esta_vacia():
    print(pila.desapilar())