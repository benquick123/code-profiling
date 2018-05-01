class Minobot(object):
    def __init__(self):
        self.x, self.y = 0, 0
        self.dir = 0

    def koordinate(self):
        return self.x, self.y

    def levo(self):
        self.dir += 90
        self.dir %= 360

    def desno(self):
        self.dir -= 90
        self.dir %= 360

    def naprej(self, d):
        if self.dir == 0:
            self.x += d
        elif self.dir == 90:
            self.y += d
        elif self.dir == 180:
            self.x -= d
        elif self.dir == 270:
            self.y -= d

    def razdalja(self):
        return abs(self.x) + abs(self.y)




