import risar
from random import randint
from math import *
import time

class Zoga:
    def __init__(self):
        self.speed_x = randint(-5, 5)
        self.speed_y = sqrt(5**2 - self.speed_x**2)

        self.x, self.y = risar.nakljucne_koordinate()

        self.krog = risar.krog(self.x, self.y, 10, risar.nakljucna_barva(), 5)

    def premik(self):
        if self.krog.x() > risar.maxX - 10 or self.krog.x() < 10:
            self.speed_x = -self.speed_x
        elif self.krog.y() > risar.maxY - 10 or self.krog.y() < 10:
            self.speed_y = -self.speed_y

        nx = self.x + self.speed_x
        ny = self.y + self.speed_y

        self.krog.setPos(nx, ny)

        self.x, self.y = nx, ny

zoge = []

start = time.time()
seconds = 20

for i in range(30):
    zoge.append(Zoga())

while time.time() < start + seconds:
    for i in range(30):
        zoge[i].premik()
    risar.cakaj(0.02)