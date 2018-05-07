import risar, os
from random import random, uniform, randint
from time import time
from math import sqrt, pow

krogi = []
vx = []
vy = []

barva_krog_miska = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))

for i in range(30):
    x0, y0 = randint(10, risar.maxX - 10), randint(10, risar.maxY - 10)
    barva_krog = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
    krog = risar.krog(x0, y0, 10, barva=barva_krog, sirina=2)
    krogi.append(krog)
    vx.append(uniform(-5, 5))
    vy.append(1)

start = time()

x, y = risar.miska
miska = risar.krog(x, y, 30, barva=barva_krog_miska, sirina=2)

for i in range(5000):
    x, y = risar.miska
    if risar.klik == False:
        miska.setPos(x, y)
        kor_miske_x = x
        kor_miske_y = y

    for i in range(len(krogi)):
        krog = krogi[i]
        if krog.y() < 0 or krog.y() > risar.maxY - 10:
            vy[i] = -vy[i]
        if krog.x() < 0 or krog.x() > risar.maxX - 10:
            vx[i] = -vx[i]
        y = sqrt(pow(5, 2) - pow(vx[i], 2)) * vy[i]
        krog.setPos(krog.x() + vx[i], krog.y() + y)

        if risar.klik:
            if sqrt(pow(abs(krog.x() - kor_miske_x), 2) + pow(abs(krog.y() - kor_miske_y), 2)) < 41:
                risar.stoj()

    if time() - start >= 20:
        risar.stoj()
    risar.cakaj(0.02)