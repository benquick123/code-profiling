import risar
from random import randint
import math
import collections
import time
from PyQt5.QtWidgets import QMessageBox
j = 10
oo = 1
while j > 0:
    class Miska:
        def __init__(self):
            self.x = risar.maxX/2
            self.y = risar.maxY/2
            self.krog = risar.krog(self.x, self.y, 30)
            self.update()

        def update(self):
            self.krog.setPos(self.x, self.y)
            risar.obnovi()

        def fly(self, x, y):
            self.x = x
            self.y = y
            self.update()


    mis = Miska()
    krogi = []
    zadetih = 0
    vx = []
    vy = []
    zadel = []


    def miska():
        if not risar.klik:
            x, y = risar.miska
            mis.fly(x, y)
        else:
            x, y = risar.miska
            return x,y



    def pobarvaj(krog):
        c = krog.pen().color().lighter()
        c.setAlpha(192)
        krog.setBrush(c)


    def eksplozija(stev_zog):
        risar.klik = False
        xm, ym = -30, -30
        global zadetih
        global mis
        global vx
        global vy
        global zadel
        r = 10
        koordinate_miske = False
        pokaze = True
        zadete_koor = [(-500, -500) for k in range(stev_zog)]
        izginulih = 0
        izginile = False
        zadel = [False for k in range(stev_zog)]
        casi = collections.defaultdict(list)
        for i in range(stev_zog):
            x = randint(r, risar.maxX - r)
            y = randint(r, risar.maxY - r)
            barva = risar.nakljucna_barva()
            krog = risar.krog(x,y,r,barva)
            krogi.append(krog)
            vx.append(randint(-5, 5))
            od = randint(0, 1)
            if od == 1:
                vy.append(-math.sqrt(25 - vx[-1] ** 2))
            else:
                vy.append(math.sqrt(25 - vx[-1] ** 2))
        while not izginile:
            if risar.klik:
                casi[mis].append(time.time())
                if not koordinate_miske:
                    xm, ym = miska()
                    koordinate_miske = True
                if casi[mis][-1] - casi[mis][0] >= 4:
                    mis.fly(-30, -30)
                    xm, ym = -30, -30
                if xm == -30 and izginulih == zadetih:
                    izginile = True
                pokaze = False
            if pokaze:
                miska()
            for i in range(len(krogi)):
                krog = krogi[i]
                krog.setPos(krog.x()+ vx[i], krog.y() + vy[i])
                if koordinate_miske:
                    if math.sqrt((xm - krog.x())**2 + (ym - krog.y())**2) <= 40 or any(math.sqrt((k[0] - krog.x())**2 + (k[1] - krog.y())**2) <= 40 for k in zadete_koor):
                        if not zadel[i]:
                            zadetih += 1
                            xz = krog.x()
                            yz = krog.y()
                            zadete_koor[i] = (xz, yz)
                        zadel[i] = True
                    if zadel[i]:
                        vx[i] = 0
                        vy[i] = 0
                        krog.setRect(-30, -30, 60, 60)
                        pobarvaj(krog)
                        casi[krog].append(time.time())
                        if casi[krog][-1] - casi[krog][0] >= 4:
                            krog.hide()
                            krog.setPos(-300,-300)
                            zadete_koor[i] = (-500, -500)
                            if zadel[i]:
                                izginulih += 1
                                zadel[i] = False
                if not (r < krog.x() < risar.maxX -r):
                    vx[i] = - vx[i]
                if not (r < krog.y() < risar.maxY -r):
                    vy[i] = - vy[i]
            risar.cakaj(0.02)


    QMessageBox.information(None, "stopnja {}".format(oo), "Zadeni {} od {}".format(j * 2 + 1, j*5))
    eksplozija(j*5)

    risar.pobrisi()

    if zadetih > j*2:
        j -= 1
        oo += 1
    else:
        QMessageBox.information(None, "ŽOGANJE", "Zadetih žog je {}. Premalo".format(zadetih))



QMessageBox.information(None, "ŽOGANJE", "Zmaga")