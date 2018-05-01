class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = 1
        self.ukazi = []
        self.rev = False

    def naprej(self, d):
        if self.smer == 0:
            self.y += d
        elif self.smer == 1:
            self.x += d
        elif self.smer == 2:
            self.y -= d
        elif self.smer == 3:
            self.x -= d
        if not self.rev:
            self.ukazi.append(int(d))
        self.rev = False

    def desno(self):
        if self.smer == 0:
            self.smer = 1
        elif self.smer == 1:
            self.smer = 2
        elif self.smer == 2:
            self.smer = 3
        elif self.smer == 3:
            self.smer = 0
        if not self.rev:
            self.ukazi.append("desno")
        self.rev = False

    def levo(self):
        if self.smer == 0:
            self.smer = 3
        elif self.smer == 1:
            self.smer = 0
        elif self.smer == 2:
            self.smer = 1
        elif self.smer == 3:
            self.smer = 2
        if not self.rev:
            self.ukazi.append("levo")
        self.rev = False

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        self.rev = True
        if self.ukazi:
            if self.ukazi[-1] == "desno":
                self.levo()
                self.ukazi = self.ukazi[:-1]
            elif self.ukazi[-1] == "levo":
                self.desno()
                self.ukazi = self.ukazi[:-1]
            else:
                self.naprej(-1 * (int(self.ukazi[-1])))
                self.ukazi = self.ukazi[:-1]
        else:
            self.x=0
            self.y=0


