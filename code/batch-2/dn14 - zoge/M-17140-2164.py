import risar
from random import *
from math import *


def zoga():
    barva = risar.nakljucna_barva()
    x, y = risar.nakljucne_koordinate()
    krog = risar.krog(x, y, 10, barva)

    vx = randint(-5, 5)
    vy = sqrt(25 - vx ** 2)
    return vx, vy, krog

'''for j in range(30):'''
vx, vy, krog = zoga()

for i in range(800):
    krog.setPos(krog.x() + vx, krog.y() + vy)
    if not (10 < krog.x() < risar.maxX - 10):
        vx = -vx
    if not (10 < krog.y() < risar.maxY - 10):
        vy = -vy
    risar.cakaj(0.02)
