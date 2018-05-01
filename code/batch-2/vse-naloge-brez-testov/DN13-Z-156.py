class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = (1, 0)
        self.stanja =[(self.x, self.y, self.smer)]

    def naprej(self, d):
        a, b = self.smer
        self.x = self.x + a * d
        self.y = self.y + b * d
        self.stanja.append((self.x, self.y, self.smer))

    def desno(self):
        if self.smer == (1, 0):
            self.smer = (0, -1)
        elif self.smer == (0, -1):
            self.smer = (-1, 0)
        elif self.smer == (-1, 0):
            self.smer = (0, 1)
        else:
            self.smer = (1, 0)
        self.stanja.append((self.x, self.y, self.smer))


    def levo(self):
        if self.smer == (1, 0):
            self.smer = (0, 1)
        elif self.smer == (0, 1):
            self.smer = (-1, 0)
        elif self.smer == (-1, 0):
            self.smer = (0, -1)
        else:
            self.smer = (1, 0)
        self.stanja.append((self.x, self.y, self.smer))

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if len(self.stanja) > 1:
            self.stanja.pop()
        self.x, self.y, self.smer = self.stanja[-1]

