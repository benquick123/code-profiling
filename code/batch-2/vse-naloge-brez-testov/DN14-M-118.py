import risar
import random
import math
from time import time

def ocena_6():
    hitrost_x = []
    hitrost_y = []
    krogi = []

    x0, y0 = random.randint(16, risar.maxX), random.randint(13, risar.maxY)
    barva = risar.barva(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    krog = risar.krog(x0, y0, 10, barva, 3)
    krogi.append(krog)
    hx = random.randint(-4, 4)
    hitrost_x.append(hx)
    hitrost_y.append(math.sqrt(5 ** 2 - hx ** 2))

    start = time()
    while time() - start < 20:
        for i in range(len(krogi)):
            krog = krogi[i]
            krog.setPos(krog.x() + hitrost_x[i], krog.y() + hitrost_y[i])
            if not (13 < krog.x() < risar.maxX - 13):
                hitrost_x[i] = -hitrost_x[i]
            if not (13 < krog.y() < risar.maxY - 13):
                hitrost_y[i] = -hitrost_y[i]
        risar.cakaj(0.02)
    exit()

def ocena_7():
    hitrost_x = []
    hitrost_y = []
    krogi = []

    for i in range(30):
        x0, y0 = random.randint(13, risar.maxX - 13), random.randint(13, risar.maxY - 13)
        barva = risar.barva(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        krog = risar.krog(x0, y0, 10, barva, 3)
        krogi.append(krog)
        hx = random.randint(-4, 4)
        hitrost_x.append(hx)
        hitrost_y.append(math.sqrt(5 ** 2 - hx ** 2))

    start = time()
    while time() - start < 20:
        for i in range(len(krogi)):
            krog = krogi[i]
            krog.setPos(krog.x() + hitrost_x[i], krog.y() + hitrost_y[i])
            if not (13 < krog.x() < risar.maxX - 13):
                hitrost_x[i] = -hitrost_x[i]
            if not (13 < krog.y() < risar.maxY - 13):
                hitrost_y[i] = -hitrost_y[i]
        risar.cakaj(0.02)
    exit()

def ocena_8():
    hitrost_x = []
    hitrost_y = []
    krogi = []

    for i in range(30   ):
        x0, y0 = random.randint(13, risar.maxX - 13), random.randint(13, risar.maxY - 13)
        barva = risar.barva(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        krog = risar.krog(x0, y0, 10, barva, 3)
        krogi.append(krog)
        hx = random.randint(-4, 4)
        hitrost_x.append(hx)
        hitrost_y.append(math.sqrt(5 ** 2 - hx ** 2))
    miska = risar.krog(risar.miska[0], risar.miska[1], 30, barva, 3)
    start = time()
    while time() - start < 20:
        while not risar.klik:
            mx, my = risar.miska
            miska.setPos(mx, my)
            for i in range(len(krogi)):
                krog = krogi[i]
                krog.setPos(krog.x() + hitrost_x[i], krog.y() + hitrost_y[i])
                if not (13 < krog.x() < risar.maxX - 13):
                    hitrost_x[i] = -hitrost_x[i]
                if not (13 < krog.y() < risar.maxY - 13):
                    hitrost_y[i] = -hitrost_y[i]
            risar.cakaj(0.02)

        for i in range(len(krogi)):
            krog = krogi[i]
            krog.setPos(krog.x() + hitrost_x[i], krog.y() + hitrost_y[i])
            if not (13 < krog.x() < risar.maxX - 13):
                hitrost_x[i] = -hitrost_x[i]
            if not (13 < krog.y() < risar.maxY - 13):
                hitrost_y[i] = -hitrost_y[i]
            if ((krog.x() - mx) ** 2 + (krog.y() - my) ** 2) ** (1/2) <= 46:
                exit()
        risar.cakaj(0.02)

ocena_6()
ocena_7()
ocena_8()
