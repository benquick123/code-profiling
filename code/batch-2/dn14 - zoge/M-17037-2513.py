from random import randint, choice
import risar
import time
from math import sqrt
from PyQt5.QtWidgets import QMessageBox

#zidovi = [(10,10), (10,risar.maxY - 12), (risar.maxX - 12, 10), (risar.maxX - 12, risar.maxY - 12)]
uporabljene_barve = []


class Zogica():
    def __init__(self):
        #izberemo manjše okno, da ne slučajno ne bi naredil loop
        #self.x = randint(10, risar.maxX - 12)
        #self.y = randint(10, risar.maxY - 12)
        self.x = randint(30, risar.maxX - 32)
        self.y = randint(30, risar.maxY - 32)
        self.debelina = 10
        self.ovoj = 2
        self.pot_x = randint(-5, 5)
        self.pot_y = choice([1, -1]) * sqrt(5**2 - self.pot_x**2)
        self.barva = risar.barva(randint(0,255), randint(0,255), randint(0,255))
        while self.barva in uporabljene_barve:
            self.barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
        uporabljene_barve.append(self.barva)
        self.zogica = risar.krog(self.x, self.y, self.debelina, self.barva, self.ovoj)
        self.odboj = False
        self.odboj_stena = 0
        self.update()

    def update(self):
        self.zogica.setPos(self.x, self.y)
        if (risar.maxX - 12 - abs(self.pot_x) < self.x or self.x  <= 10 + abs(self.pot_x)):
            self.odboj_stena = "navpicna"
            if self.x > risar.maxX / 2:
                tmp_x = risar.maxX - 12 - self.x
            else:
                tmp_x = self.x - 10
            if self.pot_x == 0:
                self.pot_x = 1
            tmp_y = ((tmp_x * 100) / abs(self.pot_x)) / 100 * self.pot_y
            self.x += tmp_x
            self.y -= tmp_y
            self.odboj = True
            self.zogica.setPos(self.x, self.y)
        elif (risar.maxY - 12 - abs(self.pot_y) <= self.y or self.y < 10 + abs(self.pot_y)):
            self.odboj_stena = "vodoravna"
            if self.y < risar.maxY / 2:
                tmp_y = self.y - 10
            else:
                tmp_y = risar.maxY - 12 -self.y
            if self.pot_y == 0:
                self.pot_y = 1
            tmp_x = (((tmp_y * 100) / abs(self.pot_y)) / 100) * self.pot_x
            self.x += tmp_x
            self.y -= tmp_y
            self.odboj = True
            self.zogica.setPos(self.x, self.y)
        if self.odboj:
            self._odboj_od_stene()

    def _odboj_od_stene(self):
        if self.odboj_stena == "navpicna":
            self.pot_x = -self.pot_x
        elif self.odboj_stena == "vodoravna":
            self.pot_y = -self.pot_y
        self.odboj = False
        self.odboj_stena = 0

    def potovanje(self):
        self.x += self.pot_x
        self.y += self.pot_y
        self.update()

class MorjeZogic():
    def __init__(self, z):
        self.zogice = []
        self.kord_zogice = {}
        for zogica in range(z):
            zogica = Zogica()
            self.zogice.append(zogica)
            self.kord_zogice[zogica] = (zogica.x, zogica.y)

    def potovanje(self):
        for zogica in self.zogice:
            zogica.potovanje()
            self.kord_zogice[zogica] = (zogica.x, zogica.y)


class ZadeteZogice(MorjeZogic):
    def __init__(self, z):
        super().__init__(z)
        self.zadeta = False
        x, y = risar.miska
        self.miskin_klik = risar.klik
        self.obroba_miske = risar.krog(x, y, 30, risar.bela, 2)
        self.koor = (0,0)
        self.update()

    def update(self):
        if not self.miskin_klik:
            x, y = risar.miska
            self.obroba_miske.setPos(x, y)
            self.miskin_klik = risar.klik
            if self.miskin_klik:
                self.koor = (x, y)

    def potovanje(self):
        super().potovanje()
        if self.miskin_klik == True:
            for x, y in self.kord_zogice.values():
                if abs(abs(self.koor[0]) - abs(x)) < 42 and abs(abs(self.koor[1]) - abs(y)) < 42:
                #if self.koor[0]-32 <= x < self.koor[0] + 32 and self.koor[1]-32 <= y < self.koor[1] + 32:
                    self.zadeta  = True
                    risar.klik = False
        self.update()


