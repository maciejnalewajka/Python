x = 12
y = 5

# Zadanie 1
"""Napisz program, który wykona dodawanie, odejmowanie, dzielenie, mnożenie, potęgowanie, dzielenie bez reszty oraz poda resztę z dzielenia dwóch podanych liczb"""

def zadanie_1(a, b):
    # dodawanie
    print("Wynik dodawania liczb {} oraz {} to: {}".format(a, b, a+b))
    # odejmowanie
    print("Wynik odejmowania liczb {} oraz {} to: {}".format(a, b, a-b))
    # dzielenie
    print("Wynik dzielenia liczb {} oraz {} to: {}".format(a, b, a/b))
    # mnożenie
    print("Wynik mnożenia liczb {} oraz {} to: {}".format(a, b, a*b))
    # potęgowanie
    print("Wynik z podniesienia liczby {} do potęgi {} to: {}".format(a, b, a**b))
    # dzielenie bez reszty
    print("Wynik dzielenia bez reszty liczb {} oraz {} to: {}".format(a, b, a//b))
    # reszta z dzielenia
    print("Reszta z dzielenia liczb {} oraz {} to: {}".format(a, b, a%b))

# zadanie_1(x, y)

# Zadanie 2
"Napisz rpogram, który będzie zwracał informację jakiego typu jest podana zmienna."

def zadanie_2(podana_zmienna):
    return type(podana_zmienna)

# print(zadanie_2(9))

# Zadanie 3
"Napisz program, który będzie przekształcał typ int i float na string i odwrotnie o ile to możliwe."

def zadanie_3(value):
    if(isinstance(value, str)):
        try:
            value = float(value)
            try:
                value = int(value)
            except:
                pass
            return "Wartość {} jest teraz typu {}.".format(value, type(value))
        except:
            pass
    elif(isinstance(value, int) or isinstance(value, float)):
        value = str(value)
        return "Wartość {} jest teraz typu {}.".format(value, type(value))
    return "Wartości {} nie można zmienić.".format(value)

# print(zadanie_3("16"))
