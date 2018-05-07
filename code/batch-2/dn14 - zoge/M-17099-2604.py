import risar
from random import *
from math import *
from PyQt5.QtWidgets import QMessageBox




class Krog:
    def __init__(self):
        from random import randint
        self.x, self.y = randint(10, risar.maxX - 10), randint(10, risar.maxY - 10)
        self.r = 10
        self.barva = risar.nakljucna_barva()
        self.kx = randint(-5, 5)
        self.ky = sqrt(25 - self.kx ** 2)

    def narisi(self):
        risar.krog(self.x, self.y, self.r, self.barva, 1)

    def premikanje(self):
        kroglica = risar.krog(self.x + self.kx, self.y + self.ky, self.r, self.barva, 1)
        risar.cakaj(0.02)
        if (self.x + self.kx < 10) or (self.x + self.kx > risar.maxX + 10):
            self.kx *= -1

        if (self.y + self.ky < 10) or (self.y + self.ky > risar.maxY + 10):
            self.ky *= -1

        risar.odstrani(kroglica)
        self.x += self.kx
        self.y += self.ky

vec_krogov = []
for i in range(30):
    vec_krogov.append(Krog())

for i in range(1000):
        vec_krogov[1].premikanje()
        #vec_krogov[2].premikanje() noce delati



#for i in range(1000):








