import risar
from math import sqrt
import random
import collections

def sest():
    krogec = risar.krog(random.randint(10, risar.maxX - 10), random.randint(10, risar.maxY - 10), 10, barva=risar.nakljucna_barva())
    hx = random.randint(-5, 5)
    hy = sqrt(25 - hx ** 2)
    for i in range(660):
        krogec.setPos(krogec.x() + hx, krogec.y() + hy)
        if not (10 < krogec.x() < risar.maxX - 10):
            hx = -hx
        if not (10 < krogec.y() < risar.maxY - 10):
            hy = -hy
        risar.cakaj(0.02)



def sedem():
    krogeci = list()
    hitrostx = list()
    hitrosty = list()
    for i in range(30):
        krogec = risar.krog(random.randint(10, risar.maxX - 10), random.randint(10, risar.maxY - 10), 10, barva=risar.nakljucna_barva())
        hx = random.randint(-5, 5)
        hy = sqrt(25 - hx ** 2)
        krogeci.append(krogec)
        hitrostx.append(hx)
        hitrosty.append(hy)
    for e in range(660):
        for stev, krog in enumerate(krogeci):
            krog.setPos(krog.x() + hitrostx[stev], krog.y() + hitrosty[stev])
            if not (10 < krog.x() < risar.maxX - 10):
                hitrostx[stev] = -hitrostx[stev]
            if not (10 < krog.y() < risar.maxY - 10):
                hitrosty[stev] = -hitrosty[stev]
        risar.cakaj(0.02)
sedem()