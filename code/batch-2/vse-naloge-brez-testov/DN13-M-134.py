
class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = "R"

    def naprej(self, d):
        if self.smer == "R":
            self.x += d
        elif self.smer == "L":
            self.x -= d
        elif self.smer == "U":
            self.y += d
        else:
            self.y -= d

    def desno(self):
        if self.smer == "R":
            self.smer = "D"
        elif self.smer == "U":
            self.smer = "R"
        elif self.smer == "L":
            self.smer = "U"
        else:
            self.smer = "L"

    def levo(self):
        if self.smer == "R":
            self.smer = "U"
        elif self.smer == "U":
            self.smer = "L"
        elif self.smer == "L":
            self.smer = "D"
        else:
            self.smer = "R"

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        razd = abs(self.x) + abs(self.y)
        return razd

