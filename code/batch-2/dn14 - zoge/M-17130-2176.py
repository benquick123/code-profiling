import risar
import random
import math

barva_kroga = risar.nakljucna_barva()
x, y = risar.nakljucne_koordinate()
krog = risar.krog(x, y, 10, barva_kroga)

nx = random.randint(-5, 5)
ny = math.sqrt(25 - nx**2)

for i in range(1000):
    krog.setPos(krog.x() + nx, krog.y() + ny)

    if not (11 < krog.x() and krog.x() < risar.maxX - 11):
        nx = -nx

    elif not (11 < krog.y() and krog.y() < risar.maxY - 11):
        ny = -ny

    risar.cakaj(0.02)