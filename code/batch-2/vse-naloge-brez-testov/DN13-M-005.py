class Minobot:
    def __init__(self):
        self.pot = []
        self.x, self.y = 0, 0
        self.smer = 1

    def update(self):
        self.pot.append((self.x, self.y, self.smer))

    def naprej(self, d):
        if self.smer == 0:
            self.y += d
        elif self.smer == 1:
            self.x += d
        elif self.smer == 2:
            self.y -= d
        else:
            self.x -= d
        self.update()

    def desno(self):
        if self.smer != 3:
            self.smer += 1
        else:
            self.smer = 0
        self.update()

    def levo(self):
        if self.smer != 0:
            self.smer -= 1
        else:
            self.smer = 3
        self.update()

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if self.pot:
            del self.pot[-1]
        if self.pot:
            self.x, self.y, self.smer = self.pot[-1]
        else:
            self.x, self.y, self.smer = 0, 0, 1


