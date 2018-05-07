import risar
from random import *
from math import sqrt
import time
class Zoge:
    def __init__(self,r):
        self.r = r

        self.x = randint(self.r, risar.maxX - self.r)
        self.y = randint(self.r, risar.maxY - self.r)

        v = 5
        tab=[-1,1]
        self.vx = randint(-v, v)
        self.vy = sqrt(v**2 - self.vx**2) * tab[randint(0, len(tab)-1)]
        self.krog = risar.krog(self.x, self.y, self.r, risar.nakljucna_barva())

    def premiki(self):
        self.x += self.vx
        self.y += self.vy
        self.krog.setPos(self.x, self.y)

    def odbij(self):
        if self.x < self.r:
            self.vx = abs(self.vx)
        if self.x > risar.maxX - self.r:
            self.vx = -abs(self.vx)
        if self.y < self.r:
            self.vy = abs(self.vy)
        if self.y > risar.maxY - self.r:
            self.vy = -abs(self.vy)

    def sledi(self):
        a = risar.miska
        self.x = a[0]
        self.y = a[1]
        if risar.klik == False:
            self.premiki()
    def koor(self):
        return (self.x,self.y)

t_end = time.time() + 20
k = []
t = Zoge(30)
for i in range(30):
    k.append(Zoge(10))
while time.time() < t_end:
    t.sledi()
    for j in k:
        j.premiki()
        j.odbij()
    risar.cakaj(0.02)
risar.stoj()
