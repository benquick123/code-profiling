class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = "E"
        self.pot = []

    def koordinate(self):
        return (self.x, self.y)

    def naprej(self, d):
        if (self.smer == "N"):
            self.y += d
        elif (self.smer == "E"):
            self.x += d
        elif (self.smer == "S"):
            self.y -= d
        elif (self.smer == "W"):
            self.x -= d

        self.pot.append(d)

    def nazaj(self, d):
        if (self.smer == "N"):
            self.y -= d
        elif (self.smer == "E"):
            self.x -= d
        elif (self.smer == "S"):
            self.y += d
        elif (self.smer == "W"):
            self.x += d

    def levo(self):
        if (self.smer == "N"):
            self.smer = "W"
        elif (self.smer == "E"):
            self.smer = "N"
        elif (self.smer == "S"):
            self.smer = "E"
        elif (self.smer == "W"):
            self.smer = "S"

        self.pot.append("levo")

    def desno(self):
        if (self.smer == "N"):
            self.smer = "E"
        elif (self.smer == "E"):
            self.smer = "S"
        elif (self.smer == "S"):
            self.smer = "W"
        elif (self.smer == "W"):
            self.smer = "N"

        self.pot.append("desno")

    def desno_brez(self):
        if (self.smer == "N"):
            self.smer = "E"
        elif (self.smer == "E"):
            self.smer = "S"
        elif (self.smer == "S"):
            self.smer = "W"
        elif (self.smer == "W"):
            self.smer = "N"

    def levo_brez(self):
        if (self.smer == "N"):
            self.smer = "W"
        elif (self.smer == "E"):
            self.smer = "N"
        elif (self.smer == "S"):
            self.smer = "E"
        elif (self.smer == "W"):
            self.smer = "S"

    def razdalja(self):
        return (abs(self.x)+abs(self.y))

    def razveljavi(self):
        if (len(self.pot) == 0):
            return None
        if (self.pot[len(self.pot)-1] == "levo"):
            self.desno_brez()
            self.pot = self.pot[:-1]
        elif (self.pot[len(self.pot)-1] == "desno"):
            self.levo_brez()
            self.pot = self.pot[:-1]
        else:
            self.nazaj(int(self.pot[len(self.pot)-1]))
            self.pot = self.pot[:-1]


