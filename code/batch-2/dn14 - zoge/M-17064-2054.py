import risar
from random import randint
from math import sqrt

risar.obnavljaj = False

class Jakob:
    def  __init__(self):
        nk = risar.nakljucne_koordinate()
        self.x, self.y = abs(nk[0] - 10), abs(nk[1] - 10)
        self.r = 10
        self.barva = risar.nakljucna_barva()
        self.sirina = 3


    def narisi(self):
        
        return risar.krog(self.x, self.y, self.r, barva=self.barva, sirina=self.sirina)


    def premik(self):
        f = randint(-5,5)
        #g = randint(-5,5)
        g = sqrt(25 - f ** 2)
        i = 0
        while i < 20:
            if self.x > risar.maxX - 10 or self.x < 10:
                f = -f
            if self.y < 10 or self.y > risar.maxY - 10:
                g = -g
            
            self.x += f
            self.y += g

            a = risar.krog(self.x, self.y, self.r, barva=self.barva, sirina=self.sirina)
            
            
            risar.cakaj(0.02)
            risar.odstrani(a)
            risar.obnovi()
            i += 0.02
            #print(i)
            


    
            

a = Jakob()


a.premik()



"""
class Jakob:
    def  __init__(self):
        
        self.x, self.y = 0, 0
        self.r = 10
        self.barva = risar.bela
        self.sirina = 3
        #self.krog = risar.krog(self.x, self.y, self.r, barva=self.barva, sirina=self.sirina)



    def krog(self):
        nk = risar.nakljucne_koordinate()
        self.x, self.y = nk[0], nk[1]
        self.barva = risar.nakljucna_barva()
        #self.krog = risar.krog(self.x, self.y, self.r, barva=self.barva, sirina=self.sirina)
        return risar.krog(self.x, self.y, self.r, barva=self.barva, sirina=self.sirina)
        
    def kr(self):
        s = []
        for i in range(30):
            s.append(Jakob.krog(self))




            
a = Jakob()
a.kr()

"""
