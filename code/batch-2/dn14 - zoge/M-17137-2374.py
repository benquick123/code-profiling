from random import randint
from math import *
import time
import risar
class Ball:
    def __init__(self):
        barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
        self.barva = barva
        self.krog = risar.krog(0, 0, 10, barva, 3)
        self.x = randint(0,risar.maxX)
        self.y = randint(0,risar.maxY)
        self.angle = randint(0,360)
        self.hitrostx = randint(-5,5)
        self.hitrosty = sqrt(25- self.hitrostx**2)
        self.refresh()

    def refresh(self):
        self.krog.setPos(self.x, self.y)

    def gas(self):
        if self.x < 20:
            self.x = 20
        if self.y < 20:
            self.y = 20
        if self.x > risar.maxX -20:
            self.x = risar.maxX -21
        if self.y > risar.maxY -20:
            self.y = risar.maxY -21
        if self.hitrostx == 0:
            self.hitrostx = 1



        while cas > time.time():

            nx = self.x + self.hitrostx
            ny = self.y + self.hitrosty
            self.x = nx
            self.y = ny
            self.refresh()

            if not 10 < self.x <risar.maxX-11:
                self.hitrostx = - self.hitrostx
            if not 10 < self.y <risar.maxY-11:
                self.hitrosty = -self.hitrosty


            risar.cakaj(0.02)






a = Ball()
dvajest = 20
cas = time.time() + dvajest
a.gas()



