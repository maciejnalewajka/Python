"""Zaprojektuj i napisz funkcję, która konwertuje liczbę podaną w pozycyjnym systemie
liczbowym A na liczbę w systemie liczbowym B. Jako wynik funkcja zwraca słownik:

{‘system A’: liczba_w_systemie_A, ‘system B’: liczba_w_systemie_B}. Systemy pozycyjne
proszę ograniczyć od dwójkowego do szesnastkowego."""

def z_dziesietnego(liczba, na_system):
    tablica_znakow = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    s1 = ""
    while(liczba > 0):
        s1 += tablica_znakow[liczba % na_system]
        liczba = liczba // na_system
    return s1[::-1]

def konwerter(liczba, z_systemu, na_system):
    tablica_znakow = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    nowa = 0
    s = str(liczba)
    for i in range(len(s)):
        nowa += int(tablica_znakow[s[i]] * (z_systemu ** (len(s) - 1 - i)))
    if(na_system == 10):
        return str(nowa)
    return z_dziesietnego(int(nowa), na_system)

def main(liczba, z_systemu, na_system):
    if(z_systemu < 1 | z_systemu > 17 | na_system < 1 | na_system > 17):
        raise Exception('system', 'system > 1 or system < 17')
    sys1 = "system " + str(z_systemu)
    dict = {}
    dict[sys1]= liczba
    if(z_systemu == na_system):
        return dict
    if(z_systemu == 10):
        sys2 = "system " + str(na_system)
        dict[sys2]= z_dziesietnego(liczba, na_system)
        return dict
    else:
        sys2 = "system " + str(na_system)
        dict[sys2]= konwerter(liczba, z_systemu, na_system)
    return dict

# main(1111, 2, 16)["system 16"]
