import itertools

class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = "desno"

    def naprej(self, premik):
        if (self.smer == "desno"):
            self.x += premik

        elif (self.smer == "levo"):
            self.x -= premik

        elif (self.smer == "gor"):
            self.y += premik

        elif (self.smer == "dol"):
            self.y -= premik

    def koordinate(self):
        return self.x, self.y

    def desno(self):
        if (self.smer == "desno"):
            self.smer = "dol"

        elif (self.smer == "dol"):
            self.smer = "levo"

        elif (self.smer == "levo"):
            self.smer = "gor"

        elif (self.smer == "gor"):
            self.smer = "desno"

    def levo(self):
        if (self.smer == "desno"):
            self.smer = "gor"

        elif (self.smer == "gor"):
            self.smer = "levo"

        elif (self.smer == "levo"):
            self.smer = "dol"

        elif (self.smer == "dol"):
            self.smer = "desno"

    def razdalja(self):
        return abs(self.x) + abs(self.y)

a = Minobot()
a.levo()
a.naprej(4)
a.desno()
a.naprej(3)
#print(a.koordinate())



