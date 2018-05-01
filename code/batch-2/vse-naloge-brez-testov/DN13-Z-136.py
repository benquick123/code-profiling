class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = "desno"

    def naprej(self, d):
        if self.smer == "desno":
            self.x += d
        elif self.smer == "levo":
            self.x -= d
        elif self.smer == "gor":
            self.y += d
        elif self.smer == "dol":
            self.y -= d

    def desno(self):
        if self.smer == "gor":
            self.smer = "desno"
        elif self.smer == "desno":
            self.smer = "dol"
        elif self.smer == "dol":
            self.smer = "levo"
        elif self.smer == "levo":
            self.smer = "gor"

    def levo(self):
        if self.smer == "gor":
            self.smer = "levo"
        elif self.smer == "levo":
            self.smer = "dol"
        elif self.smer == "dol":
            self.smer = "desno"
        elif self.smer == "desno":
            self.smer = "gor"

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return  abs(self.x) + abs(self.y)

