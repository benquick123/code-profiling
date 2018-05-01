from cmath import sqrt
from random import randint, random
import time

import risar

class Zoga:

    def __init__(self):
        self.r = 10
        self.x = randint(self.r, risar.maxX - self.r)
        self.y = randint(self.r, risar.maxY - self.r)
        self.v = 5
        self.vx = randint(-5, 5)
        self.vy = sqrt(self.v**2 - self.vx**2).real
        self.barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
        self.sirina = 5
        self.krog = risar.krog(self.x, self.y, self.r, self.barva, self.sirina)

    def premikanje(self):
        self.x += self.vx
        self.y += self.vy
        self.krog.setPos(self.x, self.y)

    def odbijanje(self):
        if self.x < self.r:
            self.vx = abs(self.vx)
        if self.x > risar.maxX - self.r:
            self.vx = -abs(self.vx)
        if self.y < self.r:
            self.vy = abs(self.vy)
        if self.y > risar.maxY - self.r:
            self.vy = -abs(self.vy)

zoge = []
for i in range(30):
    zoge.append(Zoga())

cas = time.time() + 20
while time.time() <= cas:
    for zoga in zoge:
        zoga.premikanje()
        zoga.odbijanje()
    risar.cakaj(0.02)