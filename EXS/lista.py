lista_int = [1,4,2,5,6,77]
lista_string = ["ala", "ma", "kota"]
lista_mieszana = [1, "ola", 1.34]

# Zadanie 1
"Wypisz wszystkie elementy listy."

def zadanie_1(lista):
    for i in lista:
        print(i)

# zadanie_1(lista_string)

# Zadanie 2
"Połącz ze sobą wszystkie wyrazy z listy oddzielając je podanym znakiem i zakończ kropką."

def zadanie_2(lista, znak):
    polaczone_slowa = lista[0]
    for i in range(1, len(lista)):
        polaczone_slowa += f"{znak}{lista[i]}"
    polaczone_slowa += '.'
    return polaczone_slowa

# print(zadanie_2(lista_string, " "))

# Zadanie 3
"Połącz ze sobą trzy podane listy, przekształć otrzymaną listę w słownik gdzie indeks jest kluczem. Wypisz wszystkie elementy słownika."

def zadanie_3(lista_1, lista_2, lista_3):
    nowa_lista = lista_1 + lista_2 + lista_3
    slownik = {}
    for i in range(len(nowa_lista)):
        slownik[i] = nowa_lista[i]
        print(slownik[i])
    return slownik

# lista_1 = [1,2,3]
# lista_2 = ["Ala", "kot", "owca"]
# lista_3 = [None, True, False]
#
# print(zadanie_3(lista_1, lista_2, lista_3))
