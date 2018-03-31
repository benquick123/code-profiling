import risar
from random import randint,random
from math import *
from PyQt5.QtWidgets import QMessageBox
krogi = []
vx = []
vy = []
for i in range(30):
    krog = risar.krog(randint(0, risar.maxX-100), randint(0, risar.maxY-100), 10, barva=risar.nakljucna_barva())
    krogi.append(krog)
    vx.append(2 + random() * 3)
    vy.append(2 + random() * 3)
mis = risar.miska
krog_mis = risar.krog(mis[0],mis[1], 30, barva=risar.nakljucna_barva())
i = 0
while i != 2:
    klik = risar.klik
    if not klik:
        mis = risar.miska
        krog_mis.setPos(mis[0],mis[1])
    if klik:
        c = krog_mis.pen().color().lighter()
        c.setAlpha(192)
        krog_mis.setBrush(c)
    for i in range(len(krogi)):
        krog = krogi[i]
        krog.setPos(krog.x() + vx[i], krog.y() + vy[i])
        #if round(krog.x())==mis[0] and klik and round(krog.y())==mis[1] and klik:
        xos = krog.x() - mis[0]
        yos = krog.y() - mis[1]
        if sqrt(xos**2 + yos**2) <= 40 and klik:
            #print(mis,round(krog.x()), round(krog.y()))
            c = krog.pen().color().lighter()
            c.setAlpha(192)
            krog.setBrush(c)
            i = 2
            break
        if not (0 < krog.x() < risar.maxX):
            vx[i] = -vx[i]
        if not (0 < krog.y() < risar.maxY):
            vy[i] = -vy[i]

    risar.cakaj(0.02)


#risar.cakaj(20)