import risar
from math import *
from random import randint, uniform
from time import time

start = time()
krogi = []
polmer = 10

minX = minY = polmer + 1
maxX = risar.maxX - polmer - 1
maxY = risar.maxY - polmer - 1

for i in range(30):
    smerX = uniform(-5, 5)
    smerY = sqrt(5 ** 2 - smerX ** 2)
    x, y = randint(minX, maxX), randint(minY, maxY)
    krogi.append((risar.krog(x, y, polmer, risar.nakljucna_barva(), 3),
                  [smerX, smerY]))

while time() - start <= 20:
    for i in range(len(krogi)):
        smerX, smerY = krogi[i][1]
        krog = krogi[i][0]

        if krog.x() <= minX or krog.x() >= maxX:
            krogi[i][1][0] = -smerX
            smerX, smerY = krogi[i][1]

        if krog.y() <= minY or krog.y() >= maxY:
            krogi[i][1][1] = -smerY
            smerX, smerY = krogi[i][1]

        krog.setPos(krog.x() + smerX, krog.y() + smerY)
    risar.cakaj(0.02)
