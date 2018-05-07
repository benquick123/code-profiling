class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smerr = "E"
        self.smeri = "NESW"
        self.premiki = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.shrani_ukaze = []
        self.res = False

    def naprej(self, d):
        ismer = self.smeri.index(self.smerr)
        dx, dy = self.premiki[ismer]
        self.x += dx * d
        self.y += dy * d
        self.shrani_ukaze.append("n" + str(d))

    def nazaj(self, d):
        ismer = self.smeri.index(self.smerr)
        dx, dy = self.premiki[ismer]
        self.x -= dx * d
        self.y -= dy * d

    def desno(self):
        ismer = self.smeri.index(self.smerr)
        self.smerr = self.smeri[(ismer + 1) % 4]
        if not self.res:
            self.shrani_ukaze.append("d")

    def levo(self):
        ismer = self.smeri.index(self.smerr)
        self.smerr = self.smeri[(ismer - 1) % 4]
        if not self.res:
            self.shrani_ukaze.append("l")

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(0 - self.x) + abs(0 - self.y)

    def razveljavi(self):
        self.res = True
        if len(self.shrani_ukaze) != 0:
            ukaz = self.shrani_ukaze.pop()
            if len(ukaz) == 1:
                if ukaz == "l":
                    self.desno()
                else:
                    self.levo()
            else:
                self.nazaj(int(ukaz[1]))
