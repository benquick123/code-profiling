import risar
from random import randint
import math
import time
from PyQt5.QtWidgets import QMessageBox
class obv3:

    def __init__(self):
        self.x,self.y=risar.nakljucne_koordinate()
        self.x,self.y=self.preveriZacPoz()
        self.barva=risar.nakljucna_barva()
        self.sirina=2
        self.krog=risar.krog(self.x, self.y, 10, barva=self.barva, sirina=self.sirina)
        self.sx,self.sy=self.hitrost()

    def preveriZacPoz(self):
        maxX = risar.maxX - 1
        maxY = risar.maxY - 1
        if self.x+13> maxX-7:
            self.x=self.x-14
        if self.x - 13 < 7:
            self.x = self.x + 14
        if self.y + 13 > maxY - 7:
            self.y = self.y - 14
        if self.y - 13 < 7:
            self.y = self.y + 14



        return self.x,self.y
    def hitrost(self):
        sx=randint(-4,4)
        sy=math.sqrt(25-(sx*sx))
        rnd=randint(0,1)
        if rnd ==1:
            return sx,sy
        else:
            return sx,-sy

    def risi1(self):
        t_end=time.time()+20
        maxX = risar.maxX - 1
        maxY = risar.maxY - 1
        while time.time()<=t_end:
            self.x += self.sx
            self.y += self.sy
            if self.x + 12 >= maxX:
                self.sx = -self.sx
            elif self.y + 12 >= maxY:
                self.sy = -self.sy
            elif self.y - 12 <= 0:
                self.sy = abs(self.sy)
            elif self.x - 10 <= 0:
                self.sx = abs(self.sx)
            self.krog.setPos(self.x, self.y)
            risar.cakaj(0.02)

    def risi30(self,tab):
        t_end = time.time() + 20
        maxX = risar.maxX - 1
        maxY = risar.maxY - 1
        while time.time() <= t_end:
            for i in tab:
                i.x += i.sx
                i.y += i.sy
                if i.x + 12 >= maxX:
                    i.sx = -i.sx
                elif i.y + 12 >= maxY:
                    i.sy = -i.sy
                elif i.y - 12 <= 0:
                    i.sy = abs(i.sy)
                elif i.x - 10 <= 0:
                    i.sx = abs(i.sx)
                i.krog.setPos(i.x, i.y)
            risar.cakaj(0.02)

    def risi30Klik(self,tab,miska):
        maxX = risar.maxX - 1
        maxY = risar.maxY - 1
        g=True
        while g:
            for i in tab:
                if not risar.klik:
                    miska.x,miska.y=risar.miska
                    miska.krog.setPos(miska.x,miska.y)
                else:
                    d=abs(math.sqrt((abs(i.x-miska.x)**2)+(abs(i.y-miska.y)**2)))
                    if d<=(32+12):
                        g=False

                i.x += i.sx
                i.y += i.sy
                if i.x + 12 >= maxX:
                    i.sx = -i.sx
                elif i.y + 12 >= maxY:
                    i.sy = -i.sy
                elif i.y - 12 <= 0:
                    i.sy = abs(i.sy)
                elif i.x - 10 <= 0:
                    i.sx = abs(i.sx)
                i.krog.setPos(i.x, i.y)
            risar.cakaj(0.02)

    def risi301Bum(self,tab,miska):
        maxX = risar.maxX - 1
        maxY = risar.maxY - 1
        bum=[]
        stBal=len(tab)
        dodajVBum=[]
        bumbil = False
        jeKlik=False
        while True:
            for krogec in tab:
                if not risar.klik:
                    miska.x, miska.y = risar.miska
                    miska.krog.setPos(miska.x, miska.y)
                    jeKlik=True
                else:
                    if jeKlik:
                        bum.append((miska,time.time()+4,miska.x,miska.y))
                        bumbil = True
                        jeKlik=False

                    for objekt,cas,px,py in bum:
                        razdalja = abs(math.sqrt((abs(krogec.x - px) ** 2) + (abs(krogec.y - py) ** 2)))
                        if razdalja<=(32+12):
                            dodajVBum=[(krogec,time.time()+4,krogec.x,krogec.y)]
                            if krogec in tab:
                                 tab.remove(krogec)
                            krogec.krog.hide()
                            k = krogec.barva
                            krogec.krog = risar.krog(krogec.x, krogec.y, 30, barva=k, sirina=krogec.sirina)
                            c = krogec.krog.pen().color().lighter()
                            c.setAlpha(192)
                            krogec.krog.setBrush(c)
                        elif time.time()>=bum[0][1]:
                            bum[0][0].krog.hide()
                            del bum[0]
                    if len(dodajVBum)==1:
                        bum.append(dodajVBum[0])
                        dodajVBum=[]
                krogec.x += krogec.sx
                krogec.y += krogec.sy
                if krogec.x + 12 >= maxX:
                    krogec.sx = -krogec.sx
                elif krogec.y + 12 >= maxY:
                    krogec.sy = -krogec.sy
                elif krogec.y - 12 <= 0:
                    krogec.sy = abs(krogec.sy)
                elif krogec.x - 10 <= 0:
                    krogec.sx = abs(krogec.sx)
                krogec.krog.setPos(krogec.x, krogec.y)


            if len(tab)==0:
                while True:
                    if len(bum)==0:
                        break
                    if time.time()>=bum[0][1]:
                        bum[0][0].krog.hide()
                        del bum[0]

                    risar.cakaj(0.2)
                QMessageBox.information(None, "Rezultat", "Počili ste vse balončke! ("+str(stBal-len(tab))+")")
                break
            elif bumbil and len(bum) == 0 or len(tab)<stBal and len(bum)==0:
                QMessageBox.information(None, "Rezultat", "Počeni balončki: " + str(stBal-len(tab)))
                break

            risar.cakaj(0.02)

    def risi301BumBum(self, tab, miska):
        maxX = risar.maxX - 1
        maxY = risar.maxY - 1
        bum = []
        stBal = len(tab)
        dodajVBum = []
        bumbil = False
        jeKlik = False
        while True:
            for krogec in tab:
                if not risar.klik:
                    miska.x, miska.y = risar.miska
                    miska.krog.setPos(miska.x, miska.y)
                    jeKlik = True
                else:
                    if jeKlik:
                        bum.append((miska, time.time() + 4, miska.x, miska.y))
                        bumbil = True
                        jeKlik = False

                    for objekt, cas, px, py in bum:
                        razdalja = abs(math.sqrt((abs(krogec.x - px) ** 2) + (abs(krogec.y - py) ** 2)))
                        if razdalja <= (32 + 12):
                            dodajVBum = [(krogec, time.time() + 4, krogec.x, krogec.y)]
                            if krogec in tab:
                                tab.remove(krogec)
                            krogec.krog.hide()
                            k = krogec.barva
                            krogec.krog = risar.krog(krogec.x, krogec.y, 30, barva=k, sirina=krogec.sirina)
                            c = krogec.krog.pen().color().lighter()
                            c.setAlpha(192)
                            krogec.krog.setBrush(c)
                        elif time.time() >= bum[0][1]:
                            bum[0][0].krog.hide()
                            del bum[0]
                    if len(dodajVBum) == 1:
                        bum.append(dodajVBum[0])
                        dodajVBum = []
                krogec.x += krogec.sx
                krogec.y += krogec.sy
                if krogec.x + 12 >= maxX:
                    krogec.sx = -krogec.sx
                elif krogec.y + 12 >= maxY:
                    krogec.sy = -krogec.sy
                elif krogec.y - 12 <= 0:
                    krogec.sy = abs(krogec.sy)
                elif krogec.x - 10 <= 0:
                    krogec.sx = abs(krogec.sx)
                krogec.krog.setPos(krogec.x, krogec.y)

            if len(tab) == 0:
                while True:
                    if len(bum) == 0:
                        break
                    if time.time() >= bum[0][1]:
                        bum[0][0].krog.hide()
                        del bum[0]

                    risar.cakaj(0.2)
                return stBal
                break
            elif bumbil and len(bum) == 0 or len(tab)<stBal and len(bum)==0:
                for skrij in tab:
                    skrij.krog.hide()
                return stBal - len(tab)
                break

            risar.cakaj(0.02)


