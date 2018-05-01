import math

class Minobot:
    def __init__(self):
        self.x = self.y = 0
        self.kot = 0
        self.stanja = [[self.x, self.y, self.kot]]

    def obrni_se(self, kot_):
        self.stanja.append([self.x, self.y, self.kot])

        self.kot += kot_

        if self.kot == 360:
            self.kot = 0
        elif self.kot < 0:
            self.kot = 360 + self.kot

    def naprej(self, d):
        self.stanja.append([self.x, self.y, self.kot])

        if self.kot == 0:
            self.x += d
        elif self.kot == 90:
            self.y -= d
        elif self.kot == 180:
            self.x -= d
        elif self.kot == 270:
            self.y += d

    def desno(self):
        self.obrni_se(90)

    def levo(self):
        self.obrni_se(-90)

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if len(self.stanja) < 1:
            return

        self.x, self.y, self.kot = self.stanja.pop()


