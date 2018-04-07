import risar
from PyQt5.QtWidgets import QMessageBox
import random
import math
import time

ST_KROGLIC = [10, 15, 15, 20, 20, 25, 25, 30, 30, 40]
ST_CILJ =    [1,  3,  6,  12, 15, 21, 22, 27, 28, 39]

POLMER_KROGLICE = 10
POLMER_KROGA = 30

BARVA_MISKE = risar.barva(180, 180, 180)
DEBELINA_KROGA = 3

CAS_EKSPLODIRANJA = 4
PAVZA = 0.02
HITROST = 5

def generiraj_kroge(st_krogov, POLMER_KROGLICE, HITROST, DEBELINA_KROGA):
    krogi = []
    for i in range(st_krogov):
        x, y = risar.nakljucne_koordinate()
        barva = risar.nakljucna_barva()
        xPremik = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        ySmer = random.choice([-1, 1])
        yPremik = math.sqrt(HITROST ** 2 - xPremik ** 2) * ySmer
        krog = risar.krog(x, y, POLMER_KROGLICE, barva, DEBELINA_KROGA)
        krogi.append([krog, x, y, xPremik, yPremik])
    return krogi

def premakni_kroge(krogi, PAVZA, POLMER_KROGLICE):
    index = 0
    maxX = risar.maxX - POLMER_KROGLICE
    maxY = risar.maxY - POLMER_KROGLICE
    for krog, x, y, xPremik, yPremik in krogi:
        if x + xPremik < POLMER_KROGLICE:
            x = x + abs(x + xPremik)
            krogi[index][3] = xPremik * -1
        elif x + xPremik > maxX:
            x = x - ((x + xPremik) - maxX)
            krogi[index][3] = xPremik * -1
        else:
            x = x + xPremik
        if y + yPremik < POLMER_KROGLICE:
            y = y + abs(y + yPremik)
            krogi[index][4] = yPremik * -1
        elif y + yPremik > maxY:
            y = y - ((y + yPremik) - maxY)
            krogi[index][4] = yPremik * -1
        else:
            y = y + yPremik
        krog.setPos(x, y)
        krogi[index][0] = krog
        krogi[index][1] = x
        krogi[index][2] = y
        index += 1
    risar.cakaj(PAVZA)

def preveri_krogle(krogi, POLMER_KROGLICE, POLMER_KROGA, aktivirani, cas, st):
    index = 0
    while index < len(krogi):
        for x1, y1, start, krog2 in aktivirani:
            razdalja = math.sqrt(abs(krogi[index][1] - x1) ** 2 + abs(krogi[index][2] - y1) ** 2)
            if razdalja < POLMER_KROGA + POLMER_KROGLICE:
                krogi[index][0].setRect(-POLMER_KROGA, -POLMER_KROGA, POLMER_KROGA * 2, POLMER_KROGA * 2)
                c = krogi[index][0].pen().color().lighter()
                c.setAlpha(192)
                krogi[index][0].setBrush(c)
                aktivirani.append((krogi[index][1], krogi[index][2], time.time(), krogi[index][0]))
                st += 1
                krogi.pop(index)
                index -= 1
                break
        index += 1
    end = time.time()
    index = 0
    while index < len(aktivirani):
        if end - aktivirani[index][2] > cas:
            aktivirani[index][3].hide()
            aktivirani.pop(index)
        else:
            index += 1
    return krogi, aktivirani, st

i = 0
while i < len(ST_KROGLIC):
    stevilo, cilj = ST_KROGLIC[i], ST_CILJ[i]
    okno = "Stopnja " + str(i+1)
    sporocilo = "Št. žog: " + str(stevilo) + " cilj: " +  str(cilj)
    QMessageBox.information(None, okno, sporocilo)
    risar.klik = False
    KROGI = generiraj_kroge(stevilo, POLMER_KROGLICE, HITROST, DEBELINA_KROGA)
    miskaX, miskaY = risar.miska
    miska = risar.krog(miskaX, miskaY, POLMER_KROGA, BARVA_MISKE, DEBELINA_KROGA)
    while True:
        premakni_kroge(KROGI, PAVZA, POLMER_KROGLICE)
        if not risar.klik:
            miskaX, miskaY = risar.miska
            miska.setPos(miskaX, miskaY)
        else:
            c = miska.pen().color().lighter()
            c.setAlpha(192)
            miska.setBrush(c)
            break
    aktivirani = [(miskaX, miskaY, time.time(), miska)]
    st = 0
    while aktivirani:
        KROGI, aktivirani, st = preveri_krogle(KROGI, POLMER_KROGLICE, POLMER_KROGA, aktivirani, CAS_EKSPLODIRANJA, st)
        premakni_kroge(KROGI, PAVZA, POLMER_KROGLICE)
    if st >= cilj:
        sporocilo = "Št. eksplodiranih žog: " + str(st) + " dosegli ste cilj (" + str(cilj)+ ")"
        i += 1
    else:
        sporocilo = "Št. eksplodiranih žog: " + str(st) + " niste dosegli cilja (" + str(cilj) + ")"
    risar.pobrisi()
    QMessageBox.information(None, okno, sporocilo)

risar.stoj()