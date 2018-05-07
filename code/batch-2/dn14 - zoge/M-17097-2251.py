#coding=utf-8
#from __future__ import unicode_literals
from math import *
import risar
from random import randint



class Krog:

    def __init__(self):

        self.x = randint(10, risar.maxX-15)
        self.y = randint(10, risar.maxY-15)
        self.r = 10
        self.xh = randint(-5, 5)
        self.yh = sqrt(25 - self.xh ** 2)
        self.barva = risar.nakljucna_barva()
        self.krog = risar.krog(self.x, self.y, self.r, self.barva, 3)


    def narisi(self):

        self.krog.setPos(self.krog.x() + self.xh, self.krog.y() + self.yh)

        if (self.krog.x() > risar.maxX - 10 or self.krog.x() < 10):
             self.xh = -self.xh
        if (self.krog.y() > risar.maxY - 10 or self.krog.y() < 10):
            self.yh = -self.yh




krogi = []
for i in range(30):
    krogi.append(Krog())


for i in range(1000):
    for j in range(len(krogi)):
        krogi[j].narisi()
        risar.cakaj(0.000002)
