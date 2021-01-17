def bubble_sort(lista):
    for j in range(len(lista)-1, 0, -1):
        for i in range(j):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista
