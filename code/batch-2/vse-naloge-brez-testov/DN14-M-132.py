import risar
from random import randint
from math import sqrt
from PyQt5.QtWidgets import QMessageBox


class Krog:
    def __init__(self, x = None, y = None, r = None, v = None, barva = None):
        if r is None:
            self.r = 10
        else:
            self.r = r
        if x is None or y is None:
            self.x = randint(self.r, risar.maxX - self.r)
            self.y = randint(self.r, risar.maxY - self.r)
        else:
            self.x = x
            self.y = y
        if v is None:
            v = 5
        self.vx = randint(-v, v)
        self.vy = sqrt(v ** 2 - self.vx ** 2)
        self.eksplodiran = False
        self.lifetime = 0.00
        if barva is None:
            self.barva = risar.nakljucna_barva()
        else:
            self.barva = barva
        self.krog = risar.krog(self.x, self.y, self.r, self.barva, 6)

    def premik(self):
        if not self.eksplodiran:
            self.x += self.vx
            self.y += self.vy
            self.setPosition(self.x, self.y)
            self.stene()

    def stene(self):
        # Leva stena
        if self.x < self.r:
            self.vx = abs(self.vx)
        # Desna stena
        if self.x > risar.maxX - self.r:
            self.vx = -abs(self.vx)
        # Zgornja stena
        if self.y < self.r:
            self.vy = abs(self.vy)
        # Spodnja stena
        if self.y > risar.maxY - self.r:
            self.vy = -abs(self.vy)

    def se_dotika(self, druga):
        return (self.x - druga.x) ** 2 + (self.y - druga.y) ** 2 <= (self.r + druga.r) ** 2

    def eksplodiraj(self):
        if not self.eksplodiran:
            self.eksplodiran = True
            self.r = 30
            self.krog.setRect(-30, -30, 60, 60)

    def setPosition(self, x, y):
        self.krog.setPos(self.x, self.y)

    def getEksplodiran(self):
        return self.eksplodiran

    def disable(self):
        risar.odstrani(self.krog)

    def resetLifetime(self):
        self.lifetime = 0.00

    def getLifetime(self):
        return self.lifetime

    def addLifetime(self, s):
        self.lifetime += s

class MiskinKrog():
    def __init__(self):
        self.r = 30
        self.x, self.y = risar.miska
        barva = risar.barva("grey")
        self.krog = risar.krog(self.x, self.y, self.r, barva, 3)

    def update(self):
        self.x, self.y = risar.miska
        self.krog.setPos(self.x, self.y)

    def disable(self):
        risar.odstrani(self.krog)

    def getX(self):
        return self.x

    def getY(self):
        return self.y


def ustvari_kroge(st):
    krogi = []
    for i in range(st):
        krogi.append(Krog())
    return krogi


def start_level(za_zadet, st_krogov):
    risar.pobrisi()
    interval = 0.02
    se_zacelo = False
    risar.klik = False
    zadeti = 0
    krogi = ustvari_kroge(st_krogov)
    eksplodirani = []
    miskin_krog = MiskinKrog()

    while(True):

        # Preveri, če so vsi eksplodirani izginili
        if se_zacelo:
            if len(eksplodirani) == 0:
                return (False, zadeti)

        for krog in krogi:
            if krog.getEksplodiran():
                krogi.remove(krog)
                continue
            krog.premik()
            for k in eksplodirani:
                if krog.se_dotika(k):
                    zadeti += 1
                    krog.eksplodiraj()
                    krog.resetLifetime()
                    eksplodirani.append(krog)
                    break

        # Preveri žilenjsko dobo eksplodiranih krogov
        for krog in eksplodirani:
            krog.addLifetime(interval)
            if krog.getLifetime() >= 4:
                krog.disable()
                eksplodirani.remove(krog)

        # Krog, ki sledi miški
        if not se_zacelo:
            if risar.klik:
                se_zacelo = True
                miskin_krog.disable()
                nov_krog = Krog(miskin_krog.getX(), miskin_krog.getY(), 0, 0, risar.barva("grey"))
                nov_krog.eksplodiraj()
                eksplodirani.append(nov_krog)
            else:
                miskin_krog.update()

        # Preveri, če je dovolj eksplozij za zaključek stopnje
        if zadeti >= za_zadet:
            return (True, zadeti)

        risar.cakaj(interval)

    return (False, zadeti)





stopnje = [(1, 5), (2, 5), (3, 10), (4, 10), (5, 10), (6, 10), (7,10), (8,10), (9,10), (120, 120)]
for i, stopnja in enumerate(stopnje):
    st_zadetkov, st_zog = stopnja
    while(True):
        QMessageBox.information(None, "Stopnja {}".format(str(i+1)), "Razstreli {} izmed {} žog.".format(st_zadetkov, st_zog))
        zmagal, razstreljenih = start_level(st_zadetkov, st_zog)
        if zmagal:
            break
        QMessageBox.information(None, ":(", "Žal ti ni uspelo. Razstrelil si {} žog.\n Poskusi še enkrat!".format(razstreljenih))
QMessageBox.information(None, "GG WP", "KONEC IGRE! Ma ti si car.".format(st_zadetkov, st_zog))

