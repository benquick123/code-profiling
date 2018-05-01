import math

class Minobot:
    def __init__(self):
        self.x=0
        self.y=0
        self.smer="E"
        self.ukazi=[]

    def naprej(self,d):
        self.ukazi.append("naprej"+":"+str(d))
        if self.smer == "E":
            self.x=self.x+d
        if self.smer == "W":
            self.x=self.x-d
        if self.smer == "N":
            self.y=self.y+d
        if self.smer == "S":
            self.y=self.y-d
    def nazaj(self):

        beseda = self.ukazi[-1]

        razcleni = beseda.split(":")
        k=int(razcleni[1])
        if self.smer == "E":
            self.x=self.x-k
        if self.smer == "W":
            self.x=self.x+k
        if self.smer == "N":
            self.y=self.y-k
        if self.smer == "S":
            self.y=self.y+k
        self.ukazi[:]=self.ukazi[:-1]

    def desno(self):
        self.ukazi.append("desno")
        if self.smer=="E":
            self.smer="S"
        elif self.smer=="S":
            self.smer="W"
        elif self.smer=="W":
            self.smer="N"
        elif self.smer=="N":
            self.smer="E"

    def desno_nazaj(self):

        if self.smer=="E":
            self.smer="S"
        elif self.smer=="S":
            self.smer="W"
        elif self.smer=="W":
            self.smer="N"
        elif self.smer=="N":
            self.smer="E"
        self.ukazi[:] = self.ukazi[:-1]
    def levo(self):
        self.ukazi.append("levo")
        if self.smer=="E":
            self.smer="N"
        elif self.smer=="N":
            self.smer="W"
        elif self.smer=="W":
            self.smer="S"
        elif self.smer=="S":
            self.smer="E"
    def levo_nazaj(self):

        if self.smer=="E":
            self.smer="N"
        elif self.smer=="N":
            self.smer="W"
        elif self.smer=="W":
            self.smer="S"
        elif self.smer=="S":
            self.smer="E"
        self.ukazi[:] = self.ukazi[:-1]
    def koordinate(self):
        return self.x,self.y
    def razdalja(self):
        x1=0
        y1=0
        return abs(self.x-x1)+abs(self.y-y1)

    def razveljavi(self):
        if len(self.ukazi)>0:
            beseda = self.ukazi[-1]
            razcleni = beseda.split(":")

            if self.ukazi[-1]=="levo":
                #print("obracam levo")
                self.desno_nazaj()
            elif self.ukazi[-1]=="desno":
                #print("obracam desno")
                self.levo_nazaj()

            elif "naprej" in razcleni[0]:

                self.nazaj()

    def zbrisi_zadnjega(self):
        return self.ukazi[:-1]

    def printaj(self):
        return self.ukazi
    def printaj2(self):
        return self.smer



