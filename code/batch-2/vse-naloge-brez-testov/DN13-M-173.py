class Minobot():
    def __init__(self):
        self.x, self.y = (0, 0)
        self.kot = 0


    def naprej(self, d):
        if self.kot == 0:
            self.x += d
        elif self.kot == 180:
            self.x -= d
        elif self.kot == 90:
            self.y += d
        elif self.kot == 270:
            self.y -= d


    def desno(self):
        if self.kot == 0:
            self.kot = 270
        else:
            self.kot -= 90


    def levo(self):
        if self.kot == 270:
            self.kot = 0
        else:
            self.kot += 90


    def koordinate(self):
        return ((self.x, self.y))


    def razdalja(self):
        return (abs(self.x) + abs(self.y))





