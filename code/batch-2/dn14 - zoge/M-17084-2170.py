import risar
import random


# za oceno 6
def zoga():
    x, y = risar.nakljucne_koordinate()
    barva = risar.barva(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    zoga = risar.krog(x, y, 10, barva, 2)
    k = random.choice((-1, 1))
    q = random.choice((-1, 1))
    for i in range(1000):
        zoga.setPos(x, y)
        risar.cakaj(0.02)
        x += k * 5
        y += q * 5
        if x >= risar.maxX or x <= 0:
            k *= -1
        if y >= risar.maxY or y <= 0:
            q *= -1

#zoga()

# za oceno 7
def zoge():
    sez = []
    for i in range(30):
        x, y = risar.nakljucne_koordinate()
        barva = risar.barva(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        k = random.choice((-1, 1))
        q = random.choice((-1, 1))
        krog = risar.krog(x, y, 10, barva, 2)
        sez.append([x, y, barva, k, q, krog])

    for i in range(500):
        for a in sez:
            a[5].setPos(a[0], a[1])
            a[0] += a[3] * 5
            a[1] += a[4] * 5
            if a[0] > risar.maxX or a[0] < 0:
                a[3] *= -1
            if a[1] > risar.maxY or a[1] < 0:
                a[4] *= -1
            risar.cakaj(0.001)

zoge()

# za oceno 8
"""def mis():
    krog = risar.krog(risar.maxX / 2, risar.maxY / 2, 30, risar.bela, 2)
    while not risar.klik:
        x, y = risar.miska
        krog.setPos(x, y)
        risar.cakaj(0.01)
    risar.krog(x, y, 30, risar.bela, 2)

    risar.stoj()

mis()

nisem znal vec, ups"""