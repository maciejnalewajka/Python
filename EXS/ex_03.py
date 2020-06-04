def policz(s):
    r = 0
    for i in range(0, len(s)):
        r += 1
    return r

def policz2(s):
    return len(s)

def policzLiczby(s):
    k = 0
    for i in s:
        try:
            int(i)
            k += 1
        except:
            pass
    return k

def dodajLiczby(s):
    k = 0
    for i in s:
        try:
            k += int(i)
        except:
            pass
    return k

def policzZnak(z, s):
    k = 0
    for i in s:
        if z == i: k += 1
    return k

def policzSlowo(s, str):
    k = 0
    l = len(s)
    for i in range(0, len(str)):
        if s == str[i:i+l]: k += 1
    return k


print(policzSlowo("zo", "aloosozozolo"))
