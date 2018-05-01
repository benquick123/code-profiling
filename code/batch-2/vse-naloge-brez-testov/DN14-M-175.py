import risar
import math
import random

class Zoga:
    def __init__(self):
        self.x, self.y = risar.nakljucne_koordinate()

        self.r = 10

        self.barva = risar.nakljucna_barva()

        self.krog = risar.krog(self.x, self.y, self.r, self.barva)

        self.dx = random.randint(-5, 5)
        self.dy = math.sqrt(25 - self.dx**2)

    def tick(self):

        self.x += self.dx
        self.y += self.dy

        if self.x < self.r:
            self.dx = abs(self.dx)
        if self.y < self.r:
            self.dy = abs(self.dy)
        if self.x > risar.maxX - self.r:
            self.dx = -abs(self.dx)
        if self.y > risar.maxY - self.r:
            self.dy = -abs(self.dy)

        self.krog.setPos(self.x, self.y)

def evklidska_razdalja(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


zoge = [Zoga() for i in range(30)]

konec = False

krog_miska = risar.krog(risar.miska[0], risar.miska[1], 30)

while not konec:
    for zoga in zoge:
        zoga.tick()

    if not risar.klik:
        krog_miska.setPos(risar.miska[0], risar.miska[1])
    else:
        for zoga in zoge:
            if evklidska_razdalja(zoga.x, zoga.y, krog_miska.x(), krog_miska.y()) < zoga.r + 30:
                konec = True

    risar.cakaj(0.02)


risar.stoj()