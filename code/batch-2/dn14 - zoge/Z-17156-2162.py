import risar
import random
import math
import time
#from PyQt4.QtWidgets import QMessageBox

class kroglica:

    def __init__(self):

        self.barva = random.choice([risar.bela,risar.rdeca,risar.zelena, risar.modra, risar.vijolicna, risar.rumena, risar.siva, risar.rjava])
        self.x = random.randint(10,risar.maxX-20)
        self.y = random.randint(10,risar.maxY-20)
        self.hitrostx = random.choice((-5,5))
        self.hitrosty = random.choice((-5,5))
        self.krogla = risar.krog(self.x,self.y,10,self.barva)
        self.boom = False
        self.start = False
        self.vidna = True
        self.starttime = 0

    def premakni(self):
        self.y = self.y + self.hitrosty
        self.x = self.x + self.hitrostx
        if self.x-10 <= 0 or self.x+10 >= risar.maxX:
            self.hitrostx *= -1
        if self.y-10 <= 0 or self.y+10 >= risar.maxY:
            self.hitrosty *= -1

    def narisi(self):
        if self.start:
            if time.time()-self.starttime  >= 4:
                self.krogla.hide()
                self.boom = False
                self.vidna = False
        self.krogla.setPos(self.x, self.y)

    def dotik(self,kugle):
        for main in kugle:
            if main.boom and main.y <= self.y+30 and main.y >=self.y-30 and main.x<=self.x+30 and main.x>=self.x-30:
                self.boom = True
                if not self.start:
                    self.starttime = time.time()
                if time.time()-self.starttime < 4:
                    self.start = True
                self.hitrostx = 0
                self.hitrosty = 0
                self.krogla.setRect(-30, -30, 60, 60)
                tmp = self.krogla.pen().color().lighter()
                tmp.setAlpha(192)
                self.krogla.setBrush(tmp)

class miskrog:

    def __init__(self):
        self.x,self.y = risar.miska
        self.krogla = risar.krog(self.x,self.y,30)
        self.boom = False
        self.start = False
        self.vidna = True
        self.starttime = 0

    def premakni(self):
        if self.start:
            if time.time()-self.starttime  >= 4:
                self.krogla.hide()
                self.boom = False
                self.vidna = False
        if not self.boom and not self.start:
            self.boom = risar.klik
            self.x,self.y = risar.miska
        else:
            if not self.start:
                self.starttime=time.time()
            if time.time() - self.starttime < 4:
                self.start = True


    def narisi(self):
        self.krogla.setPos(self.x, self.y)

    def dotik(self,kugle):
        pass

class igra:
    def __init__(self):
        self.stopnja = 0
        self.stkroglcilj = [(1,5),(2,10),(4,15),(6,20),(10,25),(15,30),(18,35),(22,40),(30,45),(37,50)]
        self.kroglice = []
        self.pocenekrogle = set()
        self.konec = False
        self.counterpocenih = -1

    def postaviIgro(self):
        self.pocenekrogle = set()
        risar.barvaOzadja(risar.bela)
        while not risar.klik:
            if self.counterpocenih == -1:
                risar.besedilo(risar.maxX / 2 - 140, risar.maxY / 2 - 70,
                               "Začetek nove stopnje!\n\n"+
                               "Razstreliti morate : " +
                               str(self.stkroglcilj[self.stopnja][0]) + " od " +
                               str(self.stkroglcilj[self.stopnja][1]) + " žog, \nda napredujete stopnjo " +
                               str(self.stopnja + 1) + "!" + "\n\n\nZa začetek pritisni gumb na miški.", risar.crna)
            else:
                risar.besedilo(risar.maxX / 2 - 140, risar.maxY / 2 - 70,
                               "Začetek nove stopnje!\n\n"+
                               "Razstreliti morate : " +
                               str(self.stkroglcilj[self.stopnja][0]) + " od " +
                               str(self.stkroglcilj[self.stopnja][1]) + " žog, \nda napredujete stopnjo " +
                               str(self.stopnja + 1) + "!" +"\nRazstreljenih žog je bilo: "+str(self.counterpocenih)+ "\n\n\nZa začetek pritisni gumb na miški.", risar.crna)
            risar.cakaj(0.02)
        risar.klik = False
        risar.pobrisi()
        risar.barvaOzadja(risar.crna)
        self.kroglice = [kroglica() for x in range(self.stkroglcilj[self.stopnja][1])]
        self.miska =miskrog()
        self.kroglice.append(self.miska)

    def start(self):
        self.postaviIgro()
        levogor = risar.besedilo(0,0,str(len(self.pocenekrogle)-1)+"/"+str(self.stkroglcilj[self.stopnja][0]))
        while not self.konec:
            levogor.setPlainText(str(len(self.pocenekrogle-{self.miska}))+"/"+str(self.stkroglcilj[self.stopnja][0]))
            for x in self.kroglice:
                x.premakni()
                x.dotik(self.kroglice)
                x.narisi()
                if x.boom:
                    self.pocenekrogle.add(x)
            risar.cakaj(0.02)
            if len(self.pocenekrogle)>0 :
                if len(self.pocenekrogle-{self.miska})>self.stkroglcilj[self.stopnja][1] or  any(x.vidna for x in self.pocenekrogle) :
                    self.konec = False
                else:
                    self.konec = True
        risar.pobrisi()
        risar.barvaOzadja(risar.bela)
        if len(self.pocenekrogle-{self.miska}) >= self.stkroglcilj[self.stopnja][0]:
            self.stopnja+=1
        else:
            risar.klik = False
            while not risar.klik:
                risar.besedilo(risar.maxX/2 - 140 ,risar.maxY/2 - 70,"PORAZ!\n\nPočenih žog je bilo: "+str(len(self.pocenekrogle - {self.miska}))+"\npotrebno jih je: "+str(self.stkroglcilj[self.stopnja][0])+"\n\n\n ZA ZAČETEK PRTISNI GUMB NA MIŠKI",risar.crna)
                risar.cakaj(0.02)
        self.counterpocenih = len(self.pocenekrogle - {self.miska})
        risar.pobrisi()
        risar.klik = False
        self.konec = False

a = igra()

while a.stopnja < 10:
    a.start()