def ocena6():
    oc6=obv3()
    oc6.risi1()

def ocena7():
    tab=[]
    for a in range(0,30):
        x=obv3()
        tab.append(x)
    tab[0].risi30(tab)

def ocena8():
    miska=obv3()
    miska.krog.hide()
    miska.krog = risar.krog(miska.x, miska.y, 30, barva=risar.barva(255,255,255), sirina=2)
    tab = []
    for a in range(0, 30):
        x = obv3()
        tab.append(x)
    tab[0].risi30Klik(tab,miska)

def ocena9():
    miska = obv3()
    miska.krog.hide()
    miska.krog = risar.krog(miska.x, miska.y, 30, barva=risar.barva(255, 255, 255), sirina=2)
    tab = []
    for a in range(0, 15):
        x = obv3()
        tab.append(x)
    tab[0].risi301Bum(tab, miska)

def ocena10():
    ponovi = False
    leveli = [(5,2),(8,3),(10,5),(15,8),(20,11),(25,13),(30,16),(35,18),(40,21),(60,40)]
    for i in range(len(leveli)):
        risar.klik = False
        miska = obv3()
        miska.krog.hide()
        miska.krog = risar.krog(miska.x, miska.y, 30, barva=risar.barva(255, 255, 255), sirina=2)
        if ponovi:
            i-=1
            ponovi = False
        level = leveli[i]
        tab = []
        for a in range(0, level[0]):
            x = obv3()
            tab.append(x)

        QMessageBox.information(None, "Navodila", "Razstreli "+str(level[1])+" od "+str(level[0])+" žog")

        pubu = int(tab[0].risi301BumBum(tab, miska))
        if pubu < level[1]:
            ponovi = True
            QMessageBox.information(None, "Navodila", "Razstrelil si premalo žog ("+str(pubu)+"), poizkusi še 1x")



###########Klici############
#ocena6()
#ocena7()
#ocena8()
#ocena9()
#ocena10()