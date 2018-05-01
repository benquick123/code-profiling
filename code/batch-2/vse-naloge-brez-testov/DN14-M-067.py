import risar
from random import *
from math import *
import time

class Zoge:
    def __init__(self):
        self.x, self.y = risar.nakljucne_koordinate()
        self.krogec = risar.krog(self.x,self.y,10,barva=risar.nakljucna_barva(),sirina=2)
        self.kot = randint(0,360)
        self.odboj_strani = 1
        self.odboj_v_s = 1

        trajanje = time.time()
        while time.time() - trajanje < 20:
            self.premik()
            self.Odboj()
            self.krogec.setPos(self.x,self.y)
            risar.cakaj(0.005)



    def premik(self):
        self.x += cos(radians(self.kot)) * self.odboj_strani
        self.y += sin(radians(self.kot)) * self.odboj_v_s

    def Odboj(self):
        if self.x < 0 or self.x > risar.maxX:
            self.odboj_strani *= -1
        if self.y < 0 or self.y > risar.maxY:
            self.odboj_v_s *= -1





Zoge()






