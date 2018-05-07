import risar
from random import *
from math import *

krogi = []
vxi =[]
vyi = []
v = 5
mis=risar.krog(risar.miska[0], risar.miska[1], 30, risar.bela, 2)
for i in range(30):
    barva = risar.nakljucna_barva()
    x, y = risar.nakljucne_koordinate()
    vx = uniform(-v, v)
    vy = sqrt(v ** 2 - vx ** 2)
    krog = risar.krog(x, y, 10, barva, 2)
    krogi.append(krog)
    vxi.append(vx)
    vyi.append(vy)

for i in range(1000):
    for i in range(len(krogi)):
        krog = krogi[i]
        krog.setPos(krog.x()+vxi[i], krog.y()+vyi[i])
        if not (0 < krog.x() < risar.maxX):
            vxi[i] = -vxi[i]
        if not (0 < krog.y() < risar.maxY):
            vyi[i] = -vyi[i]
        if risar.klik == True:
            dist = sqrt((mis.x() - krog.x()) ** 2 + (mis.y() - krog.y()) ** 2)
            if dist <= 40:
                risar.stoj()
    if not risar.klik:
        mis.setPos(risar.miska[0], risar.miska[1])
    risar.cakaj(0.02)

