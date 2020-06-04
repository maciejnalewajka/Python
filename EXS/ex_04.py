class Kik:
    """Klasa kółko i krzyżyk"""

    def __init__(self, player1 = "", player2 = ""):
        self.player1 = player1
        self.player2 = player2
        self.plansza = []

    def initPlansza(self):
        self.plansza = [[[],[],[]],[[],[],[]],[[],[],[]]]
        return self.plansza

    def pokaz(self):
        for i in range(0, 3):
            print(self.plansza[i])


    def isEmpty(self):
        k = True
        for i in range(0,3):
            for j in range(0,3):
                if self.plansza[i][j] != []:
                    k = False
                    break
        return k

    def czyWygrana(self):
        p = self.isEmpty()
        if p == True: return False
        for i in self.plansza:
            if i[0] != [] and i[0] == i[1] == i[2]:
                return True
        for i in range(0, 3):
            if self.plansza[0][i] != [] and self.plansza[0][i] == self.plansza[1][i] == self.plansza[2][i]:
                return True
        if self.plansza[1][1] != []:
            if self.plansza[0][0] == self.plansza[1][1] == self.plansza[2][2]:
                return True
            if self.plansza[2][0] == self.plansza[1][1] == self.plansza[0][2]:
                return True
        return False

    def kolko(self, x, y):
        if self.plansza[x][y] != []: return False
        self.plansza[x][y] = 'o'
        return True

    def krzyzyk(self, x, y):
        if self.plansza[x][y] != []: return False
        self.plansza[x][y] = 'x'
        return True

    def miejsce(self):
        k = True
        while k:
            # x = rawinput("Podaj x (1 - 3): ")
            # y = rawinput("Podaj y (1 - 3): ")
            x = 1
            y = 1
    # TODO:         try:
        #         int(x)
        #         int(y)
        #         k = False
        #     except: pass
        # return (x-1, y-1)

# TODO:
    # def gra(self):
    #     p = False
    #     while p == False:
    #         k = self.miejsce()


a = Kik()
a.initPlansza()
# a.kolko(0,0)
# a.pokaz()
a.miejsce()
