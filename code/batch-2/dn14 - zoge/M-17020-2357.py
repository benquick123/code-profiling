
#Za oceno 10:

import risar
from random import randint, choice
from math import sqrt
import time
from PyQt5.QtWidgets import QMessageBox


def ponavljaj(stevilo_zog):
    stevilo_eksplodiranih_kroglic = 0
    stevilo_razsteljenih = 0
    zacni = True
    zoge = []
    xhitrosti = []
    yhitrosti = []
    barve = []
    mx, my = risar.miska
    miskin_krogec = risar.krog(mx, my, 30, risar.bela, 2)
    eksplodirane = []
    skrite = []
    for stevilo in range(stevilo_zog):
        barva = risar.nakljucna_barva()
        x, y = randint(10, risar.maxX - 10), randint(10, risar.maxY - 10)
        krogec = risar.krog(x, y, 10, barva, 2)
        zoge.append(krogec)
        vx = randint(-5, 5)
        vy = choice([- sqrt(25 - (vx * 2)), sqrt(25 - (vx * 2))])
        xhitrosti.append(vx)
        yhitrosti.append(vy)
        barve.append(barva)
    while stevilo_eksplodiranih_kroglic > 0 or zacni:
        for i in range(len(zoge)):
            zoga = zoge[i]
            x1, y1 = zoga.x(), zoga.y()
            if zoga in eksplodirane:
                if 3.9 < time.time() - zoga.time < 4.1:
                    zoga.hide()
                    skrite.append(zoga)
                    del eksplodirane[eksplodirane.index(zoga)]
                    stevilo_eksplodiranih_kroglic -= 1
                    if stevilo_eksplodiranih_kroglic == 0:
                        risar.pobrisi()
                        zacni = False
                        return stevilo_razsteljenih
            if risar.klik:
                ostani_na_x, ostani_na_y = mx, my
                if miskin_krogec not in eksplodirane and miskin_krogec not in skrite:
                    miskin_krogec.setPos(ostani_na_x, ostani_na_y)
                    miskin_krogec.time = time.time()
                    eksplodirane.append(miskin_krogec)
                if miskin_krogec in eksplodirane:
                    razdalja = sqrt(((x1 - ostani_na_x) ** 2) + ((y1 - ostani_na_y) ** 2))
                    if 3.9 < time.time() - miskin_krogec.time < 4.1:
                        miskin_krogec.hide()
                        skrite.append(miskin_krogec)
                        del eksplodirane[eksplodirane.index(miskin_krogec)]
                        razdalja = 50
                        if stevilo_eksplodiranih_kroglic == 0:
                            risar.pobrisi()
                            zacni = False
                            return stevilo_razsteljenih
                if razdalja <= 40:
                    if zoga not in eksplodirane and zoga not in skrite:
                        zoga.setRect(-30, -30, 60, 60)
                        zoga.setPos(x1, y1)
                        eksplodirane.append(zoga)
                        stevilo_eksplodiranih_kroglic += 1
                        stevilo_razsteljenih += 1
                        c = zoga.pen().color().lighter()
                        c.setAlpha(192)
                        zoga.setBrush(c)
                        zoga.time = time.time()
                for e in range(len(eksplodirane)):
                    eksplodirana = eksplodirane[e]
                    xe, ye = eksplodirana.x(), eksplodirana.y()
                    distanca = sqrt(((x1 - xe) ** 2) + ((y1 - ye) ** 2))
                    if distanca <= 40:
                        if zoga not in eksplodirane and zoga not in skrite:
                            zoga.setRect(-30, -30, 60, 60)
                            zoga.setPos(x1, y1)
                            eksplodirane.append(zoga)
                            stevilo_eksplodiranih_kroglic += 1
                            stevilo_razsteljenih += 1
                            c = zoga.pen().color().lighter()
                            c.setAlpha(192)
                            zoga.setBrush(c)
                            zoga.time = time.time()
                if zoga not in eksplodirane:
                    zoga.setPos(zoga.x() + xhitrosti[i], zoga.y() + yhitrosti[i])
                    if not (0 < zoga.x() < risar.maxX - 10):
                        xhitrosti[i] = - xhitrosti[i]
                    if not (0 < zoga.y() < risar.maxY - 10):
                        yhitrosti[i] = - yhitrosti[i]
            else:
                mx, my = risar.miska
                miskin_krogec.setPos(mx, my)
                zoga.setPos(zoga.x() + xhitrosti[i], zoga.y() + yhitrosti[i])
                if not (0 < zoga.x() < risar.maxX - 10):
                    xhitrosti[i] = - xhitrosti[i]
                if not (0 < zoga.y() < risar.maxY - 10):
                    yhitrosti[i] = - yhitrosti[i]
        risar.cakaj(0.02)
    return stevilo_razsteljenih


def izvedi(stopnja, kvota, stevilo_zog):
    a = 0
    while a < kvota:
        QMessageBox.information(None, "Stopnja {}".format(stopnja), "Razstreli {} žog od {}".format(kvota, stevilo_zog))
        a = ponavljaj(stevilo_zog)
        if a < kvota:
            QMessageBox.information(None, "okno", "Uspelo ti je razstreliti {} žog. Premalo.".format(a))
            risar.klik = False
        else:
            risar.pobrisi()
            risar.klik = False


#Stopnja 1:
izvedi(1, 1, 5)

#Stopnja 2:
izvedi(2, 2, 8)

#Stopnja 3:
izvedi(3, 5, 10)

#Stopnja 4:
izvedi(4, 7, 14)

#Stopnja 5:
izvedi(5, 9, 17)

#Stopnja 6:
izvedi(6, 11, 19)

#Stopnja 7:
izvedi(7, 13, 22)

#Stopnja 8:
izvedi(8, 15, 27)

#Stopnja 9:
izvedi(9, 17, 30)

#Stopnja 10:
izvedi(10, 30, 40)

#Konec igre:
QMessageBox.information(None, "Konec igre!", "Zmagal si!")


