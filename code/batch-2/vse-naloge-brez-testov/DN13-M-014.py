class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 90

    def naprej(self, d):
        if self.angle % 4 == 2:
            if 270 > self.angle > 0 or self.angle <= -270:
                nx = self.x + d
                self.x = nx
            else:
                nx = self.x - d
                self.x = nx
        if self.angle % 4 == 0:
            if self.angle > 0 or self.angle <= -180:
                ny = self.y + d
                self.y = ny
            else:
                ny = self.y - d
                self.y = ny

    def desno(self):
        desno = self.angle - 90
        self.angle = desno

    def levo(self):
        levo = self.angle + 90
        self.angle = levo

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        xr = self.x
        yr = self.y
        return abs(xr) + abs(yr)

