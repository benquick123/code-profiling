import PyQt5
import risar
from random import randint
from math import sqrt
def naredi_kroglico():
    x, y = risar.nakljucne_koordinate()
    barva = risar.nakljucna_barva()
    dx = randint(-5, 5)
    dy = sqrt(25 - (dx * dx))
    return x, y, barva, dx, dy
def gibaj(x, y, barva, dx, dy):
    if risar.klik and (xme- x) * (xme- x) + (yme- y) * (yme- y) < 1600:
        risar.stoj()
        return
    if x < 5  and dx < 0 or (risar.maxX - x) < 5 and dx > 0:
        dx = - dx
    if y < 5 and dy < 0 or (risar.maxY - y) < 5 and dy > 0:
        dy = -dy
    risar.krog(x, y, 10, barva, 1)
    x += dx
    y += dy
    return x, y, barva, dx, dy

Kroglice = []
for a in range(31):
    Kroglice.append(naredi_kroglico())


barvamiske = risar.nakljucna_barva()

for time in range(501):
    risar.pobrisi()
    i = 0
    if not risar.klik:
        xme, yme = risar.miska
    for kroglica in Kroglice:
        Kroglice[i] = gibaj(kroglica[0], kroglica[1], kroglica[2], kroglica[3], kroglica[4])
        i += 1
    risar.krog(xme, yme, 30, barvamiske, 1)
    risar.cakaj(0.02)
risar.stoj()