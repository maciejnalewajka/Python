string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sed cursus tortor. Cras accumsan mattis nulla, non euismod quam gravida eu. Duis ultricies a nunc id sollicitudin. Cras lacinia sodales enim, vel laoreet nulla pretium blandit. Suspendisse cursus nec dui a placerat. Maecenas nisi urna, interdum in venenatis quis, rhoncus in felis. Integer at mattis massa. Etiam ac condimentum urna. Nullam id mattis augue.

Pellentesque eu luctus quam. Nulla at ex elit. Cras luctus, lacus eu hendrerit feugiat, orci eros ullamcorper nisl, in finibus sem arcu nec ex. Donec auctor elit a mi pretium, ut interdum nunc ullamcorper. Aenean non orci vitae nisl eleifend porttitor. Nullam varius, lectus ut scelerisque commodo, tortor enim pulvinar eros, sed placerat dui velit eu ipsum. In sit amet sem ut purus tempus semper. Phasellus facilisis sodales dui, mattis gravida augue dapibus in. Praesent arcu est, feugiat at rutrum nec, dignissim ac augue. Suspendisse ultricies felis dui, eget cursus velit varius vel. Duis volutpat lacus quis purus sagittis porttitor.

Mauris tempor lorem eu ex egestas, sit amet varius metus lobortis. Curabitur vitae ligula lorem. Pellentesque dictum viverra euismod. Nunc blandit mollis gravida. Ut vel bibendum nunc. Proin eget dapibus purus. Fusce a ullamcorper quam, ac mattis tortor. Integer sed sapien et risus porttitor fermentum sit amet in ligula. Vivamus scelerisque sapien et justo tristique varius eget vel sapien.

Proin sed mauris nec felis porta imperdiet nec id lectus. Praesent sit amet arcu id leo accumsan condimentum. Praesent feugiat odio velit, at tincidunt neque fermentum malesuada. Maecenas eros nisl, egestas pretium semper a, vulputate aliquet arcu. Etiam placerat elit sit amet imperdiet pellentesque. Maecenas dignissim tempus vulputate. Nunc dui ante, egestas vitae urna id, posuere facilisis ipsum. Integer mi dui, tempus id dolor et, molestie euismod neque. Quisque et risus libero. Nulla facilisi.

Etiam congue mi et vulputate scelerisque. Quisque consectetur mi dapibus dolor imperdiet, hendrerit luctus mauris mollis. Ut ornare tortor quis nibh imperdiet, vel scelerisque quam molestie. Morbi eget finibus elit. Ut dui turpis, lobortis a auctor id, posuere eget lectus. Sed bibendum ullamcorper purus. Aliquam non nunc ac sem fermentum euismod eget ut mi. In scelerisque nibh odio, et tincidunt massa molestie quis. Cras euismod tristique porta. Mauris eu feugiat turpis. Ut sed justo finibus, pellentesque lectus eu, ultrices urna. Nam dolor nisl, aliquet eget lobortis a, congue at nisl."""

# Zadanie 1
"""Policz wszystkie wystąpienia znaków w tekście. Przedstaw je w postaci słownika.
a) rozróżniaj małe i duże znaki
b) nie rozróżniaj małych i dużych znaków
"""

def zadanie_1(string, litera):
    slownik = {}
    if(litera == 'b'):
        string = string.upper() # Duże
        # string = string.lower()   # Małe
    for el in string:
        if(el not in slownik):
            slownik[el] = 1
        else:
            slownik[el] += 1
    return slownik
# print(zadanie_1(string, "b"))

# Zadanie 2
"""Zamień każdy wybrany znak na inny znak w tekście. Zwróć tekst w postaci String."""

def zadanie_2(string, stary_znak, nowy_znak):
    x = 0
    nowy_string = ""
    for i in range(len(string)):
        if(string[i] == stary_znak):
            nowy_string += string[x:i]
            nowy_string += nowy_znak
            x = i+1
    nowy_string += string[x:len(string)]
    return nowy_string

# print(zadanie_2(string, 'a', '?'))
