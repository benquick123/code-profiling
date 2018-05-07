import risar
import random
from math import *
import collections


class Krog(object):
    def __init__(self):
        self.x, self.y = random.randint(0, risar.maxX - 10), random.randint(0, risar.maxY - 10)
        self.barva = risar.nakljucna_barva()

    def krog6(self):
        krog = risar.krog(self.x, self.y, 10, self.barva)
        vx = random.randint(-5,5)
        vy = sqrt(5**2 - vx**2)
        for i in range(630):
            krog.setPos(krog.x() + vx, krog.y() + vy)
            if not (0 < krog.x() < risar.maxX):
                vx = -vx
            if not (0 < krog.y() < risar.maxY):
                vy = -vy
            risar.cakaj(0.02)

    def krog7(self):
        krogi = collections.defaultdict(list)
        for i in range(30):
            krog = risar.krog(random.randint(0, risar.maxX - 10), random.randint(0, risar.maxY - 10), 10,
                              risar.nakljucna_barva())
            vx = random.randint(-5, 5)
            vy = sqrt(5 ** 2 - vx ** 2)
            krogi[krog] = [vx, vy]
        for i in range(630):
            for krog, v in krogi.items():
                krog.setPos(krog.x() + v[0], krog.y() + v[1])
                if not (10 < krog.x() < risar.maxX - 10):
                    v[0] = -v[0]
                if not (10 < krog.y() < risar.maxY - 10):
                    v[1] = -v[1]
            risar.cakaj(0.02)

    



k = Krog()
k.krog7()