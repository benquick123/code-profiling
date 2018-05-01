class Minobot:
    def __init__(self):
        self.x, self.y = 0, 0
        self.smer = 90
        self.s = []

    def naprej(self, d):
        if self.smer%360 == 90:
            self.x += d
        if self.smer%360 == 180:
            self.y -= d
        if self.smer%360 == 270:
            self.x -= d
        if self.smer%360 == 0:
            self.y += d
        self.s.append(d)

    def desno(self):
        self.smer += 90
        self.s.append("desno")

    def levo(self):
        self.smer -= 90
        self.s.append("levo")

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if len(self.s) >= 1:
            if self.s[-1] == "levo":
                self.desno()
            elif self.s[-1] == "desno":
                self.levo()
            else:
                self.naprej(-self.s[-1])
            del self.s[-1]
            del self.s[-1]











#=========================================== TESTI ============================================

