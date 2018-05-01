import risar, zelva, random
from math import sqrt

#6
"""""
krog = risar.krog(risar.nakljucne_koordinate()[0], risar.nakljucne_koordinate()[1], 10,
                      barva=risar.nakljucna_barva(), sirina=1)
vx = random.randint(-5, 5)
vy = sqrt(25 - vx ** 2)

i = 0
while i != 5000:
    krog.setPos(krog.x() + vx, krog.y() + vy)
    if not (0 < krog.x() < risar.maxX - 5):
        vx = -vx
    if not (0 < krog.y() < risar.maxY - 5):
        vy = -vy
    i += 1
    risar.cakaj(0.02)
"""
#7

krogi = []
vx = []
vy = []

for i in range(30):
    krog = risar.krog(risar.nakljucne_koordinate()[0], risar.nakljucne_koordinate()[1], 10,
                      barva=risar.nakljucna_barva(), sirina=1)
    krogi.append(krog)
    vx.append(random.randint(-5, 5))
    vy.append(sqrt(25 - vx[i] ** 2))



for i in range(5000):
    for i in range(len(krogi)):
        krog = krogi[i]
        krog.setPos(krog.x() + vx[i], krog.y() + vy[i])
        if not (0 < krog.x() < risar.maxX - 5):
            vx[i] = -vx[i]
        if not (0 < krog.y() < risar.maxY - 5):
            vy[i] = -vy[i]
    risar.cakaj(0.02)


