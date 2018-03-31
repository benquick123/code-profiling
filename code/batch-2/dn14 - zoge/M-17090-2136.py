import risar
import random
import time
from math import *
from PyQt5.QtWidgets import QMessageBox

class Zoga():
    def __init__(self):
        self.polmer = 10
        self.x, self.y = risar.nakljucne_koordinate()
        self.hitrostX = random.uniform(-5.0, 5.0)
        self.hitrostY = sqrt(5**2 - self.hitrostX**2) #hitrost po pitagori
        self.barva = risar.nakljucna_barva()
        self.telo = risar.krog(self.x, self.y, self.polmer, self.barva)
        self.eksplozija = False
        self.cas = 0
        self.obstoj = True
        self.update()

    def update(self):
        if self.eksplozija: #če se je krog zaletel
            self.telo.setRect(-30, -30, 60, 60) #spremenimo polmer in barvo
            c = self.telo.pen().color().lighter()
            c.setAlpha(192)
            self.telo.setBrush(c)
            if (time.clock() - self.cas) > 4: #po 4 sekundah, krog izgine
                self.telo.hide()
                self.obstoj = False #in ne ovira ostalih krogov
                risar.obnovi()

        else:
            self.x += self.hitrostX
            self.y -= self.hitrostY
            self.telo.setPos(self.x, self.y)
            self.odboj() #če pride do roba, se odbije
            risar.obnovi()

    def odboj(self): #pri odboju se zamenja smer (hitrost)
        if self.x <= 0 or self.x >= risar.maxX:
            self.hitrostX = -self.hitrostX
        if self.y <= 0 or self.y >= risar.maxY:
            self.hitrostY = -self.hitrostY


class Miska():
    def __init__(self):
        self.polmer = 30
        self.x, self.y = risar.miska
        self.telo = risar.krog(self.x, self.y, self.polmer)
        self.cas = 0
        self.zabelezi = 1 #poskrbi, da samo enkrat zabeležimo čas miške (ob kliku)
        self.obstoj = True

    def update(self):
        if not risar.klik: #po kliku se krog ne obnavlja več
            self.x, self.y = risar.miska
            self.telo.setPos(self.x, self.y)
            risar.obnovi()
        if risar.klik:
            if (time.clock() - self.cas) > 4: #po 4 sekundah, krog od miške izgine
                self.telo.hide()
                self.obstoj = False #in ne ovira ostalih krogov
                risar.obnovi()


def stopnja(n, cilj):
    QMessageBox.information(None, "Stopnja {}".format(cilj), "Razstreli {} od {} kroglic.".format(cilj, n))
    risar.klik = False
    miska = Miska()
    zoge = []
    boom = set() #množica eksplodiranih (množica, da se izognimo duplikatom)
    igra = 1 #dokler je igra == 1, se program izvaja
    konec = 0 #od zadnje eksplozije beleži, kdaj se bo program ustavil
    naprej = False #pove, ali smo eksplodirali dovolj kroglic, da gremo na naslednjo stopnjo
    for i in range(n):
        z = Zoga()
        zoge.append(z)
    while igra == 1:
        miska.update()
        for i in zoge:
            i.update()
            if risar.klik: #po kliku miške, gledamo kolizijo
                if miska.zabelezi == 1: #zabeleži, kdaj smo pritisnili na miško
                    miska.cas = time.clock()
                    miska.zabelezi = 0
                    konec = time.clock()
                if not i.eksplozija and miska.obstoj: #dokler krog od miške obstaja, preverjamo kolizijo
                    if sqrt((i.x - miska.x) ** 2 + (i.y - miska.y) ** 2) < (i.polmer + miska.polmer):  # eksplozija
                        i.eksplozija = True
                        i.cas = time.clock()
                        konec = time.clock()
                        boom.add(i) #eksplodirano doda v množico
                if i.eksplozija and i.obstoj: #po eksploziji kroga, gledamo se kolizijo z ostalimi
                    for j in zoge:
                        if not j.eksplozija:
                            if sqrt((i.x - j.x) ** 2 + (i.y - j.y) ** 2) < (30 + j.polmer):
                                j.eksplozija = True
                                j.cas = time.clock()
                                konec = time.clock()
                                boom.add(j) #eksplodirano doda v množico
        risar.cakaj(0.02)
        if (time.clock() - konec) > 5 and risar.klik: #1 sekundo po tem, ko izgine zadnja eksplodirana kroglica, se program konča
            if len(boom) >= cilj:
                QMessageBox.information(None, "Bravo!", "Eksplodiralo je {} kroglic. Zmaga!".format(len(boom))) #in izpiše rezultat
                igra = 0
                naprej = True
            if len(boom) < cilj:
                QMessageBox.information(None, ":(", "Eksplodiralo je {} kroglic. Poskusi znova.".format(len(boom))) #in izpiše rezultat
                igra = 0
    risar.pobrisi()
    return naprej


zmaga = False
level = 1
while not zmaga:
    if level == 1:
        if stopnja(5, 1): #cilj uporabimo tudi pri izpisu na kateri stopnji je igralec (drugače bi rabili dodaten števec)
            level += 1
    if level == 2:
        if stopnja(8, 2):
            level += 1
    if level == 3:
        if stopnja(10, 3):
            level += 1
    if level == 4:
        if stopnja(12, 4):
            level += 1
    if level == 5:
        if stopnja(13, 5):
            level += 1
    if level == 6:
        if stopnja(14, 6):
            level += 1
    if level == 7:
        if stopnja(15, 7):
            level += 1
    if level == 8:
        if stopnja(16, 8):
            level += 1
    if level == 9:
        if stopnja(17, 9):
            level += 1
    if level == 10:
        if stopnja(18, 10):
            zmaga = True
            QMessageBox.information(None, "Zmaga!", "Premagal si vse stopnje. Čestitam!")