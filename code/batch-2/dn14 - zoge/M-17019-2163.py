import risar
from random import randint
from math import sqrt,isclose
import time
from PyQt5.QtWidgets import QMessageBox



class Igrax:
    def __init__(self, barva):
        self.x =randint(0,risar.maxX)
        self.y =randint(0,risar.maxY)
        self.hitrostx = randint(-5,5)
        self.hitrosty = sqrt(25+self.hitrostx**2)
        self.smer=0
        self.barve = barva
        self.krog = risar.krog(self.x, self.y, 10, self.barve, 1)
        risar.barvaOzadja(risar.barva(250, 250, 250))
        self.boom = False

        self.cas = time.time()
        self.klik = False

        self.premik()
#Namig: za x-komponento hitrosti določite naključno število med -5 in 5. Komponento y izračunate po Pitagori.)
#Vse kroglice naj se premikajo z enako hitrostjo, namreč 5 točk na eno iteracijo zanke; v zanko dodajte 0.02 sekunde pavze.

    def premik(self):
        #print("Hirost je : {}, koordinate x je: {}in y je {}: ".format(self.hitrostx, self.x, self.y))

        self.x += self.hitrostx
        self.y += self.hitrosty
        if self.x >= risar.maxX-10 or self.x <=10:
            self.hitrostx = -self.hitrostx
        if self.y >= risar.maxY-10 or self.y <=10:
            self.hitrosty = -self.hitrosty


        if time.time() - self.cas > 4 and self.klik:
            self.krog.hide()

        if not self.boom:
            self.cas = time.time()
            self.krog.setPos(self.x, self.y)

        else:
            self.krog.setRect(-30, -30, 60, 60)
            c = self.krog.pen().color().lighter()
            c.setAlpha(192)
            self.krog.setBrush(c)
        #risar.cakaj(0.00000001)

        if time.time() - self.cas > 4:
            self.krog.hide()





class Igravec():
    def __init__(self, koliko):
        risar.pobrisi()
        self.koliko = koliko
        self.seznam =[]
        self.barve =[]
        #generator zelene barve
        self.stevile = [x for x in range(1,koliko+1)]
        for i in self.stevile:
            self.stevile[i-1] = i*255/koliko
        for i in range(1,koliko+1):
            #risar.barva(rgb[0], rgb[1], rgb[-1])
            self.barve.append(risar.barva(self.stevile[i-1], 23,60))
        #print(self.stevile)
        for i in range(koliko):
            self.seznam.append(Igrax(self.barve[i]))
        self.xm = 0
        self.ym = 0
        self.miska = risar.miska
        self.klik = False
        self.mis = risar.krog(0, 0, 30, risar.barva(116, 5, 212), 1)
        self.cas = time.time()
        self.boomkrogi = []
        self.konec = True
        #print("klik je vreensoti {}".format(self.klik))
        self.premik()
        risar.cakaj(0.2)
        risar.klik = False
        self.konec = 125
        risar.barvaOzadja(risar.barva(250, 250, 250))

    def boom(self,x,y):
        #da preveri ce se zaleti z katerem koli vv seznamu
        #preveri ali zaleten krog [e aktualen
        for xx, yy, timex in self.boomkrogi:
            if isclose(xx, x, abs_tol=35)  and isclose(yy,y, abs_tol=35) and time.time() - timex < 4:
                #print("BOOM BOOM in {}".format(time.time() - timex) )
                self.konec = len(self.boomkrogi)
                #self.cas = time.time() # odvzami cas in ga klici takrt ko je mis true
                #risar.cakaj(1)
                #self.mis.hide() # kdaj se skrije
                #risar.stoj()
                return True
        return False


    def izgine(self):
        #print("XXXXXXXXXXXXXXXXxxxxxXxxXXXXXXXXX")
        if not self.klik:
            self.cas = time.time()
        if time.time() - self.cas > 4 and self.klik and self.cas:
            self.mis.hide()
            #self.krog.hide()
            #print("Izgine kroglica")
            #vr\i jo ven iz boomkrogi


    def premik(self):

        while self.konec:
            #tru zamenjaj zazadnjim elementom v seznamu ;e ima aktualen cas
            if( time.time() - self.cas > 1 and self.klik and (time.time() -self.boomkrogi[-1][2]) >4  ) or len(self.boomkrogi) == self.koliko +1:
                # klici konec igre

                self.konec = len(self.boomkrogi) -1
                #print('Self.konec je {}'.format(self.konec))
                QMessageBox.information(None, "Konec igre", "Konec igre, razstrelili ste {} žog. ".format(self.konec))

                self.konec = False
            self.izgine()

            self.klik = risar.klik
            #print("Ali je miska kliknena{}".format(self.klik))
            for zelva in self.seznam:
                zelva.premik()
                # preveri ;e sem kliknil, preveri ali se zaleti ce se zalti ji dodaj boom in vnesi kordiante kroga v boomzeznam z casom
                if self.klik:
                    if zelva.boom != True:
                        if self.boom(zelva.x, zelva.y):
                            zelva.boom = True
                            self.boomkrogi.append((zelva.x, zelva.y, time.time()))


            risar.cakaj(0.02)
            if not self.klik:
                self.mis.setPos(risar.miska[0], risar.miska[1])
                self.xm = risar.miska[0]
                self.ym = risar.miska[1]
            #ce je seznam prazen potem dodaj element v boomkrogiu in pobrarvaj misko
            else:
                if len(self.boomkrogi)==0:
                    self.boomkrogi.append((self.xm, self.ym, time.time()))
                    c = self.mis.pen().color().lighter()
                    c.setAlpha(255)
                    self.mis.setBrush(c)

    def koneccano(self):
        return len(self.boomkrogi)




                    #print("Trenutni ca je {} in self.cas je {} stanej risar.miska je {}".format(time.time(), self.cas, self.klik))
            #print(time.time() - self.cas)



class Igrazadest(Igravec):
    def __init__(self):

        self.koncan = 0
        self.tezavnost =[0,1,2,5,10,20,50,100,200,2,3]
        self.zmaga=     [0,1,1,3,6, 15,40,50,100,2,3]
        #self.zmaga=     [0,1,1,1,1, 1,40,50,100,1,1] # ce ti ne gre dobro, si lahko malce poenostavis tezavnost
        self.stopnja = 1



        # Sele tukaj klici druge funkcije
        self.igra()

    def igra(self):
        QMessageBox.information(None, "Obvestilo", "Malce je popravljena barvan shema, pa prijetno igranje")
        while self.stopnja < 11:
            QMessageBox.information(None, "Igra z {} žogo".format(self.tezavnost[self.stopnja]), "Živjo gremo se igrat. Za napredovanje morate razstleiti vsaj {} od {}.".format(self.zmaga[self.stopnja], self.tezavnost[self.stopnja] ))
            igramose = Igravec(self.tezavnost[self.stopnja])

            self.konec = igramose.koneccano()-1
            #print("raszrelil sem {} zog".format(self.konec))
            if self.konec >= self.zmaga[self.stopnja]:


                self.stopnja+=1
                if self.stopnja == 11:
                    QMessageBox.information(None, "Cestitke", "Cestitke koncali ste igro na vrsti je prokrastinacija")
                else:

                    #print("Napredujem v {} stopnjo".format(self.stopnja))
                    QMessageBox.information(None, "Cestitke","Napredujete v {} level.".format(self.stopnja))
            else:
                QMessageBox.information(None, "Se enkrat", "Ostajate v {} level.".format(self.stopnja))
            #print(self.konec)










Igrazadest()


