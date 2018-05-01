class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0

    def naprej(self, d):
        if self.angle == 0 or self.angle == -360 or self.angle == 360:
            self.x += d
        if self.angle == 90 or self.angle == -270:
            self.y += d
        if self.angle == -90 or self.angle == 270:
            self.y -= d
        if self.angle == 180 or self.angle == -180:
            self.x -= d

    def desno(self):
        self.angle -= 90

    def levo(self):
        self.angle += 90

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)

