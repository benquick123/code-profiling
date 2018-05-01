
class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.koordinati = (self.x, self.y)
        self.smer = "desno"
        self.koraki = ["desno", "dol", "levo", "gor"]
        self.stevec = 0
        self.ukazi = []

    def update(self):
        self.koordinati = (self.x, self.y)
        self.smer = self.smer
        self.stevec = self.stevec
        self.ukazi.append([self.koordinati, self.smer])

    def naprej(self, d):
        if self.smer == "desno":
            self.x += d
        if self.smer == "levo":
            self.x -= d
        if self.smer == "gor":
            self.y += d
        if self.smer == "dol":
            self.y -= d
        self.update()

    def desno(self):
        self.stevec += 1
        if self.stevec == 4:
            self.stevec = 0
        self.smer = self.koraki[self.stevec]
        self.update()

    def levo(self):
        self.stevec -= 1
        if self.stevec == - 1:
            self.stevec = 3
        self.smer = self.koraki[self.stevec]
        self.update()

    def koordinate(self):
        return self.koordinati

    def razdalja(self):
        x0, y0 = self.x, self.y
        return abs(x0) + abs(y0)

    def razveljavi(self):
        if not self.ukazi:
            return None
        if len(self.ukazi) == 1:
            self.x, self.y = 0, 0
            self.smer = "desno"
        else:
            ukaz = self.ukazi[-2]
            self.x, self.y = ukaz[0]
            self.smer = ukaz[1]
            self.ukazi = self.ukazi[:-2]
            self.update()


