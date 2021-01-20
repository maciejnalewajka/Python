# Zadanie 1
"Napisz program, który sprawdzi czy podana liczba należy do podanego przedziału"

def zadanie_1(liczba, poczatek_przedzialu, koniec_przedzialu):
    wynik = False
    try:
        wynik = liczba >= poczatek_przedzialu and liczba <= koniec_przedzialu
    except:
        return "Wprowadzono nieprawidłową wartość!"
    return wynik

# print(zadanie_1(5, 0, 2))

# Zadanie 2
"Napisz program, który zwróci typ wprowadzonej wartości."

def zadanie_2(value):
    return type(value)

# Zadanie 3
"Napisz program, który z podanej listy wartości oblicza ilość takich samych typów i przedstawia je w postaci słownika."

def zadanie_3(values):
    dictOfTypes = {}
    for value in values:
        typeName = str(type(value))
        if(typeName in dictOfTypes):
            dictOfTypes[typeName] += 1
        else:
            dictOfTypes[typeName] = 1
    return dictOfTypes

# values = [1, 2, 3, "Hi", "Mark", None, True]
# print(zadanie_3(values))
