import risar
import random
import math

class Krog:
    def __init__(self):
        self.x, self.y = risar.nakljucne_koordinate()
        self.angle = random.randint(1,360)
        self.barva=risar.nakljucna_barva()
    def narisi(self):
        self.narisan_krog=risar.krog(self.x, self.y, 10, barva=self.barva, sirina=5)
    def naprej(self,s):
        angle = math.radians(self.angle)
        nx, ny = self.x + s * math.cos(angle), self.y + s * math.sin(angle)
        if risar.maxX-5<nx or  5>nx  :
            self.odboj(True)
        if risar.maxY-5<ny or 5>ny:
            self.odboj(False)
            nx, ny = self.x + s * math.cos(angle), self.y + s * math.sin(angle)
        self.x, self.y = nx, ny
        self.narisan_krog.setPos(self.x,self.y)
    def odboj(self,xy):
        if xy:
            self.angle = (self.angle-90/2)
        else:
            self.angle = -self.angle


k=Krog()
k.narisi()

for i in range(1500):
    risar.cakaj(0.005)
    k.naprej(2)



risar.stoj()


