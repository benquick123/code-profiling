import risar
import time
from random import randint,randrange
import math

t_end = time.time() + 20

class krog():
    def __init__(self,dx,dy):
        self.x, self.y = risar.nakljucne_koordinate()
        self.barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
        self.r = 10
        self.k = risar.krog(self.x, self.y, self.r, self.barva, 3)
        self.h = 5
        self.dx = randrange(1,5)
        self.dy = math.sqrt(self.h*self.h - self.dx-self.dx)

    def preveri(self):
        if (self.x <= self.r or self.x >= 800 - self.r):
            self.dx= -self.dx

        if (self.y <= self.r or self.y >= 500 - self.r):
            self.dy = -self.dy


class miska():
    def __init__(self):
        self.x,self.y = risar.miska


c= []
dx = randint(-5,5)
dy = randint(-5,5)
for n in range(30):
    c.append(krog(dx,dy))



risar.obnavljaj = True
t = 0.02
m = miska()

while time.time() < t_end:
    #risar.crta(0,250,600,250,risar.crna,500)
    for i in c:
        #c[i].hide()
        i.preveri()
        i.x += i.dx
        i.y += i.dy
        i.k.setPos(i.x,i.y)
    risar.obnovi()
    risar.cakaj(t)





risar.stoj()