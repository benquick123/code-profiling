class Minobot:
    def __init__(self):
        self.x,self.y=0,0
        self.smer="E"

    def premik(self,ukaz):
        smeri = "NESW"
        premiki = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ismer = smeri.index(self.smer)
        if ukaz == "R":
            self.smer = smeri[(ismer + 1) % 4]
        elif ukaz == "L":
            self.smer = smeri[(ismer - 1) % 4]
        else:
            dx, dy = premiki[ismer]
            self.x += dx * ukaz
            self.y += dy * ukaz

    def naprej(self,d):
        self.premik(d)
    def desno(self):
        self.premik("R")
    def levo(self):
        self.premik("L")
    def koordinate(self):
        return self.x,self.y
    def razdalja(self):
        return abs(self.x)+abs(self.y)



