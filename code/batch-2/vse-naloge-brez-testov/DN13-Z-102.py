class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.obrnjen = 1 #desno

    def naprej(self,d):
        if self.obrnjen == 0: #navzgor
            self.y = self.y + d

        elif self.obrnjen == 1: #desno
            self.x = self.x + d

        elif self.obrnjen == 2: #navzdol
            self.y = self.y - d

        elif self.obrnjen == 3: #levo
            self.x = self.x - d

    def levo(self):
        self.obrnjen = (self.obrnjen + 3) % 4

    def desno(self):
        self.obrnjen = (self.obrnjen + 1) % 4

    def koordinate(self):
        return (self.x,self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

