'''
    OPIS: risanje in premikanje krogcev
    AVTOR: Blaž Kumer
    Datum: 15.1.2017
'''
import risar
from math import sqrt
from random import randint
from PyQt5.QtWidgets import QMessageBox
krogi=[]
vx = []
vy = []
poceni=[]
casi=[]
sporocilo=False
for a in range(11):
    krogi.append(None)
    vx.append(None)
    vy.append(None)
    poceni.append(None)
    casi.append(None)

krogi[0] = risar.krog(risar.miska[0], risar.miska[1], 30, risar.nakljucna_barva(), 5)
casi[0]=None
poceni[0]=None
vx[0]=None
vy[0]=None
ze=False
kolikoZog=0
for x in range(1,11):
    krog= risar.krog(randint(20,risar.maxX-25),randint(20,risar.maxY-25),10,risar.nakljucna_barva(),5)
    krogi[x]=krog
    koordinate=[krog.x(),krog.y()]
    z = randint(1, 5)
    vx[x]=z
    vy[x]=sqrt(25 - z ** 2)

QMessageBox.information(None, " ZA 9 ", "zadeni vsaj 5 od 10 žog")
for i in range(2000000):
    for j in range(1,len(krogi)):
        krog = krogi[j]
        if krog==None:
            continue
        if not poceni[j]:
            krog.setPos(krog.x() + vx[j], krog.y() + vy[j])
        if not (0 < krog.x() < risar.maxX - 10):
            vx[j] = -vx[j]
        if not (0 < krog.y() < risar.maxY - 10):
            vy[j] = -vy[j]
        if not risar.klik:
            krogi[0].setPos(risar.miska[0], risar.miska[1])
        else:
            if not ze:
                poceni[0]=krogi[0]
                casi[0]=i
                ze=True
            for k in range(len(poceni)):
                if poceni[k]:
                    pozX=poceni[k].x()
                    pozY=poceni[k].y()
                    if pozX-35< krog.x()<pozX+35 and pozY-35 <krog.y()<pozY+35:
                        c = krog.pen().color().lighter()
                        c.setAlpha(100)
                        krog.setBrush(c)
                        krog.setRect(-30, -30, 60, 60)
                        if not poceni[j]:
                            poceni[j]=krog
                            casi[j]=i

                    if i-casi[k]>250:
                        if krogi[k]:
                            krogi[k].hide()
                            poceni[k] = None
                            krogi[k]=None
                            casi[k]=None
                            kolikoZog += 1
    risar.cakaj(0.01)
    if ze:
        for a in poceni:
            if a:
                break
        else:
            if kolikoZog>5:
                if not sporocilo:
                    QMessageBox.information(None, "BRAVO", "zadeli ste {} zog".format(kolikoZog-1))
                risar.stoj()
                sporocilo=True
            else:
                if not sporocilo:
                    QMessageBox.information(None, "ŠKODA", "premalo žog")
                    risar.stoj()
                    sporocilo=True

        for kr in krogi:
            if kr:
                break
        else:
            if kolikoZog > 5:
                if not sporocilo:
                    QMessageBox.information(None, "BRAVO", "zadeli ste {} zog".format(kolikoZog - 1))
                risar.stoj()
                sporocilo = True
            else:
                if not sporocilo:
                    QMessageBox.information(None, "ŠKODA", "premalo žog")
                    risar.stoj()
                    sporocilo = True
risar.stoj()

'''ZA 8

import risar
from math import sqrt
from random import random,randint
krogi=[]
vx = []
vy = []
krogMis = risar.krog(risar.miska[0], risar.miska[1], 30, risar.nakljucna_barva(), 5)

for x in range(30):

    krog= risar.krog(randint(20,risar.maxX-25),randint(20,risar.maxY-25),10,risar.nakljucna_barva(),5)
    krogi.append(krog)
    z = randint(-5, 5)
    vx.append(z)
    vy.append(sqrt(25 - z ** 2))
while True:
    for j in range(len(krogi)):
        krog = krogi[j]
        krog.setPos(krog.x() + vx[j], krog.y() + vy[j])
        if not (0 < krog.x() < risar.maxX - 10):
            vx[j] = -vx[j]
        if not (0 < krog.y() < risar.maxY - 10):
            vy[j] = -vy[j]
        if not risar.klik:
            krogMis.setPos(risar.miska[0], risar.miska[1])
        else:
            pozX = krogMis.x()
            pozY = krogMis.y()
            if pozX-35< krog.x()<pozX+35 and pozY-35 <krog.y()<pozY+35:
                c = krog.pen().color().lighter()
                c.setAlpha(100)
                krog.setBrush(c)
                krog.setRect(-30, -30, 60, 60)
                risar.stoj()
    risar.cakaj(0.01)
risar.stoj()
'''

''' ZA 6
import risar
from random import randint

krog = risar.krog(randint(20, risar.maxX - 25), randint(20, risar.maxY - 25), 10, risar.nakljucna_barva(), 5)
vx=randint(-10,10)
vy=randint(-10,10)
for i in range(1000):
    krog.setPos(krog.x() + vx, krog.y() + vy)
    if not (10 < krog.x() < risar.maxX - 10):
        vx = -vx
    if not (10 < krog.y() < risar.maxY - 10):
        vy = -vy
    risar.cakaj(0.02)
risar.stoj()

'''


''' ZA 7

import risar
from random import randint
krogi=[]
vx = []
vy = []

for x in range(30):
    krog= risar.krog(randint(20,risar.maxX-25),randint(20,risar.maxY-25),10,risar.nakljucna_barva(),5)
    krogi.append(krog)
    vx.append(randint(-10,10))
    vy.append(randint(-10,10))
for i in range(1000):
    for j in range(len(krogi)):
        krogi[j].setPos(krogi[j].x() + vx[j], krogi[j].y() + vy[j])
        if not (10 < krogi[j].x() < risar.maxX - 10):
            vx[j] = -vx[j]
        if not (10 < krogi[j].y() < risar.maxY - 10):
            vy[j] = -vy[j]
    risar.cakaj(0.02)
risar.stoj()

'''



