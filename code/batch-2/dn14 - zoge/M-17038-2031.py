import risar
from random import randint, random,uniform,choice
from math import *

#poskusil sem usposobiti za 8, ampak mi je zmanjkalo časa, morda so v kodi ostanki naloge za osem. Miško sem pustil ker lepše zgleda

class Circle:
    def __init__(self):

        move=1
        self.maxx=risar.maxX-12
        self.maxy=risar.maxY-12
        self.x=randint(0,self.maxx)
        self.y=randint(0,self.maxy)
        self.color=risar.nakljucna_barva()
        self.speedx=uniform(-5,5)
        self.speedy=(sqrt(25-self.speedx**2))

        rd=randint(1,2)
        if rd == 1:
            self.speedy=-self.speedy
        else:
            no = 0
        self.c = risar.krog(self.x, self.y, 10, barva=self.color, sirina=3)



    def move(self):

            self.c.setPos((self.x+self.speedx),(self.y+self.speedy))
            self.x=self.x+self.speedx
            self.y = self.y + self.speedy
            if self.x<=10:
                self.speedx=-self.speedx

            if self.y<=10:
                self.speedy=-self.speedy

            if self.x>self.maxx:
                self.speedx= -self.speedx
            if self.y>self.maxy:
                self.speedy=-self.speedy



d = risar.krog(risar.miska[0], risar.miska[1], 30, barva=risar.bela, sirina=3)
c = []
for i in range(30):
    c.append(Circle())


for i in range(830):
    for all in c:
        all.move()
    risar.cakaj(0.02)

    if risar.klik != True:
        d.setPos(risar.miska[0], risar.miska[1])















