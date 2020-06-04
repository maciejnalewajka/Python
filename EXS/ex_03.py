# Funkcja liczy znaki ciągu znaków
def policz(s):
    r = 0
    for i in range(0, len(s)):
        r += 1
    return r

def policz2(s):
    return len(s)

# Funkcja liczy cyfry w ciągu znaków
def policzCyfry(s):
    k = 0
    for i in s:
        try:
            int(i)
            k += 1
        except:
            pass
    return k

# Funkcja sumuje cyfry w ciągu znaków
def dodajCyfry(s):
    k = 0
    for i in s:
        try:
            k += int(i)
        except:
            pass
    return k

# Funkcja liczy ilość wystąpień podanego znaku w ciągu znaków
def policzZnak(z, s):
    k = 0
    for i in s:
        if z == i: k += 1
    return k

# Funkcja liczy ilość wystąpień podanego słowa w ciągu znaków
def policzSlowo(s, str):
    k = 0
    l = len(s)
    for i in range(0, len(str)):
        if s == str[i:i+l]: k += 1
    return k
