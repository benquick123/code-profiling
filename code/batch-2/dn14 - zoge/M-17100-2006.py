import risar
import time
from random import randint, choice
from math import sqrt

class krogci:
    def __init__(self, existing = []):
        self.r = 10
        self.x = randint(self.r, risar.maxX - self.r)
        self.y = randint(self.r, risar.maxY - self.r)
        hitrost = 5
        self.hitrost = 5
        vx = randint(-hitrost, hitrost)
        vy = sqrt(hitrost ** 2 - vx ** 2)
        self.vx = vx
        self.vy = vy
        self.barva = risar.nakljucna_barva()
        self.krog = risar.krog(self.x, self.y, self.r, barva= self.barva, sirina = 1)

    def meje(self):
        if self.x < self.r:
            self.vx = abs(self.vx)
        elif self.x > risar.maxX - self.r:
            self.vx = -abs(self.vx)
        elif self.y < self.r:
            self.vy = abs(self.vy)
        elif self.y > risar.maxY - self.r:
            self.vy = -abs(self.vy)

    def premakni(self):
        self.x += self.vx
        self.y += self.vy
        self.krog.setPos(self.x, self.y)

t = krogci()

i = 0
while i < 1000:
    t.premakni()
    t.meje()
    risar.cakaj(0.02)
    i += 1

risar.stoj()

#def postavitev():
    #mehurcki = []
    #for i in range(30):
        #mehurcki.append(krogci(existing = mehurcki))
    #return mehurcki

#def zacetek():
    #mehurcki = postavitev()
    #i = 0
    #while i < 1000:
        #if time.time() - zacetni_cas == 0:
            #risar.exit()
        #else:
            #for i, j in enumerate(mehurcki):
                #j.premakni()
                #j.meje()

            #risar.cakaj(0.02)
            #i += 1



#zacetni_cas = time.time()
#zacetek()











