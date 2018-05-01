from math import sqrt
import risar
import time
from random import randint, randrange, choice

class Krog:
    def __init__(self):
        self.x, self.y = risar.nakljucne_koordinate()
        self.r = 10
        self.xx = randrange(-5, 5)
        self.yy = sqrt(25 - self.xx**2)*choice([-1,1])
        self.body = risar.krog(self.x, self.y, self.r, barva=risar.nakljucna_barva(), sirina = 3)
        self.update()

    def update(self):
        self.body.setPos(self.x, self.y)
        risar.obnovi()

    def premikaj(self):
        if self.x >= risar.maxX or self.x <= 0:
            self.xx *= -1
        if self.y >= risar.maxY or self.y <= 0:
                self.yy *= -1
        self.x = self.x + self.xx
        self.y = self.y + self.yy
        self.update()

krogi = []
for i in range(30):
    k = Krog()
    k.angle = randint(0, 360)
    krogi.append(k)

konec = time.time() + 20
while time.time() < konec:
    k = choice(krogi)
    k.premikaj()
    if risar.klik == False:
        x,y = risar.miska
        veliki_krog = risar.krog(x,y, r=30, barva=risar.bela, sirina=3)
        veliki_krog.hide()
    else:
        stojeci_krog = risar.krog(x,y, r=30, barva=risar.bela, sirina=3)
        if abs(k.y - y) < 30 and abs(k.x - x) < 30:
            break

risar.besedilo(225, 175, "KONEC", barva = risar.rdeca, velikost=100,  pisava="Arial")
risar.stoj()