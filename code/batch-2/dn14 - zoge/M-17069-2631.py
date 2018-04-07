import risar
from random import *
from math import *
import random, decimal

zoge = []
x = []
y = []
vx = []
vy = []
znak1 = []
znak2 = []
for i in range(30):
    hx = randint(-5,5)
    hy = sqrt(25 - (hx ** 2))
    print(hx,hy)
    vx.append(hx)
    vy.append(hy)
    barva = risar.nakljucna_barva()
    znak1.append(randint(0, 1))
    znak2.append(randint(0, 1))
    x1,y1 = risar.nakljucne_koordinate()
    x.append(x1)
    y.append(y1)
    zoge.append(risar.krog(x1, y1, 10, barva, 1))

for a in range(1,900):
    for i in range(30):
        zoga = zoge[i]

        if znak1[i] == 0:
            x[i] += vx[i]
        else:
            x[i] -= vx[i]
        if znak2[i] == 0:
            y[i] += vy[i]
        else:
            y[i] -= vy[i]

        zoga.setPos(x[i], y[i])

        if x[i] > risar.maxX-1:
            if znak1[i] == 1:
                znak1[i] = 0
            else:
                znak1[i] = 1

        if y[i] > risar.maxY-1:
            if znak2[i] == 1:
                znak2[i] = 0
            else:
                znak2[i] = 1

        if x[i] < 1:
            if znak1[i] == 1:
                znak1[i] = 0
            else:
                znak1[i] = 1

        if y[i] < 1:
            if znak2[i] == 1:
                znak2[i] = 0
            else:
                znak2[i] = 1
    risar.cakaj(0.02)
