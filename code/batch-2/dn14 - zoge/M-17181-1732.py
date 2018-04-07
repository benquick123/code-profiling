import risar
from random import randint
from math import sqrt


class zoga:

    def __init__(self):
        self.x, self.y = risar.nakljucne_koordinate()
        self.barva = risar.nakljucna_barva()
        self.premikx = randint(-5, 5)
        self.premiky = sqrt(25 - self.premikx ** 2)





    def premikanje(self):




        krog = risar.krog(self.x + self.premikx, self.y + self.premiky, 10, self.barva)

        if self.x + self.premikx < 0 or self.x + self.premikx > risar.maxX:
            self.premikx = -self.premikx

        if self.y + self.premiky < 0 or self.y + self.premiky > risar.maxY:
            self.premiky = -self.premiky

        risar.cakaj(0.02)
        risar.odstrani(krog)
        self.x += self.premikx
        self.y += self.premiky



krogi = []

for i in range(30):
    krogi.append(zoga())


premikx = randint(-5, 5)
premiky = sqrt(25 - premikx ** 2)

for i in range(800):            # pribl. 20sec
    krogi[1].premikanje()




