import risar
from random import randint
from math import sqrt

risar.obnavljaj = True
def zoga():
    barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
    x0, y0 = risar.nakljucne_koordinate()
    smer = randint(-5, 5)
    smery = sqrt(25 - smer**2)
    for i in range(500):
        x0 += smer
        y0 += smery
        krogi = risar.krog(x0, y0, 10, barva, 1)
        risar.cakaj(0.02)
        krogi.hide()
        if (x0 < 10 or x0 > 796):
            smer = -smer#smer - 2*smer
            #smery = sqrt(25 - smer ** 2)
        elif y0 < 10 or y0 > 496:
            smery = -smery#smery - 2 * smery
            #smer = sqrt(25 - smery ** 2)

zoga()

risar.stoj()