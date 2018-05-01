import risar
from random import *
from math import *

#Za oceno 6
'''
x, y = risar.nakljucne_koordinate()
vx = randint(-5, 5)
vy = sqrt(25 - vx**2)
nakljucno = randint(0,1)
if nakljucno == 1:
    vy -= 2*vy
krog = risar.krog(x, y, 10, barva=risar.nakljucna_barva(), sirina=3)
for i in range(1000):
    krog.setPos(krog.x() + vx, krog.y() + vy)
    if not (0 < krog.x() < risar.maxX -10):
        vx = -vx
    if not (0 < krog.y() < risar.maxY -10):
        vy = -vy
    risar.cakaj(0.02)'''


#za 7
'''
vx = []
vy = []
krogi = []
for i in range(30):
    x, y = risar.nakljucne_koordinate()
    krog = risar.krog(x, y, 10, barva=risar.nakljucna_barva(), sirina=3)
    krogi.append(krog)
    vx.append(randint(-5, 5))
    y = sqrt(25 - vx[i]**2)
    nakljucno = randint(0,1)
    if nakljucno == 1:
        y -= 2*y
    vy.append(y)


for i in range(1000):
    for i in range(len(krogi)):
        krogec = krogi[i]
        krogec.setPos(krogec.x() + vx[i], krogec.y() + vy[i])
        if not (0 < krogec.x() < risar.maxX -10):
            vx[i] = -vx[i]
        if not (0 < krogec.y() < risar.maxY -10):
            vy[i] = -vy[i]
    risar.cakaj(0.02)'''