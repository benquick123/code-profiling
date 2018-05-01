class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = 90


    def naprej(self, d):
        if self.smer == 90:
            nx = self.x + d
            self.x = nx
        if self.smer == 180:
            ny = self.y - d
            self.y = ny
        if self.smer == 270:
            nx = self.x - d
            self.x = nx
        if self.smer == 0:
            ny = self.y + d
            self.y = ny

    def desno(self):
        self.smer += 90
        if self.smer > 270:
            self.smer = 0

    def levo(self):
        self.smer -= 90
        if self.smer < 0:
            self.smer = 270

    def koordinate(self):
       return self.x,self.y

    def razdalja(self):
        x1 = abs(self.x - 0)
        y1 = abs(self.y - 0)
        return x1 + y1

a = Minobot()
a.naprej(1)
print(a.koordinate())
a.naprej(2)
print(a.koordinate())


