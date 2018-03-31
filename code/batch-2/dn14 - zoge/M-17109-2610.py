import risar
from math import sqrt
from random import randint, random


vx = []
vy = []
krogeci = []
for i in range(30):
    a= risar.krog(randint(0, risar.maxX-100), randint(0, risar.maxY-100),10,risar.nakljucna_barva())
    krogeci.append(a)
    vx.append((2+random() * 3))
    vy.append((2+random() * 3))

x, y = risar.miska
misek = risar.krog(x,y,20)

def konec(c,d):
    a=0
    while a==0:
        for i in range(len(krogeci)):
            krog = krogeci[i]
            krog.setPos(krog.x() + vx[i], krog.y() + vy[i])
            if not (3 < krog.x() < risar.maxX - 10):
                vx[i] = -vx[i]
            if not (3 < krog.y() < risar.maxY - 10):
                vy[i] = -vy[i]
            if sqrt((misek.x() - krog.x())**2  + (misek.y() - krog.y())**2) < 33:
                risar.stoj()
        risar.cakaj(0.02)

a=0
while a == 0:
    for i in range(len(krogeci)):
        krog=krogeci[i]
        krog.setPos(krog.x() + vx[i], krog.y() + vy[i])
        if not (3 < krog.x() < risar.maxX - 10):
            vx[i] = -vx[i]
        if not (3 < krog.y() < risar.maxY - 10):
            vy[i] = -vy[i]
    x,y=risar.miska
    misek.setPos(x,y)
    if risar.klik == True:
        misek.setPos(x,y)
        konec(x,y)
    risar.cakaj(0.02)