class EksplodiraneZogice():
    def __init__(self, z):
        self.sporocilo = False
        self.zogice = []
        self.kord_zogice = {}
        for zogica in range(z):
            zogica = Zogica()
            self.zogice.append(zogica)
            self.kord_zogice[zogica] = zogica.x, zogica.y
        x, y = risar.miska
        self.ekplodirane = True
        self.klik_miske = risar.klik
        self.obroba_miske = risar.krog(x, y, 30, risar.bela, 2)
        self.kord_ekplozij = {}
        self.st_zadetih = 0
        self.st_vseh = len(self.zogice)
        self.update()

    def update(self):
        if not self.sporocilo:
            QMessageBox.information(None, "Navodilo",
                                    "Izberi strateško lokacijo za postavitev pasti, tako da se bo čim večje število "
                                    "žogic nabodlo in eksplodiralo.")
            self.sporocilo = True
        if not self.klik_miske:
            x, y = risar.miska
            self.obroba_miske.setPos(x, y)
            self.klik_miske = risar.klik
            if self.klik_miske:
                self.kord_ekplozij[self.obroba_miske] = x, y, time.time()
        if self.kord_ekplozij == {} and self.klik_miske == True:
            if self.st_vseh == self.st_zadetih:
                QMessageBox.information(None, "WOOHOO",
                                        "Čestitke. Uspelo ti je uničiti vse žogice. Pohvalno.")
            elif self.st_zadetih == 0:
                QMessageBox.information(None, "BOOOO",
                                        "Čestitke, neke vrste. Si eden izmed najslabših igralcev.")
            else:
                QMessageBox.information(None, "Rezultat",
                                    "Od {} žogic ti jih je uspelo zadeti {}.".format(self.st_vseh, self.st_zadetih))
            self.ekplodirane = risar.klik = False
        else:
            self._izbris()

    def _izbris(self):
        tmp = []
        for baloncek, ostalo in self.kord_ekplozij.items():
            x, y, cas = ostalo
            if cas + 4 < time.time():
                try:
                    baloncek.hide()
                except:
                    baloncek.zogica.hide()
                tmp.append(baloncek)
        if tmp:
            for el in tmp:
                del self.kord_ekplozij[el]

    def potovanje(self):
        for zogica in self.zogice:
            zogica.potovanje()
            self.kord_zogice[zogica] = (zogica.x, zogica.y)
        if self.klik_miske == True:
            tmp_zogice = set()
            for objekt in self.zogice:
                for ignore in self.kord_zogice[objekt]:
                    x, y = self.kord_zogice[objekt]
                    tmp_ekplozije = {}
                    for terka2 in self.kord_ekplozij.values():
                        xk, yk, t = terka2
                        if abs(abs(xk) - abs(x)) < 40 and abs(abs(yk) - abs(y)) < 40:
                            objekt.zogica.setRect(-30, -30, 60, 60)
                            j = objekt.zogica.pen().color().lighter()
                            j.setAlpha(192)
                            objekt.zogica.setBrush(j)
                            tmp_ekplozije[objekt] = x, y, time.time()
                            tmp_zogice.add(objekt)

                    if tmp_ekplozije:
                        self.kord_ekplozij.update(tmp_ekplozije)
            if tmp_zogice:
                for el in tmp_zogice:
                    self.st_zadetih += 1
                    del self.kord_zogice[el]
                    self.zogice.remove(el)
        self.update()

slovenscina = ["žogo", "žogi", "žoge", "žog"]
st_zog = [5,10,15,20,25,30,35,40,45,50]
st_zahtevanih = [2,5,7,10,15,17,21,28,38,45]

class EksplodiraneZogiceHard(EksplodiraneZogice):
    def __init__(self, v):
        super().__init__(v)
        self.neuspesno = True
        self.cilj = st_zahtevanih[st_zog.index(v)]
        self.kroglic = v
        if self.cilj == 2:
            self.slovenscina = 1
        elif self.cilj == 3:
            self.slovenscina = 2
        else:
            self.slovenscina = 3
        QMessageBox.information(None, "Level {}".format(self.kroglic//5),
                                "Razstreli {} {} od {}. žog.".format(self.cilj, slovenscina[self.slovenscina], v))
        self.update()

    def update(self):
        if not self.klik_miske:
            x, y = risar.miska
            self.obroba_miske.setPos(x, y)
            self.klik_miske = risar.klik
            if self.klik_miske:
                self.kord_ekplozij[self.obroba_miske] = x, y, time.time()
        if self.kord_ekplozij == {} and self.klik_miske == True:
            if self.cilj > self.st_zadetih:
                st_zadetih_slo = self.st_zadetih - 1
                if st_zadetih_slo > 2:
                    st_zadetih_slo = 3
                QMessageBox.information(None, "Več sreče prihodnjič :)",
                                    "Uspelo ti je razstreliti samo {} {}. Poskusi še enkrat.".format(self.st_zadetih, slovenscina[st_zadetih_slo]))
                self.ekplodirane = risar.klik = False
            else:
                if self.cilj != 50:
                    QMessageBox.information(None, "Čestitke",
                                        "Končal si {}. level. Do konca jih imaš še {}.".format(self.kroglic//5, 10-self.kroglic//5))
                self.ekplodirane = self.neuspesno = risar.klik = False
        else:
            super()._izbris()


def naloga6():
    naloga_6 = Zogica()
    koncni_cas = time.time() + 21
    while time.time() < koncni_cas:
        naloga_6.potovanje()
        risar.cakaj(0.02)
    risar.pobrisi()

def naloga7():
    naloga_7 = MorjeZogic(30)
    koncni_cas = time.time() + 21
    while time.time() < koncni_cas:
        naloga_7.potovanje()
        risar.cakaj(0.02)
    risar.pobrisi()

def naloga8():
    naloga_8 = ZadeteZogice(30)
    while not naloga_8.zadeta:
        naloga_8.potovanje()
        risar.cakaj(0.02)
    risar.pobrisi()

def naloga9():
    naloga_9 = EksplodiraneZogice(30)
    while naloga_9.ekplodirane:
        naloga_9.potovanje()
        risar.cakaj(0.02)
    risar.pobrisi()

def naloga10():
    st = 5
    igra1 = EksplodiraneZogiceHard(st)
    while igra1.neuspesno == True:
        while igra1.ekplodirane:
            igra1.potovanje()
            risar.cakaj(0.02)
        risar.pobrisi()
        if igra1.neuspesno == False:
            risar.pobrisi()
            st += 5
            if st >= 55:
                QMessageBox.information(None, "Čestitke",
                                        "Čestitke, preobrnil si igrico. Ni bilo težko, kaj ne?")
                break
            igra1 = EksplodiraneZogiceHard(st)
        else:
            risar.pobrisi()
            igra1 = EksplodiraneZogiceHard(st)
    risar.pobrisi()


naloga6()
naloga7()
naloga8()
naloga9()
naloga10()
