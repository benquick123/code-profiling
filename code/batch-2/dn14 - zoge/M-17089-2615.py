import risar
from random import randint

#ZA 6

xos = []
yos = []
krogec = risar.krog(randint(0, risar.maxX-50), randint(0, risar.maxY-50), 10, barva=risar.nakljucna_barva(), sirina=2)
random_X = randint(0, 5)
random_Y = randint(-1, 5)
xos.append(random_X)
yos.append(random_Y)
for u in range(850):
    krogec.setPos(krogec.x() + xos[0], krogec.y() + yos[0])
    if not (0 < krogec.x() < risar.maxX):
        xos[0] = -xos[0]
    if not (0 < krogec.y() < risar.maxY):
        yos[0] = -yos[0]
    risar.cakaj(0.02)
del xos[:]
del yos[:]

#ZA 7
krogi = []
for i in range(30):
    krogec = risar.krog(randint(0, risar.maxX-50), randint(0, risar.maxY-50), 10, barva=risar.nakljucna_barva(), sirina=2)
    krogi.append(krogec)
    random_XX = randint(0, 5)
    random_YY = randint(-1, 5)
    xos.append(random_XX)
    yos.append(random_YY)

for v in range(850):
    for h in range(len(krogi)):
        krogec = krogi[h]
        krogec.setPos(krogec.x() + xos[h], krogec.y() + yos[h])
        if not (0 < krogec.x() < risar.maxX):
            xos[h] = -xos[h]
        if not (0 < krogec.y() < risar.maxY):
            yos[h] = -yos[h]
    risar.cakaj(0.02)






































































