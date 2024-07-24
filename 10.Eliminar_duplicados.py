def eliminar_duplicados(lista):
    return list(dict.fromkeys(lista))

lista_original = [1, 2, 3, 4, 2, 5, 6, 1, 7, 8]
print(eliminar_duplicados(lista_original))