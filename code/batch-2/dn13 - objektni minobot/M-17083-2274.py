class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = "E"

    def naprej(self, d):
        if self.smer == "E":
            self.x += d
        elif self.smer == "S":
            self.y -= d
        elif self.smer == "W":
            self.x -= d
        elif self.smer == "N":
            self.y += d

    def desno(self):
        if self.smer == "E":
            self.smer = "S"
        elif self.smer == "S":
            self.smer = "W"
        elif self.smer == "W":
            self.smer = "N"
        elif self.smer == "N":
            self.smer = "E"

    def levo(self):
        if self.smer == "E":
            self.smer = "N"
        elif self.smer == "S":
            self.smer = "E"
        elif self.smer == "W":
            self.smer = "S"
        elif self.smer == "N":
            self.smer = "W"

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)