

class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = "E"


    def naprej(self, d):
        if self.smer == "E":
            self.x += d
        if self.smer == "W":
            self.x -= d
        if self.smer == "N":
            self.y += d
        if self.smer == "S":
            self.y -= d

    def desno(self):
        slovar = "NESW"
        self.smer = slovar[(slovar.index(self.smer) + 1) % 4]

    def levo(self):
        slovar = "NESW"
        self.smer = slovar[(slovar.index(self.smer) - 1) % 4]

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)



