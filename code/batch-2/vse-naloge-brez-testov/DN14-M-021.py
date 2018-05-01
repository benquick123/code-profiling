import risar
import math
import time
import random


class  Ball:
    def __init__(self):
        #self.x,self.y = risar.nakljucne_koordinate()
        self.x, self.y = random.randint(10, risar.maxX-10), random.randint(10, risar.maxY-10)
        self.r = 10
        self.colour = risar.nakljucna_barva()
        self.vX = random.randint(-5, 5)
        self.vY = math.sqrt(25-self.vX**2)
        self.circle = risar.krog(self.x, self.y, self.r, self.colour, 1)

class Mice:
    def __init__(self):
        self.x,self.y=risar.miska
        self.r = 30
        self.colour = risar.nakljucna_barva()
        self.circle = risar.krog(self.x, self.y, self.r, self.colour, 2)



zoge = []

for i in range(30):
    zoge.append(Ball())

mrice = Mice()
status = 0
end_prog = time.time() + 20
while time.time() < end_prog:
    if not risar.klik:
        mrice.x, mrice.y = risar.miska
        mrice.circle.setPos(mrice.x,mrice.y)
    else:
        status=1
    for zoga in zoge:
        zoga.x+=zoga.vX
        zoga.y += zoga.vY
        if zoga.x > risar.maxX - zoga.r or zoga.x < zoga.r:
            zoga.vX *= -1
        if zoga.y > risar.maxY - zoga.r or zoga.y < zoga.r:
            zoga.vY *= -1
        zoga.circle.setPos(zoga.x,zoga.y)
        if mrice.circle.collidesWithItem(zoga.circle) and status == 1:
            exit()
    risar.cakaj(0.02)

risar.stoj()

