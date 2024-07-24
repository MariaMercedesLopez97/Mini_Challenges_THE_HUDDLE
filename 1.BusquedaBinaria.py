def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        busqueda = lista[medio]
        if busqueda == objetivo:
            return True 
        elif busqueda < objetivo:
                izquierda = medio + 1
        else:
                derecha = medio - 1
    return False
lista_ordenada = [1,3,5,7,9,11,13,15,17,19]
objetivo = 89

resultado = busqueda_binaria(lista_ordenada, objetivo)
print(f"El numero {objetivo} {'esta'if resultado else 'no esta'} en la lista")