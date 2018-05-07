import risar
import time
from random import *
from math import *
k = 0

class zoga:
    def __init__(self):
        self.ioe = 0
        self.x, self.y = risar.nakljucne_koordinate()
        self.barva = risar.nakljucna_barva()
        self.rad = 10
        self.toe = None
        self.sirina = 3
        self.smerx = randint(-5, 5)
        self.ali_minus = randint(1, 2)
        self.smery = sqrt(5**2 - self.smerx**2)
        if self.ali_minus == 1:
            self.smery = self.smery
        elif self.ali_minus == 2:
            self.smery = self.smery * -1

        self.object = risar.krog(self.x, self.y, self.rad, barva=self.barva, sirina=self.sirina)


    def skrij(self):
        self.object.hide()

    def eksplodiraj(self):
        self.smery = 0
        self.smerx = 0
        c = self.object.pen().color().lighter()
        c.setAlpha(192)
        self.object.setBrush(c)
        self.object.setRect(-30, -30, 60, 60)
        self.toe = time.time()
        self.ioe = randint(1, 999999)







zoge = []
eksplodirane = []

for i in range(0,30):
    zoge.append(zoga())

st_time = time.time()
eksplozije = 0
imamo_krog = False
run = True
miska = risar.krog(risar.maxX/2, risar.maxY/2, 30, barva=risar.bela, sirina=3)
krog_x = None
krog_y = None
check = False
clicks = []
sledim = True

while run == True:
    for zoga1 in zoge:
        if imamo_krog == True:
            if (zoga1 in eksplodirane):
                neki = 1
            else:
                if (zoga1.x < krog_x + 30) and (zoga1.x > krog_x - 30):
                    if (zoga1.y < krog_y + 30) and (zoga1.y > krog_y - 30):
                        zoga1.eksplodiraj()
                        k+=1
                        eksplodirane.append(zoga1)
                        run = False

                for pazi in eksplodirane:
                    if (zoga1.x < pazi.x + 30) and (zoga1.x > pazi.x - 30):
                        if (zoga1.y < pazi.y + 30) and (zoga1.y > pazi.y - 30):
                            zoga1.eksplodiraj()
                            k+=1
                            eksplodirane.append(zoga1)
                            break

        zoga1.x += zoga1.smerx
        zoga1.y += zoga1.smery

        zoga1.object.setPos(zoga1.x, zoga1.y)

        if (zoga1.x >= risar.maxX - 1):
            zoga1.smerx = zoga1.smerx * -1
        if (zoga1.x <= 0):
            zoga1.smerx = zoga1.smerx * -1
        if (zoga1.y >= risar.maxY - 1):
            zoga1.smery = zoga1.smery * -1
        if (zoga1.y <= 0):
            zoga1.smery = zoga1.smery * -1

    if(len(eksplodirane) > 0):
        check = True

    for zoga2 in eksplodirane:
        dell =[]
        if ((time.time() - zoga2.toe) > 4):
            eksplodirane = eksplodirane[::-1][:-1]
            eksplodirane = eksplodirane[::-1]
            risar.odstrani(zoga2.object)
    risar.cakaj(0.02)
    if sledim == True:
        mis_x, mis_y = risar.miska
        miska.setPos(mis_x, mis_y)


    if(risar.klik == True):
        krog_main = risar.krog(mis_x, mis_y, 30, barva=risar.modra, sirina=3)
        imamo_krog = True
        krog_x = mis_x
        krog_y = mis_y
        risar.klik = False
        sledim = False

    if imamo_krog == True:
        if check == True:
            if (len(eksplodirane) == 0):
                run = False

    '''if((time.time()-st_time) > 20):
        break'''