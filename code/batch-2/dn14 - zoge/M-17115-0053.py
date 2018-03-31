import risar
import random
from math import sqrt

class Reaction():
    def __init__(self):
        self.x,self.y = risar.nakljucne_koordinate()
        barva = risar.nakljucna_barva()
        self.krog = risar.krog(self.x,self.y,10,barva)
        self.h = 5
        self.hx = random.randint(-5,5)
        self.hy = sqrt(self.h**2 - self.hx**2)

    def move(self):
        self.x += self.hx
        self.y += self.hy
        self.krog.setPos(self.x, self.y)
        risar.obnovi()
        Reaction.wall(self)

    def wall(self):
        if self.x <= 10:
            self.hx = abs(self.hx)
        elif self.x >= risar.maxX-10:
            self.hx = -abs(self.hx)
        if self.y <= 10:
            self.hy = abs(self.hy)
        elif self.y >= risar.maxY -10:
            self.hy = -abs(self.hy)

k = Reaction()
for i in range(650):
    k.move()
    risar.cakaj(0.02)



