from math import *
import risar
from random import *


def ocena7():
    zoge = []
    vx = []
    vy = []
    v = 5
    for i in range(30):
        x, y = risar.nakljucne_koordinate()
        barva = risar.nakljucna_barva()
        krogi = risar.krog(x, y, 10, barva)
        zoge.append(krogi)
        vx.append(randint(-5, 5))
        racun = sqrt(v ** 2 - vx[i] ** 2)
        vy.append(racun)
    for j in range(1000):
        for j in range(len(zoge)):
            krogi = zoge[j]
            krogi.setPos(krogi.x() + vx[j], krogi.y() + vy[j])
            if not (0 < krogi.x() < risar.maxX):
                vx[j] = -vx[j]
            if not (0 < krogi.y() < risar.maxY):
                vy[j] = -vy[j]
        risar.cakaj(0.02)
    risar.stoj()


ocena7()

def ocena6():
    x, y = risar.nakljucne_koordinate()
    barva = risar.nakljucna_barva()
    krog = risar.krog(x, y, 10, barva)
    zoga = []
    zoga.append(krog)
    vx = randint(-5, 5)
    v = 5
    vy = sqrt(v**2-vx**2)
    for i in range(1000):
        for a in zoga:
            a.setPos(a.x() + vx, a.y() + vy)
            if not (0 < a.y() < risar.maxY):
                vy = -vy
            if not (0 < a.x() < risar.maxX):
                vx = -vx
        risar.cakaj(0.02)
    risar.stoj()
    
    
#ocena6()
