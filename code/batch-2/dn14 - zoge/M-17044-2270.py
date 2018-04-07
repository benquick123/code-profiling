import risar
from random import *
from math import *
import time



class Zoge:
    def __init__(self, obstojece=()):
        self.polmer = 10
        self.x = randint(self.polmer, risar.maxX - self.polmer)
        self.y = randint(self.polmer, risar.maxY - self.polmer)
        self.hitrost_x = randint(-5, 5)
        self.hitrost_y = sqrt(5**2 - self.hitrost_x**2)
        self.barva = risar.nakljucna_barva()
        self.krog = risar.krog(self.x, self.y, self.polmer, self.barva, 3)

    def move(self):
        self.x += self.hitrost_x
        self.y += self.hitrost_y
        self.krog.setPos(self.x, self.y)

    def stene(self):
        if self.x < self.polmer:
            self.hitrost_x = abs(self.hitrost_x)
        else:
            if self.x > risar.maxX - self.polmer:
                self.hitrost_x = -abs(self.hitrost_x)
        if self.y < self.polmer:
            self.hitrost_y = abs(self.hitrost_y)
        else:
            if self.y > risar.maxY - self.polmer:
                self.hitrost_y = -abs(self.hitrost_y)


zoge = []
for i in range(30):
    zoge.append(Zoge(obstojece=zoge))

konec = time.time() + 20
while time.time() < konec:
    for k in zoge:
        k.move()
        k.stene()

    risar.cakaj(0.02)