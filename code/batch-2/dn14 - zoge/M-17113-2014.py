import risar
from math import radians,cos,sin,sqrt
import time

class zoga:
    def __init__(self):
        from random import randint
        self.x,self.y = randint(20, risar.maxX-20), randint(20, risar.maxY-20)

        self.xSpd = randint(-5,5)
        self.ySpd = int(sqrt(25 - self.xSpd**2))

        self.radi = 15
        self.crta = 3
        self.barva = risar.nakljucna_barva()
        self.krogec = risar.krog(self.x, self.y, self.radi, self.barva, self.crta)

        self.moving = True

        self.TTL = 0

    def move(self):
        self.x += self.xSpd
        self.y += self.ySpd
        self.krogec.setPos(self.x, self.y)
        if self.x not in range(15,risar.maxX-15):
            self.xSpd *= -1
        if self.y not in range(15,risar.maxY-15):
            self.ySpd *= -1

    def explode(self):
        self.moving = False
        self.krogec.setRect(-40,-40,80,80)
        c = self.krogec.pen().color().lighter()
        c.setAlpha(192)
        self.krogec.setBrush(c)

        self.TTL = time.time()


class miš:
    def __init__(self):
        self.x, self.y = 0, 0
        self.radi = 40
        self.crta = 3
        self.barva = risar.bela
        self.krogec = risar.krog(self.x, self.y, self.radi, self.barva, self.crta)

        self.postavljen = False

    def sledi(self):
        if not self.postavljen:
            self.x,self.y = risar.miska
            self.krogec.setPos(self.x,self.y)

    def postaviKrog(self):
        self.postavljen = True
        c = self.krogec.pen().color().lighter()
        c.setAlpha(192)
        self.krogec.setBrush(c)


mouse = miš()

list=[]
while len(list) < 30:
    list.append(zoga())

brah = time.time()
nekaj = True


while(brah + 20 >= time.time() and nekaj == True):


    for a in list:
        if a.moving:
            a.move()
        if mouse.postavljen and mouse.radi+a.radi >= sqrt((a.x - mouse.x)**2 +(a.y - mouse.y)**2):
            a.explode()
            nekaj = False

    mouse.sledi()
    if risar.klik:
        mouse.postaviKrog()
    risar.cakaj(0.01)
    risar.cakaj(0.01)
