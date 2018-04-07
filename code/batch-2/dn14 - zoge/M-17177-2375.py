import risar
import random
from random import randint
import math
import time

def ocena8():
    timer = time.time() + 20
    krogci = []
    vx = []
    vy = []
    xm, ym = risar.miska
    foo = risar.krog(xm, ym, 30, risar.bela)
    for i in range(30):
        x = randint(-5, 5)
        barva = risar.nakljucna_barva()
        krogi = risar.krog(randint(0, risar.maxX-100), randint(0, risar.maxY-100), 10, barva)
        krogci.append(krogi)
        vx.append(x)
        vy.append(math.sqrt(5 ** 2 - x ** 2))
    while True:
        if time.time() > timer:
            break
        for b in range(30):
            for i in range(len(krogci)):
                krog = krogci[i]
                krog.setPos(krog.x() + vx[i], krog.y() + vy[i])
                if not (0 < krog.x() < risar.maxX):
                    vx[i] = -vx[i]
                if not (0 < krog.y() < risar.maxY):
                    vy[i] = -vy[i]
                if risar.klik == False:
                    xm, ym = risar.miska
                    foo.setPos(xm,ym)
                if risar.klik == True:
                    if (abs(krog.x() - xm) <= 40) and (abs(krog.y() - ym) <= 40):
                        exit()
            risar.cakaj(0.02)

ocena8()
risar.stoj()