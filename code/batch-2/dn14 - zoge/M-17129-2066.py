import risar
from random import randint
from math import sqrt
from PyQt5.QtWidgets import QMessageBox
import time

krogi = []
hx = []
hy = []
barve = []
casi = []
r = 10
koordinate = []
mojkrog = risar.krog(9999, 9999, 30, risar.bela, 4)
z = 0
stevec = 0
konec_igre = 0
stevec2 = 0
i = 1
zakljucek = False

def generiranje_kroglic(stevilo):
    for i in range(stevilo):
        barva = risar.nakljucna_barva()
        krog = risar.krog(randint(0, risar.maxX-10), randint(0, risar.maxY-10), 10, barva, 4)
        krogi.append(krog)
        a = randint(-5, 5)
        b = sqrt(5 ** 2 - a ** 2)
        hx.append(a)
        hy.append(b)
        barve.append(barva)
    return (krogi,hx,hy)

def igra(krogi,hx,hy):
    barve = []
    casi = []
    r = 10
    koordinate = []
    mojkrog = risar.krog(1, 1, 30, risar.bela, 4)
    z = 0
    stevec = 0
    konec_igre = 0
    stevec2 = 0

    for j in range(1000):
        if konec_igre == 1:
            break
        for i in range(len(krogi)):
            if z == 1:
                if time.time() - t1 > 3:
                    mojkrog.hide()
                    risar.klik = False
            krog = krogi[i]

            if krog == 1:
                continue

            if (krog.x(),krog.y()) in koordinate:
                o = koordinate.index((krog.x(),krog.y()))
                koncni_cas = round(time.time())
                if koncni_cas - casi[o] > 3:
                    krog.hide()
                    stevec2 -= 1
                    koordinate[o]=(99999,99999)
                    krogi[i] = 1
                    if stevec2 == 0:
                        konec_igre = 1
                continue

            krog.setPos(krog.x() + hx[i], krog.y() + hy[i])

            if not risar.klik:
                koordinati = risar.miska
                mojkrog.setPos(koordinati[0], koordinati[1])
                t1 = time.time()
                z = 1

            if not (0 < krog.x() < risar.maxX - 10):
                hx[i] = -hx[i]
            if not (0 < krog.y() < risar.maxY - 10):
                hy[i] = -hy[i]

            if 40 > (sqrt((koordinati[0] - krog.x())**2 + (koordinati[1] - krog.y())**2)) and risar.klik == True:
                koordinate.append((krog.x(),krog.y()))
                zacetni_cas = round(time.time())
                casi.append(zacetni_cas)
                krog.setRect(-30, -30, 60, 60)
                c = krog.pen().color().lighter()
                c.setAlpha(192)
                krog.setBrush(c)
                krogi[i] = krog
                stevec2 +=1
                stevec += 1
                continue

            if koordinate != []:
                for x,y in koordinate:
                    if 40 > (sqrt((x - krog.x()) ** 2 + (y - krog.y()) ** 2)):
                        koordinate.append((krog.x(), krog.y()))
                        zacetni_cas = round(time.time())
                        casi.append(zacetni_cas)
                        krog.setRect(-30, -30, 60, 60)
                        c = krog.pen().color().lighter()
                        c.setAlpha(192)
                        krog.setBrush(c)
                        krogi[i] = krog
                        stevec2 += 1
                        stevec += 1
                        break
        risar.cakaj(0.02)
    return stevec

i = 1
koliko = 5*i
zmaga = True

while i < 11:

    QMessageBox.information(None, "{}. stopnja".format(i), "Raztreli {} od {} žog".format(i*2,i*5))

    if zmaga:
        krogi, hx, hy = generiranje_kroglic(koliko)
    else:
        krogi, hx, hy = generiranje_kroglic(koliko)

    stevec = igra(krogi,hx,hy)

    if stevec < i*2:
        zmaga = False
        koliko = stevec
        QMessageBox.information(None, "Rezultat", "Eksplodiralo je {} žog! Poskusi znova!".format(stevec))
    else:
        i += 1
        zmaga = True
        koliko = 5 + stevec
        QMessageBox.information(None, "Rezultat", "Čestitam, eksplodiralo je {} žog!".format(stevec))

