class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = 90
        self.log = [(self.x, self.y, self.smer)]

    def naprej(self, d):
        if self.smer == 0:
            self.y += d

        elif self.smer == 90:
            self.x += d

        elif self.smer == 180:
            self.y -= d

        elif self.smer == 270:
            self.x -= d

        self.log.append((self.x, self.y, self.smer))

    def desno(self):
        self.smer = (self.smer + 90) % 360
        self.log.append((self.x, self.y, self.smer))

    def levo(self):
        self.smer = (self.smer - 90) % 360
        self.log.append((self.x, self.y, self.smer))

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

#-------------------------------------------------------------------------------------------
