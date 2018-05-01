import risar
import time
import sys
from random import randint, random
from math import sqrt

st_zog = 30

vx = []
vy = []
zoge = []


for i in range(st_zog):
    x0, y0 = randint(0+10, risar.maxX - 10), randint(0+10, risar.maxY - 10)
    barva = risar.nakljucna_barva()
    krog = risar.krog(x0, y0, 10, barva=barva, sirina=3)
    zoge.append(krog)

    x = (randint(-5,5))
    vx.append(x)
    c = 5
    y = sqrt(c**2 - x**2)
    vy.append(y)


for i in range(0, 4700, 5):
    for i in range(len(zoge)):
        zoga = zoge[i]
        zoga.setPos(zoga.x() + vx[i], zoga.y() + vy[i] )
        if not (0+10 < zoga.x() < risar.maxX - 10):
            vx[i] = -vx[i]
        if not (0+10 < zoga.y() < risar.maxY - 10):
            vy[i] = -vy[i]
    risar.cakaj(0.02)




