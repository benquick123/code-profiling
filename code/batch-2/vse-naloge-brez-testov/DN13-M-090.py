#OBVEZNI DEL

class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = 0 #začne obrnjen v desno
        self.stanja = [(0, 0, 0)] #začetno stanje

    def naprej(self, d): #premik za d
        if self.smer == 0: #premik v desno
            self.x += d
        if self.smer == 1: #premik gor
            self.y += d
        if self.smer == 2: #premik v levo
            self.x -= d
        if self.smer == 3: #premik dol
            self.y -= d
        self.stanja.append((self.x, self.y, self.smer))

    def desno(self): #obrat v desno
        self.smer = (self.smer-1) % 4
        self.stanja.append((self.x, self.y, self.smer))

    def levo(self): #obrat v levo
        self.smer = (self.smer+1) % 4
        self.stanja.append((self.x, self.y, self.smer))

    def koordinate(self): #vrne trenutne koordinate
        return (self.x, self.y)

    def razdalja(self): #vrne pravokotno razdaljo do (0,0)
        return abs(self.x) + abs(self.y)


    #DODATNI DEL

    def razveljavi(self): #razveljavi zadnji ukaz
        if len(self.stanja) >= 2: #če je že prejel ukaz
            del self.stanja[-1] #izbriše zadnji premik
            self.x, self.y, self.smer = self.stanja[-1] #ponastavi koordinate in smer


################################################
#Testi (ne spreminjaj)

