import risar
import random
import math
import time
from PyQt5.QtWidgets import QMessageBox


class Kroglica:
    def __init__(self):
        self.x = random.randint(10, risar.maxX - 10)
        self.y = random.randint(10, risar.maxY - 10)
        self.r = 10
        self.color = risar.nakljucna_barva()

        self.hitrost_X = random.randint(-5, 5)
        self.hitrost_Y = math.sqrt(25 - self.hitrost_X ** 2)

        self.object = risar.krog(self.x, self.y, self.r, self.color)

        self.exploded = False

    def shrani(self, sez):
        sez.append((self.exploded, self.object, self.hitrost_X, self.hitrost_Y))


stopnja = 0
parametri_stopenj = ((1, 5), (3, 5), (5, 10), (8, 10), (10, 15), (13, 15), (16, 20), (18, 20), (20, 25), (22, 25))

while stopnja < 10:

    # Izpis potreb za naslednjo stopnjo
    QMessageBox.information(None, "Rezultat", "Eksplodirajte " + str(parametri_stopenj[stopnja][0]) + " od " + str(parametri_stopenj[stopnja][1]) + " žog.")

    sez_kroglic = []
    nov_sez_kroglic = []
    miska_krog = risar.krog(risar.miska[0], risar.miska[1], 30)

    # Definiramo kroglice
    for i in range(parametri_stopenj[stopnja][1]):
        # Ustvarimo objekt
        kroglica = Kroglica()

        # Potrebne podatke shranimo v seznam
        kroglica.shrani(sez_kroglic)

    koordinate_eks_kroglic = [()]
    nove_koordinate_eks_kroglic = []
    konec = False
    st_explodiranih = 0

    while True:

        # Posodbaljanje miške do klika
        if not risar.klik:
            miska_krog.setPos(risar.miska[0], risar.miska[1])
            koordinate_eks_kroglic[0] = (miska_krog.x(), miska_krog.y(), time.time(), miska_krog)

        # Preverjanje vseh (neeksplodiranih) žog
        for stanje, kroglica, hitrost_X, hitrost_Y in sez_kroglic:
            # Če smo kliknii
            if risar.klik:

                # Pregledamo vse eksplodirane žoge
                for x, y, cas, eks_kroglica in koordinate_eks_kroglic:

                    # Če so od ekplozije minile 4 sekunde skrijemo kroglico IN JO NE DODAMO V SEZNAM ZA NASLEDNJI KROG
                    if time.time() - cas >= 4:
                        eks_kroglica.hide()
                        continue

                    # Če od ekplozije niso minile 4 sekunde ŽE EKSPLODIRANO KROGLICO DODAMO V SEZNAM ZA NASLEDNJI KROG
                    else:
                        nove_koordinate_eks_kroglic.append((x, y, cas, eks_kroglica))

                    # Če žoga še ni ekplodirana, pregledamo če se nahaja v območju eksplodirane žoge
                    if not stanje and (kroglica.x() > x - 40 and kroglica.x() < x + 40) and (kroglica.y() > y - 40 and kroglica.y() < y + 40):
                        # Če se, povečamo števec za 1
                        st_explodiranih += 1

                        # Žogo ustavimo
                        hitrost_X = 0
                        hitrost_Y = 0

                        # Nastavimo stanje na eksplodirano
                        stanje = True

                        # Povečamo obseg
                        kroglica.setRect(-30, -30, 60, 60)

                        # Spremenimo polnilo
                        c = kroglica.pen().color().lighter()
                        c.setAlpha(192)
                        kroglica.setBrush(c)

                        # Eksplodirano žogico dodamo v seznam za naslednji krog
                        nove_koordinate_eks_kroglic.append((kroglica.x(), kroglica.y(), time.time(), kroglica))

                # Ko preverimo vse eksplodirane kroglice, pogledamo, če jih je še kaj ostalo
                if len(nove_koordinate_eks_kroglic) == 0:

                    # Če ne nastavimo pogoj za konec na True
                    konec = True

                    # In zlomimo zanko
                    break

                # Če so kroglice še ostale
                else:
                    # Shranimo seznam, ki smo ga zgradili (za naslednji krog), v originalni seznam
                    koordinate_eks_kroglic = nove_koordinate_eks_kroglic[:]

                    # Seznam za naslednji krog povozimo s praznim
                    nove_koordinate_eks_kroglic = []

            # Pogledamo, če nam je kroglica "ušla" z okna (x os)
            if kroglica.x() + 10 >= risar.maxX or kroglica.x() - 10 <= 0:
                hitrost_X *= -1

            # Pogledamo, če nam je kroglica "ušla" z okna (y os)
            if kroglica.y() + 10 >= risar.maxY or kroglica.y() - 10 <= 0:
                hitrost_Y *= -1

            # Kroglici posodobimo položaj
            kroglica.setPos(kroglica.x() + hitrost_X, kroglica.y() + hitrost_Y)

            # V seznam kroglic za naslednji krog dodamo kroglico
            nov_sez_kroglic.append((stanje, kroglica, hitrost_X, hitrost_Y))

        # Če je pogoj za prekinitev resničen
        if konec:

            # Če smo eksplodirali dovolj kroglic
            if st_explodiranih >= parametri_stopenj[stopnja][0]:

                # Izpišemo sporočilo
                QMessageBox.information(None, "Rezultat", "Eksplodirali ste " + str(st_explodiranih) + " od " + str(
                    parametri_stopenj[stopnja][1]) + " žog. Nadaljujete na naslednjo stopnjo.")

                # Povečamo stopnjo
                stopnja += 1

                # Nastavimo klik na false
                risar.klik = False

                # Skrijemo kroglice te stopnje
                for stanje, kroglica, hitrost_X, hitrost_Y in sez_kroglic:
                    kroglica.hide()

                # Zlomimo zanko
                break

            # Če nismo
            else:
                # Izpišemo sporočilo
                QMessageBox.information(None, "Rezultat", "Eksplodirali ste " + str(st_explodiranih) + " od " + str(
                    parametri_stopenj[stopnja][1]) + " žog. Ostajate na trenutni stopnji.")

                # Klik nastavimo na false
                risar.klik = False

                # Skrijemo kroglice te stopnje
                for stanje, kroglica, hitrost_X, hitrost_Y in sez_kroglic:
                    kroglica.hide()

                # Zlomimo zanko
                break

        # Shranimo seznam s posodobljanimi koordinatami kroglic v originalni seznam
        sez_kroglic = nov_sez_kroglic[:]

        # Seznam s posodobljnimi koordinatami povozimo s praznim
        nov_sez_kroglic = []

        # Malo počakamo
        risar.cakaj(0.02)
