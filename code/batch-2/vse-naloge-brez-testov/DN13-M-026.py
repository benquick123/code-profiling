'''
    Opis programa: osnovne vaje z objekti
    Avtor: Blaž Kumer
    Datum: 9. 1. 2018


'''


class Minobot:
    def __init__(self):
        self.x, self.y = 0,0
        self.smer = 0
        self.ukazi=[]

    def naprej(self,d):
        if self.smer%2==0:
            if self.smer==0:
                self.x=self.x+d

            else:
                self.x=self.x-d
        else:
            if self.smer==1:
                self.y=self.y-d
            else:
                self.y=self.y+d
        self.ukazi.append(d)
    def desno(self):
        self.smer+=1
        if self.smer>3:
            self.smer-=4
        self.ukazi.append("D")
    def levo(self):
        self.smer-=1
        if self.smer<0:
            self.smer+=4
        self.ukazi.append("L")
    def koordinate(self):
        return (self.x,self.y)

    def razdalja(self):
        return abs(self.x)+abs(self.y)

    def razveljavi(self):
        if len(self.ukazi)>0:
            if self.ukazi[-1]=="D":
                self.levo()
                self.ukazi = self.ukazi[:-2]
            elif self.ukazi[-1]=="L":
                self.desno()
                self.ukazi = self.ukazi[:-2]
            else:
                self.naprej(-self.ukazi[-1])
                self.ukazi = self.ukazi[:-2]
