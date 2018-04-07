import risar
from random import *
from math import *
class Krog():
    def __init__(self):
        maxsirina = risar.maxX - 12
        maxvisina = risar.maxY - 12
        self.x = randint(10, maxsirina)
        self.y = randint(10, maxvisina)
        self.xspeed = randint(-5, 5)
        self.yspeed = sqrt(25- pow(self.xspeed, 2))
        self.krog = risar.krog(self.x, self.y, 10, risar.nakljucna_barva(), 2)

    def sprememba(self):
        if self.y < 10 or self.y > (risar.maxY -12):
            self.yspeed = -self.yspeed
        if self.x < 10 or self.x > (risar.maxX - 12):
            self.xspeed = -self.xspeed

        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed
        self.krog.setPos(self.x, self.y)
class Krogkurzor():
    def __init__(self):
        self.krog = risar.krog(risar.miska[0], risar.miska[1], 30, risar.bela , 2)

def Program_zog():
    PoljeKrogov = []
    for i in range(30):
        PoljeKrogov.append(Krog())
    krogkurzor = Krogkurzor()
    stevec = 900
    while stevec > 0:
        for i in PoljeKrogov:
            if risar.klik == False:
                krogkurzor.krog.setPos(risar.miska[0], risar.miska[1])
                krogkurzor.x, krogkurzor.y = risar.miska[0], risar.miska[1]

            if risar.klik == True and sqrt(((krogkurzor.x - i.x)**2)+((krogkurzor.y - i.y)**2)) <= 40:
                risar.stoj()

            i.sprememba()
        risar.cakaj(0.02)
        stevec -= 1
    risar.stoj()

Program_zog()