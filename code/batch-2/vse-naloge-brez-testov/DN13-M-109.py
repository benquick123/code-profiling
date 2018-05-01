class Minobot(object):
    def __init__(self):
        self.smer = "N"
        self.x = 0
        self.y = 0
        self.povrni = []
    def razveljavi(self):
        if len(self.povrni) > 0:
            self.x, self.y, self.smer = self.povrni.pop()
        else:
            return

    def koordinate(self):
        return (self.y,self.x)

    def razdalja(self):
        return abs(self.x)+abs(self.y)

#Koda za premik smeri je bila kopirana iz naloge minibot! lahko preverite nalogo, ki sem jo takrat oddal.
    def naprej(self,koraki):
        self.povrni.append((self.x, self.y, self.smer))
        if self.smer == "N":
            self.y += koraki
        elif self.smer == "S":
            self.y -= koraki
        elif self.smer == "E":
            self.x -= koraki
        elif self.smer == "W":
            self.x += koraki


    def desno(self):
        self.povrni.append((self.x, self.y, self.smer))
        polozaj = self.smer
        smeri = "NESW"
        ismer = smeri.index(polozaj)
        polozaj = smeri[(ismer + 1) % 4]
        self.smer = polozaj

    def levo(self):
        self.povrni.append((self.x, self.y, self.smer))
        polozaj = self.smer
        smeri = "NESW"
        ismer = smeri.index(polozaj)
        polozaj = smeri[(ismer - 1) % 4]
        self.smer = polozaj

