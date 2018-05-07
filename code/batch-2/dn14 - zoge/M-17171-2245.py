import risar,os
from random import *
from math import *
import time
from collections import *
risar.obnavljaj= True



def ustvari():  # Shranjevanje žogic in lastnosti
    indentiteta = defaultdict(list)
    r = 10
    sirina = 4

    while len(indentiteta) < 30:
        x, y = risar.nakljucne_koordinate()
        barva1 = risar.nakljucna_barva()
        kot = randint(0, 360)
        if x > 30 and y > 30:
            if x < (risar.maxX - 50) and y < (risar.maxY - 50):
                zogica = risar.krog(x, y, r, barva1, sirina)
                indentiteta[zogica].append(5 * cos(kot))
                indentiteta[zogica].append(5 * sin(kot))
                indentiteta[zogica].append(barva1)
    print("Število žogic na platnu: ", len(indentiteta))
    return indentiteta


def preveri(koti,tocka):
    x,y = koti
    xx = tocka[0]
    yy = tocka[1]
    r = 10
    rr = 50
    i = sqrt((x-xx)**2 + (y-yy)**2)
    if rr > (i+r):
        return False
    else:
        return True



def mainloop(): #Motor igre
    # MISKA ZOGA
    rm = 30
    sirinam = 3
    barvam = risar.bela
    seznam = []
    stop = False
    tocka = []

    # ZOGICE
    zogice = ustvari()
    close = False
    while close == False:
        for zoga,koti in zogice.items():
            if stop == True:
                test = preveri((zoga.x(),zoga.y()),tocka)
                if test == False:
                    close = True
                    risar.stoj()
            zoga.setPos(zoga.x() + koti[0], zoga.y() + koti[1])
            if not (0 < zoga.x() < risar.maxX - 8):
                koti[0] = -koti[0]
            if not (0 < zoga.y() < risar.maxY - 8):
                koti[1] = -koti[1]

        risar.cakaj(0.02)

        xm, ym = risar.miska
        if risar.klik == False and stop == False:
            if len(seznam) != 1:
                krog = risar.krog(xm, ym, rm, barvam, sirinam)
                seznam.append((xm,ym))
            if len(seznam) == 1:
                risar.odstrani(krog)
                krog = risar.krog(xm, ym, rm, barvam, sirinam)

        if risar.klik == True and stop == False:
            stop = True
            risar.odstrani(krog)
            krog = risar.krog(xm, ym, rm, barvam, sirinam)
            tocka.append(xm)
            tocka.append(ym)





a = mainloop()