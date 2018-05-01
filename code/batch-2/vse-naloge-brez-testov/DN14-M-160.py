import risar
import math
import time
from random import randint, uniform



class Krog:
    def __init__(self):
        self.x, self.y = (randint(10, risar.maxX - 10), randint(10, risar.maxY-10))
        self.barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
        self.c = (uniform(-5.0, 5.0))
        self.hitrost = [self.c, math.sqrt((5*5)-(self.c*self.c))]
        self.life = True
        self.circle = risar.krog(self.x, self.y, 10, self.barva, 3)
        self.PERIOD_OF_TIME = 20

    def zacni(self):
            self.x = self.x + self.hitrost[0]
            self.y = self.y + self.hitrost[1]
            self.circle.setPos(self.x, self.y)
            if not (0 < self.x < risar.maxX - 10):
                self.hitrost[0] = -1 * self.hitrost[0]
                if self.life:
                    self.start = time.time()
                    self.life = False
            if not (0 < self.y < risar.maxY - 10):
                self.hitrost[1] = -1 * self.hitrost[1]
                if self.life:
                    self.start = time.time()
                    self.life = False
            if not self.life:
                if time.time() > self.start + self.PERIOD_OF_TIME:
                    risar.stoj()



krogi = []
for i in range(30):
    k = Krog()
    krogi.append(k)

while True:
    for i in krogi:
        i.zacni()
    risar.cakaj(0.02)




