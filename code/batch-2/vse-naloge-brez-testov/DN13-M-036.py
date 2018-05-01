class Minobot:
    def __init__(self, x=0, y=0, smeri="VJZS", premik=0):
        self.x = x
        self.y = y
        self.smeri = smeri
        self.premik = premik

    def naprej(self, d):
        if self.smeri[self.premik] == self.smeri[0]:
            self.x += d
        elif self.smeri[self.premik] == self.smeri[2]:
            self.x -= d
        elif self.smeri[self.premik] == self.smeri[3]:
            self.y += d
        elif self.smeri[self.premik] == self.smeri[1]:
            self.y -= d

    def desno(self):
        self.premik += 1

        if self.premik == 4:
            self.premik = 0

    def levo(self):
        self.premik -= 1

        if self.premik == -1:
            self.premik = 3

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

