import risar
import random
import math
from PyQt5.QtWidgets import QMessageBox

class Zoga():
    def __init__(self):
        self.koordinate = risar.nakljucne_koordinate()
        self.x = self.koordinate[0]
        self.y = self.koordinate[1]

        if self.x >= risar.maxX - 10:
            self.x -= 10
        elif self.x <= 10:
            self.x += 10

        if self.y >= risar.maxY - 10:
            self.y -= 10
        elif self.y <= 10:
            self.y += 10

        self.polmer = 10
        self.sirina = 3

        self.barva = risar.nakljucna_barva()
        self.hitrostX = random.randint(-5, 5)
        self.hitY = math.sqrt(5 ** 2 - self.hitrostX ** 2)
        self.hitrostY = random.choice([self.hitY, -self.hitY])

        self.zogica = risar.krog(self.x, self.y, self.polmer, self.barva, self.sirina)
        self.je_eksplodirala = False

    def premik(self):
        self.zogica.setPos(self.x, self.y)

        if self.x <= 10 or self.x >= risar.maxX - 10:
            self.x -= self.hitrostX
            self.y += self.hitrostY
            self.hitrostX = -self.hitrostX

        elif self.y <= 10 or self.y >= risar.maxY - 10:
            self.x += self.hitrostX
            self.y -= self.hitrostY
            self.hitrostY = -self.hitrostY

        else:
            self.x += self.hitrostX
            self.y += self.hitrostY

    def vrni_koordinate(self):
        return (self.x, self.y)

    def eksplodiraj(self):
        self.zogica.setRect(-30, -30, 60, 60)
        self.je_eksplodirala = True
        c = self.zogica.pen().color().lighter()
        c.setAlpha(100)
        self.zogica.setBrush(c)

    def vrni_stanje(self):
        return self.je_eksplodirala

    def skrij(self):
        self.zogica.hide()

class Mis():
    def __init__(self):
        self.x = risar.miska[0]
        self.y = risar.miska[1]

        self.polmer = 30
        self.sirina = 3
        self.barva = risar.barva("white")

    def spremeni_pozicijo(self):
        self.x = risar.miska[0]
        self.y = risar.miska[1]
        self.krogec = risar.krog(self.x, self.y, self.polmer, self.barva, self.sirina)
        risar.odstrani(self.krogec)

    def postavi(self):
        self.krogec = risar.krog(self.x, self.y, self.polmer, self.barva, self.sirina)
        c = self.krogec.pen().color().lighter()
        c.setAlpha(100)
        self.krogec.setBrush(c)
        return (self.x, self.y)

    def skrij(self):
        self.krogec.hide()

def igra():
    zoga = Zoga()
    for i in range(670):
        zoga.premik()
        risar.cakaj(0.02)
    risar.stoj()

def igra_z_vec_zogicami():
    zogice = [Zoga() for i in range(30)]
    for i in range(670):
        for zogica in zogice:
            zogica.premik()
        risar.cakaj(0.02)
    risar.stoj()

def igra_z_misko():
    zogice = [Zoga() for i in range(30)]
    miska = Mis()
    mis_postavljena = False
    for i in range(670):

        if not risar.klik:
            miska.spremeni_pozicijo()
        if not mis_postavljena and risar.klik:
            k_miske = miska.postavi()
            mis_postavljena = True

        for zogica in zogice:
            zogica.premik()
            if mis_postavljena:
                k_zogice = zogica.vrni_koordinate()
                if (k_zogice[0] - k_miske[0])**2 + (k_zogice[1] - k_miske[1])**2 < 40**2:
                    risar.stoj()

        risar.cakaj(0.02)

    risar.stoj()

def igra_z_eksplozijami():
    zogice = [Zoga() for i in range(30)]
    miska = Mis()
    mis_postavljena = False
    zaletljivi_objekti = {}
    igra_v_teku = True
    casovi = {}
    stevilo_eksplodiranih = 0
    while igra_v_teku:
        if not risar.klik:
            miska.spremeni_pozicijo()
        if not mis_postavljena and risar.klik:
            k_miske = miska.postavi()
            zaletljivi_objekti[str(miska)] = (k_miske[0], k_miske[1])
            mis_postavljena = True
            casovi[str(miska)] = 0
        for zogica in zogice:
            if not zogica.vrni_stanje():
                zogica.premik()
            if mis_postavljena:
                c = casovi.copy()
                if str(miska) in c and c[str(miska)] >= 180:
                    del(casovi[str(miska)])
                    del(zaletljivi_objekti[str(miska)])
                    miska.skrij()
                if str(zogica) in c and c[str(zogica)] >= 180:
                    del(casovi[str(zogica)])
                    del(zaletljivi_objekti[str(zogica)])
                    zogica.skrij()

                zo = zaletljivi_objekti.copy()
                k_zogice = zogica.vrni_koordinate()
                for objekt in zo.values():
                    if (k_zogice[0] - objekt[0])**2 + (k_zogice[1] - objekt[1])**2 < 40**2 and not zogica.vrni_stanje():
                        zogica.eksplodiraj()
                        stevilo_eksplodiranih += 1
                        zaletljivi_objekti[str(zogica)] = (k_zogice[0], k_zogice[1])
                        casovi[str(zogica)] = 0

        for cas in casovi:
            casovi[cas] += 1
        if len(zaletljivi_objekti) == 0 and mis_postavljena:
            igra_v_teku = False
        risar.cakaj(0.02)
    a = QMessageBox.information(None, "Okno", "Konec igre! Eksplodiralo je {} žog.".format(stevilo_eksplodiranih))

    risar.stoj()

print("Naloge:")
print("6 - za oceno 6")
print("7 - za oceno 7")
print("8 - za oceno 8")
print("9 - za oceno 9")
vnos = int(input("Naloga: "))
if vnos == 6:
    igra()
elif vnos == 7:
    igra_z_vec_zogicami()
elif vnos == 8:
    igra_z_misko()
elif vnos == 9:
    igra_z_eksplozijami()


