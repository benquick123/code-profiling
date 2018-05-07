from risar import *
from random import randint


class Zoga:
    def __init__(self, barva, x, y, vx, vy):
        self.barva = barva
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def narisi(self):
        krog(self.x, self.y, 10, barva=self.barva, sirina=3)

    def premik(self):
        self.x += self.vx
        self.y += self.vy

    def odboj_x(self):
        self.vx = -self.vx

    def odboj_y(self):
        self.vy = -self.vy

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


barva = nakljucna_barva()
x, y = nakljucne_koordinate()
vx = randint(-5, 5)
vy = (vx ** 2) - 25

obnavljaj = True
zoga = Zoga(barva, x, y, vx, vy)
stevec = 0

while stevec < 20:
    pobrisi()
    zoga.narisi()
    if zoga.get_y() <= 0 or zoga.get_y() >= 600:
        zoga.odboj_y()
    if zoga.get_x() <= 0 or zoga.get_x() >= 800:
        zoga.odboj_x()
    zoga.premik()
    stevec += 0.02
    cakaj(0.02)

