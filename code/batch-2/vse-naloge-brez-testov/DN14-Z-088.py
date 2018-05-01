# Za oceno 6
import risar
from random import randint
from math import sqrt
import random

class Skokica:
    def __init__(self):
        self.x, self.y = risar.nakljucne_koordinate()
        self.barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
        self.body = risar.krog(self.x, self.y, 10, barva=self.barva)
        s = []
        for i in range(-5, 5):
            for j in range(-5, 5):
                if i**2 + j**2 == 5**2:
                    s.append((i,j))
        self.vx, self.vy = random.choice(s)

    def update(self):
        self.body.setPos(self.x, self.y)

    def forward(self):
        self.y += self.vy
        self.x += self.vx
        if not (5 <= self.x <= risar.maxX-5):
            self.vx = -self.vx
        if not (5 <= self.y <= risar.maxY-5):
            self.vy = -self.vy
        self.update()

class VojskaSkokic:
    def __init__(self, stevilo):
        self.stevilo = stevilo
        self.vse_skokice = []
        for i in range(stevilo):
            skokica = Skokica()
            self.vse_skokice.append(skokica)

    def forward(self):
        for skokica in self.vse_skokice:
            skokica.forward()
        risar.obnovi()


skokica = VojskaSkokic(30)
for i in range(0,10000000000):
    skokica.forward()
    risar.cakaj(0.02)
risar.stoj()