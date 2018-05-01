class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kot = 90

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x)+abs(self.y)

    def naprej(self,d):
        novx = self.x
        novy = self.y
        if self.kot >= 360:
            self.kot -= 360
        elif self.kot < 0:
            self.kot += 360
        if self.kot == 0:
            novy = self.y + d
        elif self.kot == 90:
            novx = self.x + d
        elif self.kot == 180:
            novy = self.y - d
        elif self.kot == 270:
            novx = self.x - d
        self.x = int(novx)
        self.y = int(novy)

    def desno(self):
        self.kot += 90

    def levo(self):
        self.kot -= 90

