class Nodo:
    def __init__(self, clave):
        self.izquierda = None
        self.derecha = None
        self.valor = clave

def insertar(raiz, clave):
    if raiz is None:
        return Nodo(clave)
    else:
        if raiz.valor < clave:
            raiz.derecha = insertar(raiz.derecha, clave)
        else:
            raiz.izquierda = insertar(raiz.izquierda, clave)
    return raiz

def en_orden(raiz):
    if raiz:
        en_orden(raiz.izquierda)
        print(raiz.valor, end=" ")
        en_orden(raiz.derecha)

raiz = None
elementos = [5, 3, 7, 1, 9]
for elemento in elementos:
    raiz = insertar(raiz, elemento)

print("Elementos en el árbol en orden:")
en_orden(raiz)
