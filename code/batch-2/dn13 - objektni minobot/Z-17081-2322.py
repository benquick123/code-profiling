class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.trenutna_smer = "E"

    def naprej(self, d):
        novo_stanje = self.premik(d, self.x, self.y, self.trenutna_smer)
        self.x = novo_stanje[0]
        self.y = novo_stanje[1]
        self.trenutna_smer = novo_stanje[2]

    def desno(self):
        novo_stanje = self.premik("R", self.x, self.y, self.trenutna_smer)
        self.x = novo_stanje[0]
        self.y = novo_stanje[1]
        self.trenutna_smer = novo_stanje[2]

    def levo(self):
        novo_stanje = self.premik("L", self.x, self.y, self.trenutna_smer)
        self.x = novo_stanje[0]
        self.y = novo_stanje[1]
        self.trenutna_smer = novo_stanje[2]

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def premik(self, ukaz, x, y, smer):
        smeri = "NESW"
        premiki = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ismer = smeri.index(smer)
        if ukaz == "R":
            smer = smeri[(ismer + 1) % 4]
        elif ukaz == "L":
            smer = smeri[(ismer - 1) % 4]
        else:
            dx, dy = premiki[ismer]
            x += dx * ukaz
            y += dy * ukaz
        return x, y, smer
