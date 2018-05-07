class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = 2
        self.sez = []

    def naprej(self,d):
        self.d = d
        if self.smer == 1: #navzgor
            self.y += d
        if self.smer == 3: #navdol
            self.y -= d
        if self.smer == 2: #desno
            self.x += d
        if self.smer == 4: #levo
            self.x -= d
        self.sez.append(((self.x, self.y),self.smer))
        return (self.x,self.y)

    def desno(self):
        if self.smer == 4:
            self.smer = 1
        else:
            self.smer += 1
        self.sez.append(((self.x, self.y), self.smer))

    def levo(self):
        if self.smer == 1:
            self.smer = 4
        else:
            self.smer -= 1
        self.sez.append(((self.x, self.y), self.smer))

    def koordinate(self):
        return (self.x,self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if len(self.sez) == 1:
            self.smer = 2
            self.x = 0
            self.y = 0
        else:
            self.sez.pop(-1)
            koordinate = self.sez[-1]
            x_y = koordinate[0]
            for deli in x_y:
                self.x = x_y[0]
                self.y = x_y[1]
            self.smer = koordinate[1]


