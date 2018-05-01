class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = (1,0)

    def naprej(self, d):
        self.x = self.x + self.smer[0] * d
        self.y = self.y + self.smer[1] * d

    def desno(self):
        sez = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        smer = sez.index(self.smer)
        smer = smer + 1
        if smer > 3:
            smer = 0
        self.smer = sez[smer]

    def levo(self):
        sez = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        smer = sez.index(self.smer)
        smer = smer - 1
        if smer < 0:
            smer = 3
        self.smer = sez[smer]

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)


