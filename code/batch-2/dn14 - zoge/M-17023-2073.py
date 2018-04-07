import risar
from random import randrange
from math import *
from PyQt5.QtWidgets import QMessageBox

class Krog:
    def __init__(self):
        r = 10
        self.x = randrange(0+5,risar.maxX-5)
        self.y = randrange(0+5,risar.maxY-5)
        self.angle = randrange(0,360)
        self.barva = risar.nakljucna_barva()
        self.body = risar.krog(self.x, self.y, r, barva=self.barva, sirina=2)
        self.timer = 4.0
        self.move = True

    def forawrd(self,speed):
        self.x = self.x + cos(radians(self.angle))*speed
        self.y = self.y + sin(radians(self.angle))*speed
        self.odboj()
        self.update()

    def odboj(self):
        if self.x < 0+5:
            self.angle = 180 - self.angle
        if self.x > risar.maxX - 5:
            self.angle = 180 - self.angle
        if self.y < 0+5:
            self.angle = - self.angle
        if self.y > risar.maxY - 5:
            self.angle = - self.angle

    def eksplozija(self):
        self.move = False


        #grafika:
        self.body.setRect(-30, -30, 60, 60)

        c = self.body.pen().color().lighter()
        c.setAlpha(192)
        self.body.setBrush(c)

    def update(self):
        self.body.setPos(self.x,self.y)



seznam_krogov = []



speed = 2.5
#speed = 5
stopnja = 1
zapri_vse = False

def je_konec():
    for e in seznam_krogov:
        if not e.move:
            return False
    return True

while not zapri_vse:
    QMessageBox.information(None, "To je "+str(stopnja)+" stopnja","Razstreliti moras "+ str(stopnja * 3) + " od "+ str(stopnja * 3+3)+ " zog!")
    for i in range(stopnja * 3+3):
        seznam_krogov.append(Krog())
    igraj = True
    prvic = True
    stevec = 0
    risar.klik = False
    miska = Krog()
    miska.body.setRect(-30, -30, 60, 60)

    while igraj:
        for e in seznam_krogov:
            if e.move:
                e.forawrd(speed)
            else:
                e.timer -= 0.01

            if e.timer <= 0:
                e.body.hide()
                seznam_krogov.remove(e)


        if not risar.klik:
            miska.x, miska.y = risar.miska
        else:
            if prvic:
                seznam_krogov.append(miska)
                miska.eksplozija()
                prvic = False

            for i in range(len(seznam_krogov)):
                for j in range(i + 1, len(seznam_krogov)):
                    if seznam_krogov[i].move != seznam_krogov[j].move:
                            if sqrt((seznam_krogov[i].x - seznam_krogov[j].x) ** 2 + (seznam_krogov[i].y - seznam_krogov[j].y) ** 2) < 40:
                                if seznam_krogov[i].move:
                                    seznam_krogov[i].eksplozija()
                                else:
                                    seznam_krogov[j].eksplozija()
                                stevec += 1
            if je_konec():
                izbrisi = []
                for e in seznam_krogov:
                    izbrisi.append(e)
                    e.body.hide()

                for e in izbrisi:
                    seznam_krogov.remove(e)


                if stopnja * 3 <= stevec:
                    QMessageBox.information(None, "Opravil si stopnjo "+str(stopnja), "Število eksplodiranih žog je "+str(stevec)+"\nPogoj za naslednjo stopnjo je "+str(stopnja*3))
                    stopnja += 1
                    if stopnja >= 11:
                        QMessageBox.information(None, "Useplo ti je!", "Dosegel si najvišjo stopnjo!")
                        zapri_vse = True
                else:
                    QMessageBox.information(None, "Poskusi ponovno", "Število eksplodiranih žog je " + str(stevec) + "\nPogoj za naslednjo stopnjo je " + str(stopnja * 3))
                break

        miska.body.setPos(miska.x,miska.y)
        risar.cakaj(0.01)




