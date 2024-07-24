def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista = [13,20,42,32,11]
lista_ordenada = burbuja(lista)
print("Lista Ordenada:",lista_ordenada)