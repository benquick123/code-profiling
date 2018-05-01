import risar
from math import *
from random import *


# import time


class zoga:
    def __init__(self):
        a, b = risar.nakljucne_koordinate()
        self.x = abs(a - 12)
        self.y = abs(b - 12)
        self.barva = risar.nakljucna_barva()
        self.zoga = risar.krog(self.x, self.y, 10, barva=self.barva, sirina=2)
        self.sx = uniform(-5, 5)
        self.sy = (5 * 5 - self.sx * self.sx) ** 0.5

    def skrijse(self):
        self.zoga.hide()


xm, ym = risar.miska
krogmis = risar.krog(xm, ym, 30, barva=risar.bela, sirina=2)

zoge = [zoga() for i in range(30)]
# poknenezoge = []
# start = time.time()
# ta zanka je preoblikovan program iz predavanj.
for i in range(950):
    for i in zoge:
        i.zoga.setPos(i.zoga.x() + i.sx, i.zoga.y() + i.sy)
        if not (0 < i.zoga.x() < risar.maxX - 12):
            i.sx = -i.sx
        if not (0 < i.zoga.y() < risar.maxY - 12):
            i.sy = -i.sy
        if risar.klik == False:
            xm, ym = risar.miska
            krogmis.setPos(xm, ym)
        else:
            razdaljax = i.zoga.x() - xm
            razdaljay = i.zoga.y() - ym
            razdalja = ((razdaljax * razdaljax) + (razdaljay * razdaljay)) ** 0.5
            if razdalja <= 42:
                risar.stoj()
                # i.zoga.setRect(-30, -30, 60, 60)
                # poknenezoge.append(i)
                # zoge.remove(i)
                # i.skrijse()
    risar.cakaj(0.02)
# stop = time.time()
# print("cas je: ", stop - start)
risar.stoj()
