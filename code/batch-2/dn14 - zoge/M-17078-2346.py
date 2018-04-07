import risar
from random import *
from math import *
from PyQt5.QtWidgets import QMessageBox


class Kroglica:

    def __init__(self):
        self.r = 10
        self.x, self.y = (randint(10, risar.maxX-10), randint(10, risar.maxY-10))
        self.barva = risar.nakljucna_barva()
        self.sx = self.sy = 1
        self.kx = randint(-5, 5)
        self.ky = sqrt(25 - self.kx ** 2)
        self.razstreljen = False
        self.cas = -1
        self.izbrisan = False

    def narisi(self):
        self.krogec = risar.krog(self.x, self.y, self.r, self.barva, 1)

    def miskica(self):
        self.x, self.y = risar.miska
        self.r = 30
        self.klik = False
        return self.x, self.y, self.klik

    def razstreli(self):
        self.krogec.hide()
        self.r = 30
        self.narisi()
        c = self.krogec.pen().color().lighter()
        c.setAlpha(192)
        self.krogec.setBrush(c)
        self.razstreljen = True

def premakni(self):
    if self.x + self.kx * self.sx < 0 + self.r or self.x + self.kx * self.sx > risar.maxX - 1 - self.r:
        self.sx *= -1
    if self.y + self.ky * self.sy < 0 + self.r or self.y + self.ky * self.sy > risar.maxY - 1 - self.r:
        self.sy *= -1
    self.x += self.kx * self.sx
    self.y += self.ky * self.sy
    self.krogec.setPos(self.x, self.y)
    return self.x, self.y

def premaknimisko(self):
    if not risar.klik:
        self.x, self.y = risar.miska
        self.krogec.setPos(self.x, self.y)
    else:
        self.klik = True
    return self.x, self.y, self.klik

def gas(tab, tmp, z):
    risar.klik = 0
    QMessageBox.information(None, "Stopnja {i}".format(i=tmp+1), "Število žog: {z}\nPotrebnih: {p}".format(z=z, p=(tmp+1)*3))
    razstreljenih = 0
    nadaljuj = -1
    miska = Kroglica()
    mx, my, klik = miska.miskica()
    miska.narisi()
    for i in range(1000):
        for krog in tab:
            if not krog.razstreljen:
                kx, ky = premakni(krog)
            if (mx + 30 > kx + 10 > mx - 30 or mx + 30 > kx - 10 > mx - 30) and \
               (my + 30 > ky + 10 > my - 30 or my + 30 > ky - 10 > my - 30) and klik == 1 and not krog.razstreljen:
                krog.razstreli()
                krog.cas = i
                razstreljenih += 1
            if krog.razstreljen:
                if krog.cas < i - 200:
                    krog.krogec.hide()
                    krog.izbrisan = True
            if krog.razstreljen and not krog.izbrisan:
                nadaljuj = 1
        if nadaljuj == 0 or razstreljenih >= (tmp+1)*3:
            return razstreljenih
        elif nadaljuj == 1:
            nadaljuj = 0
        mx, my, klik = premaknimisko(miska)
        risar.cakaj(0.02)


#ZA OCENO 10

z = 40 #število žog na začetku

for i in range(10):
    risar.pobrisi()
    tab = [Kroglica() for krog in range(z-i)]
    for krog in tab:
        krog.narisi()
    score = gas(tab, i, z-i)
    if score >= i*3:
        QMessageBox.information(None, "Bravo", "Eksplodiralo je {s} žog. Greste v naslednji krog.".format(s=score))
    else:
        QMessageBox.information(None, "Konec igre", "Eksplodiralo je {s} žog. Žal je to premalo.".format(s=score))
        break


risar.stoj()