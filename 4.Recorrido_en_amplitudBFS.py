from collections import deque

#------- Implementación de BFS para un grafo simple con 5 nodos------
def bfs(grafo, inicio):
    visitado = set()
    cola = deque([inicio])

    while cola:
        vertice = cola.popleft()
        if vertice not in visitado:
            print(vertice, end=' ')
            visitado.add(vertice)
            cola.extend(grafo[vertice] - visitado)

#------- Grafo representado como un diccionario------
grafo = {
    1: {2, 3},
    2: {1, 4, 5},
    3: {1},
    4: {2},
    5: {2}
    
}

bfs(grafo, 1)
