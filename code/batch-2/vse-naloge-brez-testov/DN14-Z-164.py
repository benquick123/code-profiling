import risar
from random import randint
from math import sqrt
from PyQt5.QtWidgets import QMessageBox

def za6():
    vx = randint(-5, 5)
    vy = sqrt(25 - vx ** 2)
    x, y = risar.nakljucne_koordinate()
    krog = risar.krog(x, y, 10, barva = risar.nakljucna_barva())
    for i in range(980):
        krog.setPos(krog.x() + vx, krog.y() + vy)
        if not (0 < krog.x() < risar.maxX - 35):
            vx = -vx
        if not (0 < krog.y() < risar.maxY - 35):
            vy = -vy
        risar.cakaj(0.02)


def za7():
    krogi = []
    vx = []
    vy = []
    for i in range(30):
        x, y = risar.nakljucne_koordinate()
        krog = risar.krog(x, y, 10, barva=risar.nakljucna_barva())
        hitrostx = randint(-5, 5)
        hitrosty = sqrt(25 - hitrostx ** 2)
        krogi.append(krog)
        vx.append(hitrostx)
        vy.append(hitrosty)
    for e in range(980):
        for stev, krog in enumerate(krogi):
            krog.setPos(krog.x() + vx[stev], krog.y() + vy[stev])
            if not (0 < krog.x() < risar.maxX - 35):
                vx[stev] = -vx[stev]
            if not (0 < krog.y() < risar.maxY - 35):
                vy[stev] = -vy[stev]
        risar.cakaj(0.02)

def za8():
    miska = risar.krog(risar.miska[0],risar.miska[1], 30)
    krogi = []
    vx = []
    vy = []
    for i in range(30):
        x, y = risar.nakljucne_koordinate()
        krog = risar.krog(x, y, 10, barva=risar.nakljucna_barva())
        hitrostx = randint(-5, 5)
        hitrosty = sqrt(25 - hitrostx ** 2)
        krogi.append(krog)
        vx.append(hitrostx)
        vy.append(hitrosty)
    while True:
        for stev, krog in enumerate(krogi):
            krog.setPos(krog.x() + vx[stev], krog.y() + vy[stev])
            if not (0 < krog.x() < risar.maxX - 35):
                vx[stev] = -vx[stev]
            if not (0 < krog.y() < risar.maxY - 35):
                vy[stev] = -vy[stev]
            if not risar.klik:
                miska.setPos(risar.miska[0], risar.miska[1])
            if (krog.x() - miska.x()) ** 2 + (krog.y() - miska.y()) ** 2 <= 40 ** 2 and risar.klik:
                return
        risar.cakaj(0.02)

def za9():
    ignor = []
    cas = []
    pobarvani = []
    sez = []
    miska = risar.krog(risar.miska[0], risar.miska[1], 30)
    krogi = []
    vx = []
    vy = []
    n = 0
    for i in range(30):
        x, y = risar.nakljucne_koordinate()
        krog = risar.krog(x, y, 10, barva=risar.nakljucna_barva())
        hitrostx = randint(-5, 5)
        hitrosty = sqrt(25 - hitrostx ** 2)
        krogi.append(krog)
        vx.append(hitrostx)
        vy.append(hitrosty)
        sez.append(krog)
    while True:
        for stev, krog in enumerate(krogi):
            if krog in sez:
                krog.setPos(krog.x() + vx[stev], krog.y() + vy[stev])
                if not (0 < krog.x() < risar.maxX - 35):
                    vx[stev] = -vx[stev]
                if not (0 < krog.y() < risar.maxY - 35):
                    vy[stev] = -vy[stev]
                if not risar.klik:
                    miska.setPos(risar.miska[0], risar.miska[1])
                if (krog.x() - miska.x()) ** 2 + (krog.y() - miska.y()) ** 2 <= 40 ** 2 and risar.klik and n < 134:
                    krog.setRect(-30, -30, 60, 60)
                    pobarvani.append(krog)
                    cas.append(0)
                    c = krog.pen().color().lighter()
                    c.setAlpha(192)
                    krog.setBrush(c)
                    sez.remove(krog)
                for barv in pobarvani:
                    if (krog.x() - barv.x()) ** 2 + (krog.y() - barv.y()) ** 2 <= 40 ** 2 and krog not in pobarvani and barv not in ignor:
                        krog.setRect(-30, -30, 60, 60)
                        pobarvani.append(krog)
                        cas.append(0)
                        c = krog.pen().color().lighter()
                        c.setAlpha(192)
                        krog.setBrush(c)
                        sez.remove(krog)
                for stev, bar in enumerate(pobarvani):
                    if cas[stev] > 134:
                        bar.hide()
                        ignor.append(bar)
                if cas != [] and min(cas) > 134:
                    return QMessageBox.information(None, 'Konec igre!', 'Eksplodiralo je {} žog.'.format(len(pobarvani)))
                if len(pobarvani) == len(krogi):
                    return QMessageBox.information(None, 'Konec igre!', 'Eksplodiralo je {} žog.'.format(len(pobarvani)))
                if pobarvani == [] and n > 134:
                    return QMessageBox.information(None, 'Konec igre!', 'Eksplodiralo je {} žog.'.format(len(pobarvani)))
        if n >= 134:
            miska.hide()
        if risar.klik:
            n += 1
        for x , y in enumerate(cas):
            cas[x] += 1
        risar.cakaj(0.02)

za9()