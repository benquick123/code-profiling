class Minobot:
    def __init__(self):
        kompas = ["N", "E", "S", "W"]
        self.x, self.y = 0, 0
        self.sprememba_pozicije = 1
        self.trenutna_pozicija = kompas[self.sprememba_pozicije]
        self.izvrseno = []
    def koordinate(self):
        kx, ky = self.x, self.y
        #print(self.trenutna_pozicija)
        #print("koordinate:",(kx,ky))
        #print("izvrseno:", self.izvrseno)
        return (kx,ky)

    def naprej(self, d):
        if self.trenutna_pozicija == "N":
            self.y+= d
        if self.trenutna_pozicija == "E":
            self.x+= d
        if self.trenutna_pozicija == "S":
            self.y-= d
        if self.trenutna_pozicija == "W":
            self.x-= d
        #print("naprej", d)
        self.izvrseno.append(d)
        #print("izvrseno:", self.izvrseno)
        return (self.x,self.y)

    def desno(self):
        kompas = ["N", "E", "S", "W"]
        self.sprememba_pozicije+= 1
        if self.sprememba_pozicije == 4:
            self.sprememba_pozicije = 0
        self.trenutna_pozicija = kompas[self.sprememba_pozicije]
        self.izvrseno.append("desno")
        #print("desno:", self.sprememba_pozicije)
        #print("izvrseno:", self.izvrseno)

    def levo(self):
        kompas = ["N", "E", "S", "W"]
        self.sprememba_pozicije-= 1
        if self.sprememba_pozicije == -4:
            self.sprememba_pozicije = 0
        self.trenutna_pozicija = kompas[self.sprememba_pozicije]
        self.izvrseno.append("levo")
        #print("levo:", self.sprememba_pozicije)
        #print("izvrseno:", self.izvrseno)

    def razdalja(self):
        manhattanska = abs(self.x) + abs(self.y)
        return manhattanska

    def razveljavi(self):
        if self.trenutna_pozicija == "E":
            self.x-= self.izvrseno[-1]
            self.izvrseno.pop(-1)
            #print(self.izvrseno)
        if self.trenutna_pozicija == "S":
            self.y-= self.izvrseno[-1]
            self.izvrseno.pop(-1)
            #print(self.izvrseno)
        if self.izvrseno[-1] == "levo" and self.trenutna_pozicija == "E":
            self.trenutna_pozicija = "S"
            self.izvrseno.pop(-1)
            #print(self.izvrseno)


