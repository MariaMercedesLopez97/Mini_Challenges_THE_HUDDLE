def recorrido_profundidad(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    print(inicio, end=' ')
    for siguiente in grafo[inicio] - visitados:
        recorrido_profundidad(grafo, siguiente, visitados)
    return visitados

grafo = {0: {1, 2}, 1: {0, 3, 4}, 2: {0, 4}, 3: {1}, 4: {1, 2}}
recorrido_profundidad(grafo, 0)