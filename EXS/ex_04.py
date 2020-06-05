class Kik:
    """Klasa kółko i krzyżyk"""

    def __init__(self, player1 = "", player2 = ""):
        self.player1 = player1
        self.player2 = player2
        self.plansza = []
        self.znak1 = 'x'
        self.znak2 = 'o'

    def __str__(self):
        return """Klasa kółko i krzyżyk"""

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

    def znak(self, z):
        x = self.x()
        y = self.y()
        if self.plansza[x][y] != []: return False
        self.plansza[x][y] = z
        return True

    def x(self):
        x = 1
        return x

    def y(self):
        y = 1
        return y

# TODO:
    def gra(self):
        p = self.czyWygrana()
        while p == False:
            while self.znak(self.znak1): pass
            p = self.czyWygrana()
            while self.znak(self.znak2): pass
            p = self.czyWygrana()




a = Kik()
a.initPlansza()
a.znak(a.znak1)
a.pokaz()
