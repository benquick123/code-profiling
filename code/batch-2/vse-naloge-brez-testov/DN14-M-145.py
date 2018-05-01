import risar
from math import sqrt
from random import *
from PyQt5.QtWidgets import QMessageBox

global bombe
bombe = []
global game_end
class Ball:
    def __init__(self):
        self.r = 10
        self.miska_end_x=0
        self.miska_end_y=0
        self.x = randint(self.r, risar.maxX - self.r)
        self.y = randint(self.r, risar.maxY - self.r)
        self.x_s = 0
        self.y_s = 0
        self.vx = randint(-5, 5) #hitrost x
        self.vy = sqrt(5**2 - self.vx**2) #hitrost y
        barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
        self.krog = risar.krog(self.x, self.y, self.r, barva, 5)
        barva = risar.barva(255,255,255) #bela barva
        self.miska = risar.krog(risar.miska[0], risar.miska[1], 30, barva, 5) #def miske
        self.zadet=False #ce je objekt zadet
        self.alive=0 #cas do kdaj je bomba ziva
		
    def zadeta(self):
        if self.zadet == True:
            return 1
        else:
            return 0

    def reset_game(self): 
        self.krog.hide()
        risar.odstrani(self.krog)
        self.miska.hide()
        risar.odstrani(self.miska)
        self.miska_end_x = 0
        self.miska_end_y = 0
        self.x_s = 0
        self.y_s = 0
        risar.klik=False

    def dotik(self, bombe):
        a=[]
        if(len(bombe)>0):
            for b_x, b_y in bombe:
                a.append((self.x - b_x) ** 2 + (self.y - b_y) ** 2 <= (self.r + 30) ** 2)
        else:
            return all([(self.x - self.miska_end_x) ** 2 + (self.y - self.miska_end_y) ** 2 <= (self.r + 30) ** 2]) #ko ni bomb
        return any([(self.x - self.miska_end_x) ** 2 + (self.y - self.miska_end_y) ** 2 <= (self.r + 30) ** 2]+[any(a)])

    def show_us_the_wae(self, miska_x, miska_y, miska_klik):
        if(self.zadet==False):
            self.x += self.vx
            self.y += self.vy
            self.krog.setPos(self.x, self.y)
        if(miska_klik==False):
            self.miska.setPos(miska_x, miska_y)
            self.miska_end_x = miska_x
            self.miska_end_y = miska_y
        else:
            if(self.miska_end_x!=0):
                if(Ball.dotik(self, bombe)):
                    c = self.krog.pen().color().lighter()
                    c.setAlpha(192)
                    self.krog.setBrush(c)
                    self.krog.setRect(-30,-30,60,60)
                    self.zadet=True
                    if((self.x, self.y) not in bombe):
                        bombe.append((self.x, self.y))
                        self.x_s = self.x
                        self.y_s = self.y
        if(self.zadet==True):
            self.alive = self.alive + 1
            if (len(bombe) == 0): #trigger za konec igre
                global trigger
                trigger = True
        if(self.alive>150):
            if((self.x, self.y) in bombe):
                bombe.remove((self.x, self.y))
            self.krog.hide()
            risar.odstrani(self.krog)

    def we_need_to_build_a_wall(self):
        if self.x < self.r:
            self.vx = abs(self.vx)
        if self.x > risar.maxX - self.r:
            self.vx = -abs(self.vx)
        if self.y < self.r:
            self.vy = abs(self.vy)
        if self.y > risar.maxY - self.r:
            self.vy = -abs(self.vy)

def start(n):
    global zoge
    zoge = []
    for i in range(n):
        zoge.append(Ball())
    return zoge

def igra_start():
    game_end=False
    max=30
    stevilo_z=max
    for i in range(1,10):
        if(game_end==True):
            break
        print("Level" + str(i))
        global trigger
        trigger = False
        krogle = start(stevilo_z)
        print(len(zoge))
        timer=0
        if(i<5): #do lvl 5
            cilj=int(max/3)
        if(i>5): # po lvl 5
            cilj=int(stevilo_z/1.5)
        if(i>8): # po lvl 8
            cilj=stevilo_z-1
        QMessageBox.information(None, "Level "+ str(i), "Raztreli vsaj " + str(cilj) + " krogov")
        while True:
            for zoga in krogle:
                zoga.show_us_the_wae(risar.miska[0], risar.miska[1], risar.klik)
                zoga.we_need_to_build_a_wall()
            risar.cakaj(0.02)
            timer=timer+1
            if(trigger==True):
                st_zadetih=0
                for zoga in krogle:
                    st_zadetih=zoga.zadeta()+st_zadetih
                if(st_zadetih>=cilj):
                    QMessageBox.information(None, "Čestitamo!", "Raztrelili ste: " + str(st_zadetih) + "/" + str(stevilo_z) + " krogov")
                else:
                    QMessageBox.information(None, "Skoda :(","Raztrelili ste samo: " + str(st_zadetih) + "/" + str(stevilo_z) + " krogov")
                    game_end=True

                for zoga in krogle:
                    zoga.reset_game()
                stevilo_z=stevilo_z-3

                break
    risar.stoj() #konec igre

#program:
igra_start()
