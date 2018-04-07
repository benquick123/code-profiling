from random import randint

from P1.Risar import risar

zaX = randint(-5, 5)
zaY = randint(-5, 5)


x, y = risar.nakljucne_koordinate()

krog = risar.krog(x, y, 10, risar.nakljucna_barva(), sirina=1)

for k in range(1000):
    x += zaX
    y += zaY

    risar.cakaj(0.02)
    krog.setPos(x, y)

    if x >= risar.maxX - 5:
        zaX = -zaX

    if y >= risar.maxY - 5:
        zaY = -zaY

    if x <= 0:
        x = -x
        zaX = -zaX

    if y <= 0:
        y = -y
        zaY = -zaY