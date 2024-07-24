import heapq

def distancia_heuristica(nodo, meta):
    # Esta es una función heurística simple. En un caso real, 
    # deberías implementar una heurística más precisa.
    return 0

def a_estrella(grafo, inicio, meta):
    #------- Inicializamos las estructuras de datos------
    cola_prioridad = [(0, inicio)]
    costo_g = {inicio: 0}
    costo_f = {inicio: distancia_heuristica(inicio, meta)}
    camino = {inicio: None}
    
    while cola_prioridad:
        _, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == meta:
            # Reconstruimos el camino
            ruta = []
            while nodo_actual:
                ruta.append(nodo_actual)
                nodo_actual = camino[nodo_actual]
            return ruta[::-1]
        
        for vecino, peso in grafo[nodo_actual].items():
            nuevo_costo_g = costo_g[nodo_actual] + peso
            
            if vecino not in costo_g or nuevo_costo_g < costo_g[vecino]:
                costo_g[vecino] = nuevo_costo_g
                costo_f[vecino] = nuevo_costo_g + distancia_heuristica(vecino, meta)
                camino[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (costo_f[vecino], vecino))
    
    #------ Si no se encuentra un camino----
    return None

# Ejemplo de uso
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

resultado = a_estrella(grafo, 'A', 'E')
print(f"El camino más corto es: {resultado}")