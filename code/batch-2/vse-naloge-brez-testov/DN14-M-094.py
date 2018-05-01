import risar
from math import*
from random import*
import time

def ocena7():
    seznam = []
    vx = []
    vy = []
    cas = time.time() + 20
    for a in range(30):
        krogi = risar.krog(randint(0, risar.maxX-100), randint(0, risar.maxY-100), 10, risar.nakljucna_barva())
        x = randint(-5, 5)
        y = sqrt(5**2 - x**2)
        seznam.append(krogi)
        vx.append(x)
        vy.append(y)


    while True:
        if time.time() > cas:
            break
        for i in range(30):
            for i in range(len(seznam)):
                krogi = seznam[i]
                krogi.setPos(krogi.x() + vx[i], krogi.y() + vy[i])
                if not (0 < krogi.x() < risar.maxX - 35):
                    vx[i] = -vx[i]
                if not (0 < krogi.y() < risar.maxY - 35):
                    vy[i] = -vy[i]
            risar.cakaj(0.02)


ocena7()
risar.stoj()