def bogosort(lista):
    """Bogosort"""
    czyTrue = True
    while czyTrue:
        random.shuffle(lista)
        i = 0
        j = len(lista)
        while i + 1 < j:
            if lista[i] > lista[i + 1]:
                break
            i += 1
            if i == len(lista)-1:
                czyTrue = False
    return lista
