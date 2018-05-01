class Minobot:
    def __init__(self):
        self.premiki = [(1, 0), (0, -1), (-1, 0), (0, 1)] # "DESNO", "DOL", "LEVO", "GOR"
        self.x = self.y = self.smer = 0
        self.poteze = []

    def naprej(self, d):
        self.x += self.premiki[self.smer][0] * d
        self.y += self.premiki[self.smer][1] * d
        self.poteze.append((self.x, self.y, self.smer))

    def desno(self):
        self.smer = (self.smer + 1) % 4
        self.poteze.append((self.x, self.y, self.smer))

    def levo(self):
        self.smer = (self.smer - 1) % 4
        self.poteze.append((self.x, self.y, self.smer))

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        del self.poteze[-1]
        if self.poteze:
            self.x, self.y, self.smer = self.poteze[-1]
        else:
            self.x = self.y = self.smer = 0
            self.poteze.append((0, 0, 0))

