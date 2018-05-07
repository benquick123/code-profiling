import risar
from math import sqrt
from random import randint
from time import *

class Zoga:
    def __init__(self):
        self.x = randint(0,risar.maxX)
        self.y = randint(0,risar.maxY)
        self.r = 10
        self.barva = risar.nakljucna_barva()
        self.hitrost = 5
        self.xx = randint(-self.hitrost,self.hitrost)
        self.yy = sqrt(self.hitrost **2 - self.xx **2)
        self.krog = risar.krog(self.x, self.y, self.r, self.barva)

    def premik(self):
        self.x += self.xx
        self.y += self.yy
        self.krog.setPos(self.x, self.y)

    def stene(self):
        if self.x < self.r:
            self.xx = abs(self.xx)
        if self.x > risar.maxX - self.r:
            self.xx = -abs(self.xx)
        if self.y < self.r:
            self.yy = abs(self.yy)
        if self.y > risar.maxY - self.r:
            self.yy = -abs(self.yy)

def koliko(x):
    zoge = []
    for i in range(1, x, 1):
        zoge.append(Zoga())
    return zoge
def start():
    dela = True
    krogi = koliko(30)
    cas = time()
    while dela and (time() - cas <= 20):
        for zoga in krogi:
            zoga.premik()
            zoga.stene()
        risar.cakaj(0.02)
start()