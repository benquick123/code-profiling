import risar, math, random
from PyQt5.QtWidgets import QMessageBox



'''
Za oceno 6: Sestavi program, ki nariše eno kroglico naključne barve, ki se pojavi na naključnem mestu in giba v 
naključni smeri (glej detajle spodaj!). Ko pride do roba, se odbije, tako kot ste se učili pri Fiziki. Odbija naj 
se približno dvajset sekund, nato se program konča.

Za oceno 7: Enako kot za oceno 6, vendar mora program risati in voditi 30 žog različnih naključnih barv, ki se gibajo
 v različnih naključnih smereh.

Za oceno 8: Poleg tega, kar ste naredili za oceno 7, naj bo na sliki še krog, katerega središče je tam, kjer je trenutno
 miška (in se seveda premika z miško). Ko uporabnik klikne, naj krog obstane, kjer je in ne sledi več miški. Program naj
  se konča, ko prva izmed žogic zadane žogo, ki smo jo postavili z miško.

Za oceno 9: Sprogramirajte eno stopnjo igre. Igra teče, dokler je kaj eksplodiranih krogel, ko izgine zadnja, pa se
 izpiše, koliko žog je eksplodiralo. S tem se program konča.

Za oceno 10: Sprogramirajte igro z 10 stopnjami. Na začetku vsake stopnje se napiše, koliko žog je v igri in koliko jih
 je eksplodiralo. Na koncu, ko izgine zadnja eksplodirana krogla, se igra nadaljuje na naslednji stopnji, če je eksplodiralo
  dovolj žog. Sicer pa se pojavi okno, v katerem piše, koliko žog je eksplodiralo in da je to premalo; igra se ponovi na 
  isti stopnji. Izmislite smiselna števila žog. Stopnje se morajo seveda razlikovati.

Detajli:

Polmer kroglic naj bo 10 točk.
Polmer kroglice, ki predstavlja miš, in polmer eksplodirane kroglice naj bo 30 točk.
Eksplodirana kroglica naj izgine po štirih sekundah.
Vse kroglice naj se premikajo z enako hitrostjo, namreč 5 točk na eno iteracijo zanke; v zanko dodajte 0.02 sekunde pavze.
 (Namig: za x-komponento hitrosti določite naključno število med -5 in 5. Komponento y izračunate po Pitagori.)
V modulu risar imate dve doslej zamolčani spremenljivki, povezani z miško:

risar.miska je terka, ki vsebuje koordinati miške, če se le-ta nahaja znotraj risarjevega okna (sicer pa koordinato, kjer je to okno zapustila).

risar.klik je spremenljivka, ki postane True, ko uporabnik klikne miško. Če jo postavite nazaj na False, jo bo risar ob naslednjem kliku spet postavil na True.

Če je krog nek krog, ga pobarvate z

c = krog.pen().color().lighter()
c.setAlpha(192)
krog.setBrush(c)
Če želite spremeniti polmer kroga krog na, recimo, 30, pokličete krog.setRect(-30, -30, 60, 60). Če ga želite skriti, pokličite krog.hide().

Za prikazovanje sporočil uporabite QMessageBox.information(None, "ime okna", "sporocilo"). Za to boste morali uvoziti from PyQt5.QtWidgets import QMessageBox.

Testov tokrat ni.

'''


