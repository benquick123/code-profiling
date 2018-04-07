import risar
from PyQt5.QtWidgets import QMessageBox
from random import randint
from math import *

class Zoga:
    def __init__(self, bool):
        if bool:
            self.x = risar.miska[0]
            self.y = risar.miska[1]
            self.r = 30
            self.barva = risar.bela
        else:
            self.r = 10
            self.x, self.y = risar.nakljucne_koordinate()
            if self.x < 10:
                self.x += 10
            elif self.x > risar.maxX - self.r:
                self.x -= 10
            if self.y < 10:
                self.y += 10
            elif self.y > risar.maxY - self.r:
                self.y -= 10
            self.barva = risar.nakljucna_barva()
            self.hitrostX = randint(-5, 5)
            self.hitrostY = sqrt(25 - self.hitrostX ** 2)
        self.eksplodirana = False
        self.active = True
        self.time_to_live = 4
        self.obj = risar.krog(self.x, self.y, self.r, self.barva, 3)


def razdalja(x, y, x1, y1):                      #vrne razdaljo med dvema točkama v 2-d ravnini
    return sqrt((x - x1) ** 2 + (y - y1) ** 2)


zoge = []
for i in range(30):               #kreira 30 objektov Zoga
    zoge.append(Zoga(False))
zoga_miska = Zoga(True)

eksplodirane = []
count_eksplodiranih = -1       #da ne šteje miska.klik

risar.obnavljaj = False

timer = 0
while not risar.klik or eksplodirane:      #izvaja se dokler nismo še kliknili z miško ali dokler je še kakšna eksplodirana žoga na zaslonu
    for el in zoge:
        el.obj.setPos(el.x, el.y)          #nastavi novo pozicijo za vsako žogo
    risar.cakaj(0.02)
    timer += 0.02
    for el in zoge:
        if el.active:
            if el.x > risar.maxX - el.r or el.x < el.r:                  #preverja odboje
                el.hitrostX = -el.hitrostX
            if el.y > risar.maxY - el.r or el.y < el.r:
                el.hitrostY = -el.hitrostY
            if not el in eksplodirane:                        #izvede premik, če žoga ni še eksplodirana
                el.x += el.hitrostX
                el.y += el.hitrostY
            for eksp in eksplodirane:       #preverja razdaljo med trenutno žogo in vsemi ostalimi eksplodiranimi žogami
                if razdalja(el.x, el.y, eksp.x, eksp.y) < 40 and el not in eksplodirane:
                    eksplodirane.append(el)
                    c = el.obj.pen().color().lighter()
                    c.setAlpha(192)
                    el.obj.setBrush(c)

    if not risar.klik:                                                    #če še ni prišlo do klika premika večji krog glede na koordinate miške
        zoga_miska.obj.setPos(risar.miska[0], risar.miska[1])
        zoga_miska.x = risar.miska[0]
        zoga_miska.y = risar.miska[1]
    elif zoga_miska not in eksplodirane and zoga_miska.active:
        eksplodirane.append(zoga_miska)

    for el in eksplodirane:                                #po 4 sekundah skrije posamezno eksplodirano žogo
        el.obj.setRect(-30, -30, 60, 60)
        el.time_to_live -= 0.02
        if el.time_to_live <= 0:
            eksplodirane.pop(eksplodirane.index(el))
            el.obj.hide()
            count_eksplodiranih += 1
            el.active = False

    risar.obnovi()
str = "Razstrelil si {} žog!".format(count_eksplodiranih)                      #izpis končnega števila razstreljenih žog
QMessageBox.information(None, "Konec", str)
risar.stoj()
