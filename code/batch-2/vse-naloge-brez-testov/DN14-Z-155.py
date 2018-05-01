import risar
from time import *
from random import *
vreme=time()
class Kugla():
    def __init__(self):
        self.boja=risar.rdeca
        self.x=randint(0,risar.maxX-10)
        self.y=randint(0,risar.maxY-10)
        self.dy=2*random()-1
        self.dx=2*random()-1
        self.tjelo=risar.krog(self.x,self.y,10,self.boja)
        self.pause=0
        self.update()
    def naprej(self):
        self.x+=self.dx
        self.y+=self.dy
        self.update()
    def update(self):
        self.tjelo.setPos(self.x,self.y)
        if self.pause:
            self.wait(self.pause)






K=Kugla()
while time()-vreme<20:
    K.naprej()
    if K.x>=risar.maxX-10:
        K.dx=-K.dx
    elif K.y>=risar.maxY-10:
        K.dy=-K.dy
    elif K.x<=10:
        K.dx=-K.dx
    elif K.y<=10:
        K.dy=-K.dy

    risar.cakaj(0.0005)
    K.update
risar.stoj()

