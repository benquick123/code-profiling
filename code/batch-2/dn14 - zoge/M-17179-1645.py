class Vector:
    def __init__(self, *v):
        self.values = list(v)

    def __str__(self):
        return "<" + ", ".join(map(str, self.values)) + ">"

    def __repr__(self):
        return "Vector({})".format(", ".join(map(str, self.values)))

    def __len__(self):
        return len(self.values)

    def __abs__(self):
        from math import sqrt
        return sqrt(sum(x ** 2 for x in self.values))

    def __add__(self, other):
        return Vector(*[x + y for x, y in zip(self.values, other.values)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum(x * y for x, y in zip(self.values, other.values))
        else:
            return Vector(*[x * other for x in self.values])

    __rmul__ = __mul__

    def __neg__(self):
        return -1 * self

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return -self + other

    def __truediv__(self, other):
        return self * (1 / other)

    def __getitem__(self, index):
        return self.values[index]

    def __setitem__(self, index, value):
        self.values[index] = value


import risar, math, time, sys
from random import randrange


def wait(t):
    #funkcija ki caka t sekund
    risar.obnovi()
    time.sleep(t)



class Circle():
    def __init__(self):
        #krog na zacetku postavimo na nakljucne koordinate in mu dolocimo nakljucno barvo, in nakljucni premik
        self.sirina = 10
        self.x, self.y = risar.nakljucne_koordinate()
        self.color = risar.nakljucna_barva()
        self.spremembaX = randrange(-5, 5, 1)
        #naključno spreminjaje y smeri gledamo ali je število liho ali sodo in glede na to določimo smer y, s tem da gledamo to naj bi povečali naključnost
        if randrange(0, 100) % 2:
            self.spremembaY = -1
        else:
            self.spremembaY = 1


    def show(self):
        #izrise krog na zaslon
        self.izrisan_krog = risar.krog(self.x, self.y, self.sirina, self.color, 2) #self.izrisan_krog.setPos(newX, newY)


    def premakni(self):
        #funkcija premakne in vodi samo en krog
        self.x = self.x + self.spremembaX
        self.y = self.y + math.sqrt(5**2 - self.spremembaX**2) * self.spremembaY
        self.izrisan_krog.setPos(self.x, self.y)
        risar.obnovi()
        if (self.x-self.sirina) < 0 or (self.x+self.sirina) > risar.maxX or (self.y-self.sirina) < 0 or (self.y+self.sirina) > risar.maxY:
            self.bounce()


    def pokazi_kroge(self, seznam_krogov: list):
        #izrise vse kroge na zacetku na zaslon
        for krog in seznam_krogov:
            krog.show()


    def premakni_kroge(self, seznam_krogov: list):
        #kot vhod dobi seznam "objektov" katere izrise na zaslon in jih premika
        for krog in seznam_krogov:
            if self.hit_test(krog) == True:
                if self.hit_ball(krog) == True:
                    #za oceno 8 do konca izreise krog pocaka 2s in zakljuci program
                    wait(1)
                    exit("Zadeli ste zogo!")
            else:
                krog.x = krog.x + krog.spremembaX #racunanje za koliko se bo premaknila zoga po x-u (max 5)
                krog.y = krog.y + math.sqrt(5 ** 2 - krog.spremembaX ** 2) * krog.spremembaY #racunanje premika y po pitagori
                krog.izrisan_krog.setPos(krog.x, krog.y) #postavimo krog na novo pozicijo
                if (krog.x - krog.sirina) < 0 or (krog.x + krog.sirina) > risar.maxX or (krog.y - krog.sirina) < 0 or (krog.y + krog.sirina) > risar.maxY:
                    krog.bounce()


    def hit_test(self,krog):
        #spremenljivke za klik se ostvarijo šele ko pritisnemo miško
        try:
            global klikX, klikY, mouse_sirina
            vector_a = Vector(klikX, klikY) #krajevni vektor miške ko kliknemo
            vector_b = Vector(krog.x, krog.y) #krajevni vekor zoge ki se premika
            vector_c = vector_a - vector_b #vektor med vektorjem a in b
            razdalja_ab = math.sqrt(vector_c * vector_c)  #razdlaje vektorja ab
            skupna_sirina = self.sirina + mouse_sirina #če je razdalja vektorja manša od sirine obeh krogov skipaj pomeni, da sta se zaletela
            if razdalja_ab < skupna_sirina:
                return True
        except:
            return False


    def hit_ball(self, krog):
        #izris zadete zoge, zoga se poveca in obarva
        krog.izrisan_krog.setRect(-30, -30, 60, 60)
        c = krog.izrisan_krog.pen().color().lighter()
        c.setAlpha(192)
        krog.izrisan_krog.setBrush(c)
        return True


    def bounce(self):
        #funkcija gleda ali se je zoga/krog zaletela v katero koli od sten in jo poslje v obratni smeri zato spremenimo predznak spremembe
        if self.x < self.sirina:
            self.spremembaX = self.spremembaX * (-1)
            self.x = self.sirina
        elif self.x > risar.maxX -  self.sirina:
            self.spremembaX = self.spremembaX * (-1)
            self.x = risar.maxX - self.sirina
        elif self.y < self.sirina:
            self.spremembaY = self.spremembaY * (-1)
            self.y = self.sirina
        else:
            self.spremembaY = self.spremembaY * (-1)
            self.y = risar.maxY - self.sirina


class Mouse():
    #objekt ki je namenjen sledenju in interakciji z misko
    def __init__(self):
        #dolocimo lastnosti kroga, ki bo sledil miski
        self.sirina = 30
        self.krog_miska = risar.krog(risar.maxX / 2, risar.maxY / 2, self.sirina)
        self.klik_done = False
        self.miskaX, self.miskaY = risar.miska


    def premik_miske(self):
        #funkcija gleda ali smo pritisnili na misko ce nismo premaknimo krog, ki sledi miski
        if risar.klik == False:
            self.miskaX, self.miskaY = risar.miska
            self.krog_miska.setPos(self.miskaX, self.miskaY)
        elif self.klik_done == False: #kliknemo lahko samo enkrat, ko kliknemo nehamo slediti miski
            self.on_click()


    def on_click(self):
        #v globalne spremenljivke si zapomnimo koordinate klika in sirino kroga (ni lepo ampak drugace nisem znal)
        global klikX, klikY, mouse_sirina
        klikX, klikY, mouse_sirina = self.miskaX, self.miskaY, self.sirina
        #zapolnimo krog in ga ne premikamo vec
        self.krog_miska_click = risar.krog(self.miskaX, self.miskaY, 30, risar.nakljucna_barva())
        c = self.krog_miska_click.pen().color().lighter()
        c.setAlpha(192)
        self.krog_miska_click.setBrush(c)
        self.klik_done = True


"""
#za oceno 6
krog = Circle()
mis = Mouse()
krog.show()

while time.perf_counter < 20:
    krog.premakni()
    mis.premik_miske()
    wait(0.02)
"""

begin = time.perf_counter()#stevec, ki steje od zacetka programa, tako da lahko casovno nastavimo delovanje programa
krogi = []
stevilo_krogov = 30 #izberemo stevilo krogov, ki jih bomo izrisali na zaslon


#naredimo list objektov Circle
for x in range(stevilo_krogov):
     krog = Circle()
     krogi.append(krog)


Circle.pokazi_kroge(Circle(), krogi) #najprej vse zoge/kroge izrisemo na zaslon
mis = Mouse() #kreiramo objekt Mouse()


while True: #zanka dela dokler je cas manjsi od podanega
    Circle().premakni_kroge(krogi) #premaknemo vse kroge
    mis.premik_miske() #premaknemo misko
    wait(0.02) #pocakamo 0.02 sekunde
   




