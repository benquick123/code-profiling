
class Minobot:

    def __init__(self):
        self.x, self.y = 0, 0
        self.smer = "E"


    def naprej(self, d):
        if self.smer == "N":
            self.y += d
        if self.smer == "E":
            self.x += d
        if self.smer == "S":
            self.y -= d
        if self.smer == "W":
            self.x -= d



    def desno(self):
        smeri = "NESW"
        if self.smer == "W":
            self.smer = "N"
        else:
            self.smer = smeri[smeri.index(self.smer) + 1]



    def levo(self):
        smeri = "NESW"
        if self.smer == "N":
            self.smer = "W"
        else:
            self.smer = smeri[smeri.index(self.smer) - 1]



    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)




