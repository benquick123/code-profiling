import risar
from math import *
from random import *
class zoga():
    def __init__(self):
        self.a = risar.krog(randint(10,risar.maxX-11),randint(10,risar.maxY-11),10,risar.nakljucna_barva(),1)
        self.x = randint(-5,5)
        self.y = sqrt(25 -(self.x*self.x))
    def premik(self):
        self.a.setPos(self.a.x() + self.x, self.a.y() + self.y)
        if self.a.x() <= 10 or self.a.x() >= risar.maxX-10:
            self.x = -self.x
        if self.a.y() <= 10 or self.a.y() >= risar.maxY-10:
            self.y = -self.y
polje = []
for i in range(30):
    polje.append(zoga())
for i in range(1000):
     for zoga in polje:
         zoga.premik()
     risar.cakaj(0.02)