class Zoga():
    def __init__(self):
        self.x, self.y = risar.nakljucne_koordinate()
        self.r = 10
        self.kroglica = risar.krog(self.x, self.y, self.r, risar.nakljucna_barva())
        self.vx = random.randint(-5, 5)
        self.vy = math.sqrt(25 - self.vx**2)
        self.cas_pop = 0



    def akcija(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.kroglica.setPos(self.x, self.y)

        if risar.maxX < self.x:
            self.vx = -self.vx
        else:
            if self.x < 0:
                self.vx = -self.vx

        if risar.maxY < self.y:
            self.vy = -self.vy
        else:
            if self.y < 0:
                self.vy = -self.vy

    def osvezi(self):
        if not self.cas_pop:
            self.akcija()
        else:
            if self.cas_pop == 100:
                self.kroglica.hide()
            self.cas_pop = self.cas_pop +1


    def eksplozija(self):
        if not self.cas_pop:
            self.vx = 0
            self.vy = 0
            self.r = 30
            self.cas_pop = 1
            krog = self.kroglica.pen().color().lighter()
            krog.setAlpha(192)
            self.kroglica.setBrush(krog)
            self.kroglica.setRect(-30, -30, 60, 60)


class Miska():
    def __init__(self):
        self.x, self.y = risar.miska
        self.r = 30
        self.cas_pop = 0
        self.kroglica = risar.krog(self.x, self.y, self.r, risar.bela)

    def osvezi(self):
        if risar.klik:
            self.eksplozija()

        if not self.cas_pop:
            self.akcija()
        else:
            self.cas_pop = self.cas_pop + 1
            if self.cas_pop == 100:
                self.kroglica.hide()


    def akcija(self):
        self.x, self.y = risar.miska
        self.kroglica.setPos(self.x, self.y)

    def eksplozija(self):
        if not self.cas_pop:
            self.cas_pop = 1


class Igra:
    def __init__(self, st_zog, cilj):
        self.zoge=[Zoga() for i in range(st_zog)]
        self.miska = Miska()
        self.zoge.append(self.miska)
        self.cilj = cilj
        self.eksplodirane = 0
        self.konec = False


    def trk(self, z):

        if z.cas_pop == 0:
            for z1 in self.zoge:

                if 0 < z1.cas_pop <= 100 and z1 != z:
                    x = z1.x - z.x
                    y = z1.y - z.y
                    r = z1.r + z.r

                    if pow(x, 2) + pow(y, 2) <= pow(r, 2):
                        if z.cas_pop == 0:
                            z.eksplozija()
                            self.eksplodirane = self.eksplodirane +1


    def osvezi(self):
        eksplodirane = 0

        for zoga in self.zoge:
            zoga.osvezi()
            self.trk(zoga)

            if 100 >= zoga.cas_pop > 0:
                eksplodirane = eksplodirane + 1

        if not eksplodirane and risar.klik:
            self.konec = True


    def igraj(self):
        zmaga = False

        if self.cilj == 1:
            QMessageBox.information(None, "Igra", "Razstreliti moras 1 zogo.")
        elif self.cilj == 2:
            QMessageBox.information(None, "Igra", "Razstreliti moras 2 zogi.")
        elif self.cilj == 3:
            QMessageBox.information(None, "Igra", "Razstreliti moras {} zoge.".format(self.cilj))
        elif self.cilj == 4:
            QMessageBox.information(None, "Igra", "Razstreliti moras {} zoge.".format(self.cilj))
        else:
            QMessageBox.information(None, "Igra", "Razstreliti moras {} zog.".format(self.cilj))

        while not self.konec:
            self.osvezi()
            risar.cakaj(0.02)

        if self.eksplodirane < self.cilj:
            QMessageBox.information(None, "Fail", "Razstrelil si premalo zog! ({}) Poskusi znova.".format(self.eksplodirane))
        else:
            zmaga = True

        for z in self.zoge:
            z.kroglica.hide()

        self.zoge=[]
        risar.klik = False

        return zmaga



'''
Za oceno 6: Sestavi program, ki nariše eno kroglico naključne barve, ki se pojavi na naključnem mestu in giba v 
naključni smeri (glej detajle spodaj!). Ko pride do roba, se odbije, tako kot ste se učili pri Fiziki. Odbija naj 
se približno dvajset sekund, nato se program konča.

Za oceno 7: Enako kot za oceno 6, vendar mora program risati in voditi 30 žog različnih naključnih barv, ki se gibajo
 v različnih naključnih smereh.

Za oceno 8: Poleg tega, kar ste naredili za oceno 7, naj bo na sliki še krog, katerega središče je tam, kjer je trenutno
 miška (in se seveda premika z miško). Ko uporabnik klikne, naj krog obstane, kjer je in ne sledi več miški. Program naj
  se konča, ko prva izmed žogic zadane žogo, ki smo jo postavili z miško.

Za oceno 9: Sprogramirajte eno stopnjo igre. Igra teče, dokler je kaj eksplodiranih krogel, ko izgine zadnja, pa se
 izpiše, koliko žog je eksplodiralo. S tem se program konča.

Za oceno 10: Sprogramirajte igro z 10 stopnjami. Na začetku vsake stopnje se napiše, koliko žog je v igri in koliko jih
 je eksplodiralo. Na koncu, ko izgine zadnja eksplodirana krogla, se igra nadaljuje na naslednji stopnji, če je eksplodiralo dovolj žog. Sicer pa se pojavi okno, v katerem piše, koliko žog je eksplodiralo in da je to premalo; igra se ponovi na isti stopnji. Izmislite smiselna števila žog. Stopnje se morajo seveda razlikovati.
'''

def Igraj_Igro(igre):
    for cilj, st_zog in igre:
        igra = Igra(st_zog, cilj)

        while not igra.igraj():
            igra = Igra(st_zog, cilj)

    QMessageBox.information(None, "Uspeh", "Zmaga!")

igre = [(1,6), (2, 6), (250,250), (4,12), (6,16), (8,18), (10,22), (12,26), (14,30), (16,40)]

Igraj_Igro(igre)