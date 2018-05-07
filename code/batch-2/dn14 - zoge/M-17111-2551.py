from math import sqrt
from random import *
import random
from time import sleep, time

import risar

class Zoga: #ustvaril sem razred Zoga, v katerem naredim zogo
    def __init__(self): #zogici dolocim njene lastnosti
        self.x = random.randint(11, risar.maxX-11)
        self.y = random.randint(11, risar.maxY-11)
        self.nakljucna_barva = risar.nakljucna_barva()
        self.krog = risar.krog(self.x, self.y, 10, barva=self.nakljucna_barva, sirina=3)
        self.smerx = random.uniform(-5,5)
        self.hitrost = 5
        self.smery = sqrt(self.hitrost ** 2 - self.smerx ** 2) #komponentoy računam po pitagorovem izreku (hitrost je hipotenuza c)


    def gibanje_zogice(self):
        self.x += self.smerx

        self.y += self.smery

        maxX = risar.maxX
        maxY = risar.maxY

        if not (10 <= self.x <= maxX-10):
            self.smerx = -self.smerx            #odboj (smer negativna ko pride do roba)
        if not (10 <= self.y <= maxY-10):
            self.smery = -self.smery

        self.krog.setPos(self.x, self.y)


cajtek = time()+20
seznam_zog = []

#Najprej v seznam_zog shranim 30 zog, ki jih kasneje znova
for a in range(0, 30):
    seznam_zog.append(Zoga())

while(time()<=cajtek):
    for a in range(0, 30):
        zogica = seznam_zog[a]
        zogica.gibanje_zogice()


    risar.obnovi()
    risar.cakaj(0.02)
