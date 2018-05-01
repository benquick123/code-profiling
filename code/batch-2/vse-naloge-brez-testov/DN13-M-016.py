from collections import deque
#inicializacija classa


class Minobot:
    #inicializacija osnovnih vrednosti
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rotation = "E"
        self.history = []

    def naprej(self, d):
        #za vsak mozen otation
        if self.rotation == "E":
            self.x = self.x + d
        elif self.rotation == "S":
            self.y = self.y - d
        elif self.rotation == "W":
            self.x = self.x - d
        elif self.rotation == "N":
            self.y = self.y + d

        #doda element v history
        self.history = self.history + [("N", d)]


    def desno(self):

        #list smeri ki ga kasneje rotejta
        smeri = ["N", "E", "S", "W"]

        #dobi indeks smeri ki jo ima zdaj
        index_s = smeri.index(self.rotation)

        #obrne list smeri tako da se zamaknejo za eno v levo
        nove_smeri = [smeri[1], smeri[2], smeri[3], smeri[0]]

        #spremeni trenuten rotation za enega bolj desno
        self.rotation = nove_smeri[index_s]

        # doda element v history
        self.history = self.history + ["R"]


    def levo(self):
        #isti k kot pri desno() samo da rotejta v drugo smer
        smeri = ["N", "E", "S", "W"]
        index_s = smeri.index(self.rotation)
        nove_smeri = [smeri[3], smeri[0], smeri[1], smeri[2]]
        self.rotation = nove_smeri[index_s]
        # doda element v history
        self.history = self.history + ["L"]

    #pomožna funkcija za razveljavi()
    def nazaj(self, d):
        if self.rotation == "E":
            self.x = self.x - d
        elif self.rotation == "S":
            self.y = self.y + d
        elif self.rotation == "W":
            self.x = self.x + d
        elif self.rotation == "N":
            self.y = self.y - d
        self.history = self.history + [("N", d)]

    #ez
    def koordinate(self):
        return self.x, self.y

    #ez
    def razdalja(self):
        return abs(self.x) + abs(self.y)

    #pomožna funkcija za izpisovanje zgodovine
    def ret(self):
        return self.history

    def razveljavi(self):
        #če je kak element v historiju
        if self.history:
            step = self.history.pop()


            if step == "R":
                self.levo()
            elif step == "L":
                self.desno()
            else:
                self.nazaj(step[1])

            #zbrisi zadnjega
            self.history = self.history[:-1]



m = Minobot()
m.desno()
m.naprej(10)
m.levo()

print(m.ret())


