from math import sqrt
import inspect

class Minobot:
    def __init__(self):
        self.x, self.y = 0,0
        self.smer="E"
        self.smeri = "NESW"
        self.ismer = self.smeri.index(self.smer)
        self.ukazi=[]
        self.razveljava=False
        
    def update_ismer(self):
        self.ismer = self.smeri.index(self.smer)
        
    def naprej(self,d):
        premiki = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dx, dy = premiki[self.ismer]
        self.x += dx * d
        self.y += dy * d
        if not self.razveljava:
            self.ukazi.append(d)
        
    def desno(self):
        self.smer = self.smeri[(self.ismer + 1) % 4]
        self.update_ismer()
        if not self.razveljava:
            self.ukazi.append("d")
        
    def levo(self):
        self.smer = self.smeri[(self.ismer - 1) % 4]
        self.update_ismer()
        if not self.razveljava:
            self.ukazi.append("l")
        
    def koordinate(self):
        return (self.x,self.y)
    
    def razdalja(self):
        return abs(0-self.x)+abs(0-self.y)

    def razveljavi(self):
        self.razveljava=True
        if len(self.ukazi)>0:
            if str(self.ukazi[-1])=="d":
                self.levo()
            elif str(self.ukazi[-1])=="l":
                self.desno()
            else:
                if len(self.ukazi)>0:
                    self.naprej(-self.ukazi[-1])
            self.ukazi= self.ukazi[:-1]
        self.razveljava=False

        



