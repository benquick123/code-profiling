import risar
import random
from random import randint
import math
import time

class Krog:

    def __init__(self):
        zacetna     = self.zaceznaPozicija()
        self.x      = zacetna[0]
        self.y      = zacetna[1]
        self.vX     = random.uniform(-5.0, 5.0)
        self.vY     = randint(0, 1)
        self.polmer = 10
        self.barva  = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
        self.sirina = 2
        self.krog   = risar.krog(self.x, self.y, self.polmer, self.barva, self.sirina)

    def zaceznaPozicija(self):
        while(1):
            tmp = risar.nakljucne_koordinate()
            if tmp[0] >= 15 and tmp[0] <= risar.maxX - 15 and tmp[1] >= 15 and tmp[1] <= risar.maxY - 15:
                return tmp

    def novaPozicija(self):
        self.x += self.vX
        if self.vY:
            self.y += math.sqrt(5**2 - self.vX**2)
        else:
            self.y -= math.sqrt(5**2 - self.vX**2)

    def preveri(self):
        if self.x > risar.maxX - 15 or self.x < 15:
            self.vX *= -1
        if self.y > risar.maxY - 15:
            self.vY = False
        if self.y < 15:
            self.vY = True

krogci = []
for i in range(30):
    krogci.append(Krog())

risar.cakaj(0.5)
konec = time.time() + 20

while(1):
    if time.time() > konec:
        break

    for a in krogci:
        a.preveri()
        a.novaPozicija()
        a.krog.setPos(a.x, a.y)

    risar.obnovi()
    risar.cakaj(0.02)
