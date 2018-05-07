from random import randint, choice
from math import *
from time import *
import risar



class Zoge:
    def __init__(self):
        hitrost = list(range(-5, 5 + 1))
        hitrost.remove(0)
        self.x = randint(15, risar.maxX - 15)
        self.y = randint(15, risar.maxY - 15)
        self.angle = round(radians(randint(1, 361)))
        self.speed = choice(hitrost)
        self.color = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
        self.krog = risar.krog(self.x, self.y, 10, self.color, 4)


    def odboj(self):
        while time() < koncaj:
            self.x = self.x + self.speed * sin(self.angle)
            self.y = self.y - self.speed * cos(self.angle)
            self.krog.setPos(self.x, self.y)
            risar.cakaj(0.02)
            if self.x >= risar.maxX - 10 or self.x <= 10:
                self.angle -= 2 * self.angle
            elif self.y >= risar.maxY - 15 or self.y <= 15:
                self.angle -= 2 * self.angle
                self.speed -= 2 * self.speed


koncaj = time() + 20
a = Zoge()
a.odboj()



