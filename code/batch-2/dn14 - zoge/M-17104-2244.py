import risar
import random
import math

#Za oceno 6
x,y = risar.nakljucne_koordinate()
barva = risar.nakljucna_barva()
lik = risar.krog(x, y, 12, barva=barva, sirina=4)
vx = random.randint(-5, 5)
smery = random.randint(1,2)
hip = 5

for i in range(600):
    lik.setX(x + vx)
    x += vx

    if smery == 1:
        lik.setY(y + math.sqrt(hip ** 2 - vx ** 2))
        y += math.sqrt(hip ** 2 - vx ** 2)
    elif smery == 2:
        lik.setY(y - math.sqrt(hip ** 2 - vx ** 2))
        y -= math.sqrt(hip ** 2 - vx ** 2)
    risar.cakaj(0.02)

    if x <= 0:
        vx = vx * -1

    elif x >= risar.maxX:
        vx = vx * -1

    elif y <= 0:
        if smery == 1:
            smery = 2
        elif smery == 2:
            smery = 1

    elif y > risar.maxY:
        if smery == 1:
            smery = 2
        elif smery == 2:
            smery = 1

#Za oceno 7
class Zoga:
    def __init__(self):
        self.x, self.y = risar.nakljucne_koordinate()
        self.barva = risar.nakljucna_barva()
        self.lik = risar.krog(self.x, self.y, 12, barva=self.barva, sirina=4)
        self.vx = random.randint(-5, 5)
        self.smery = random.randint(1, 2)
        self.hip = 5


    def premik(self):
        self.lik.setX(self.x + self.vx)
        self.x += self.vx

        if self.smery == 1:
            self.lik.setY(self.y + math.sqrt(self.hip ** 2 - self.vx ** 2))
            self.y += math.sqrt(self.hip ** 2 - self.vx ** 2)
        elif self.smery == 2:
            self.lik.setY(self.y - math.sqrt(self.hip ** 2 - self.vx ** 2))
            self.y -= math.sqrt(self.hip ** 2 - self.vx ** 2)

        if self.x <= 0:
            self.vx = self.vx * -1

        elif self.x >= risar.maxX:
            self.vx = self.vx * -1

        elif self.y <= 0:
            if self.smery == 1:
                self.smery = 2
            elif self.smery == 2:
                self.smery = 1

        elif self.y > risar.maxY:
            if self.smery == 1:
                self.smery = 2
            elif self.smery == 2:
                self.smery = 1

seznam = []
for i in range(30):
    i = Zoga()
    seznam.append(i)

for i in range(600):
    for i in seznam:
        i.premik()
    risar.cakaj(0.02)

risar.stoj()