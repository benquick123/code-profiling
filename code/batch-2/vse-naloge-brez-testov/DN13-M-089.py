from math import *

class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kot = 0

    def naprej(self, koraki):
        kott = radians(self.kot)
        xk = self.x + koraki * cos(kott)
        xz = self.y - koraki * sin(kott)
        self.x = xk
        self.y = xz

    def obrni(self, nov_kot):
        self.kot += nov_kot

    def levo(self):
        self.obrni(-90)

    def desno(self):
        self.obrni(90)

    def koordinate(self):
        koords = round(self.x), round(self.y)
        return koords

    def razdalja(self):
        taxicab = abs(self.x - 0) + abs(self.y - 0)
        return round(taxicab)


a = Minobot()
a.levo()
a.naprej(4)
a.desno()
a.naprej(3)


