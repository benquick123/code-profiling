
import risar
from random import randint
from math import sqrt
class Krog:
    def __init__(self):
        self.polmer = 10
        self.x = randint(0 + self.polmer, risar.maxX - self.polmer)
        self.y = randint(0 + self.polmer, risar.maxY - self.polmer)
        self.barva = risar.nakljucna_barva()
        self.xHitrost = randint(-5,5)
        self.yHitrost = sqrt(5**2-self.xHitrost**2)


    def pojavitev(self):
        krog = risar.krog(self.x, self.y, self.polmer, self.barva)

    def premik(self):
        if not (0 + self.polmer< self.x < risar.maxX - self.polmer):
            self.xHitrost = -self.xHitrost
        if not (0 + self.polmer< self.y < risar.maxY - self.polmer):
            self.yHitrost = -self.yHitrost
        self.x += self.xHitrost
        self.y += self.yHitrost

krogi = []
for i in range(30):
    krogi.append(Krog())

for i in range(400):
    risar.pobrisi()
    for krog in krogi:
        krog.pojavitev()
        krog.premik()
    risar.cakaj(0.02)