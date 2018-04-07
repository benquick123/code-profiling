import risar
from random import randint
from math import *
import time
from risar import stoj

class Zoga:
    def __init__(self):
        self.x = risar.maxX * randint(11, 89) / 100
        self.y = risar.maxY * randint(11, 89) / 100
        self.angle = randint(0, 360)
        self.body = risar.krog(self.x, self.y, 10, risar.nakljucna_barva(), 2)
        self.speed = 5
        self.update()

    def update(self):
        self.body.setPos(self.x, self.y)
        risar.obnovi()


    def move(self):
        phi = radians(self.angle)
        self.x = self.x + self.speed * cos(phi)
        self.y = self.y - self.speed * sin(phi)
        if self.y < 10:
            self.angle = 360 - self.angle
        if self.y > risar.maxY - 10:
            self.angle = 360 - self.angle
        if self.x < 10:
            self.angle = 180 - self.angle
        if self.x > risar.maxX - 10:
            self.angle = 180 - self.angle
        self.update()
        #risar.cakaj(0.2)



"""z = Zoga()
t_end = time.time() + 60

while time.time() < t_end:
    z.move()"""


zoge = []

for i in range(1, 30):
    zoge.append(Zoga())

t_end = time.time() + 20
while time.time() < t_end:
    for zoga in zoge:
        zoga.move()



risar.stoj()