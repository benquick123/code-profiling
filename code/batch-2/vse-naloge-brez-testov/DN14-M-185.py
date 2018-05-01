import risar
from random import *
from math import sqrt





class Zoge():

    def __init__(self, x=None, y=None, vx=None, vy=None, barva=None):

        if x is None and y is None:
            x , y = risar.nakljucne_koordinate()

        self.x = x
        self.y = y

        if vx is None or vy is None:
            v = randint(5, 10)
            vx = randint(-v, v)
            vy = sqrt(v ** 2 - vx ** 2) #* random.choice[-1, 1]
        self.vx = vx
        self.vy = vy

        if barva is None:
            barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))

        self.krog = risar.krog(self.x, self.y, 10, barva, sirina = 2)

    def getxy(self):
        return self.x,self.y

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.krog.setPos(self.x, self.y)

    def walls(self):
        if self.x < 10:
            self.vx = abs(self.vx)
        if self.x > risar.maxX - 10:
            self.vx = -abs(self.vx)
        if self.y < 10:
            self.vy = abs(self.vy)
        if self.y > risar.maxY - 10:
            self.vy = -abs(self.vy)

class Miska():

    def __init__(self, x=None, y=None):

        self.x, self.y = risar.miska

        self.miska = risar.krog(self.x, self.y, 30, sirina = 2)

    def update(self):
        self.x, self.y = risar.miska
        self.miska.setPos(self.x, self.y)

    def getxy(self):
        return self.x, self.y

t = Miska()
x = []

for i in range(30):
    x.append(i)
for i in range(30):
    x[i] = Zoge()
for l in range(1000):
    brejk = False
    for i in range(30):
        x[i].move()
        x[i].walls()
        if not risar.klik:
            t.update()
        else:
            a,b = x[i].getxy()
            c,d = t.getxy()
            d = sqrt((c-a)**2 + (d-b)**2)
            if d < 45:
                brejk = True
                break
    if brejk == True:
        break
    risar.cakaj(0.02)
risar.stoj()