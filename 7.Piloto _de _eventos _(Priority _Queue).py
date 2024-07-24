class ColaPrioridad:
    def __init__(self):
        self.cola = []
    
    def insertar(self, elemento, prioridad):
        self.cola.append((prioridad, elemento))
        self.cola.sort(reverse=True)
    
    def eliminar(self):
        if self.cola:
            return self.cola.pop(0)[1]
        return None

cp = ColaPrioridad()
cp.insertar("Tarea 1", 3)
cp.insertar("Tarea 2", 1)
cp.insertar("Tarea 3", 4)
cp.insertar("Tarea 4", 2)
cp.insertar("Tarea 5", 5)

for _ in range(5):
    print(cp.eliminar())