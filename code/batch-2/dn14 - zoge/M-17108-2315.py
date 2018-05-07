import risar
from random import randint
from math import sqrt
from PyQt5.QtWidgets import QMessageBox

def nakljucne_koordinate():                     #oddali zoge od roba
    from random import randint
    return randint(30, risar.maxX-30), randint(30, risar.maxY-30)

naslednja_stopnja = False
ista_stopnja = False

def stopnja(st_zog, eksplozije):
    def zaleten_krog():
        krog.setRect(-30, -30, 60, 60)  # povecas krog, ga ustavis, pobarvas in dodas v seznam ustavljeni_krogi
        ustavljeni_krogi.append(krog)
        vx[i], vy[i] = 0, 0

        c = krog.pen().color().lighter()  # barvanje kroga
        c.setAlpha(192)
        krog.setBrush(c)

        cas_ustavljenih_krogov.append(cas)
        bool_krogi.append(True)

    krogi = []
    vx = []
    vy = []
    ustavljeni_krogi = []
    cas_ustavljenih_krogov = []
    bool_krogi = []
    risar.pobrisi()
    risar.klik = False
    miska = True
    global naslednja_stopnja
    global ista_stopnja
    ista_stopnja = False
    naslednja_stopnja = False
    izhod = False

    for i in range(st_zog):  #ustvaris "st_zog" zog na razlicnih lokacijah, z razlicnimi barvami in smermi oz. hitrosti
        x, y = nakljucne_koordinate()

        krog = risar.krog(x, y, 10, barva=risar.nakljucna_barva(), sirina=2)

        krogi.append(krog)

        x = randint(-5, 5)
        vx.append(x)
        y = sqrt(25-x**2)

        seznam = [y, -y]

        izberi_y = randint(0,1)
        vy.append(seznam[izberi_y])

    krog_miska = risar.krog(risar.maxX/2, risar.maxY/2, 30, barva=risar.bela, sirina=2) #ustvaris objekt za krog, ki bo sledil miski in ga skrijes
    krog_miska.hide()
    risar.miska = (600, 500)
    cas = 0
    cas_miska = 0

    for i in range(1000000):
        for i in range(len(krogi)):
            if izhod:
                break
            krog = krogi[i]
            krog.setPos(krog.x() + vx[i], krog.y() + vy[i])     #updatanje pozicije
            if not (0 < krog.x() < risar.maxX):
                vx[i] = -vx[i]                          #odbijanje od roba
            if not (0 < krog.y() < risar.maxY):
                vy[i] = -vy[i]

            if not risar.klik:                  #če miška še ni bila pritisnena, krog sledi miški
                x, y = risar.miska
                if (0 < x < risar.maxX) and (0 < y < risar.maxY):      #krog pokažeš prvič ko pride miška v igralno polje
                    krog_miska.show()
                    krog_miska.setPos(x, y)
                    cas_miska = cas             #shraniš čas, ko je bila miška pritisnena
            else:
                if cas-cas_miska == 200:
                    krog_miska.hide()
                    miska = False
                                                                       #ko je miška pritisnena se krog ustavi
                if (abs(krog.x()-x) <= 30) and (abs(krog.y()-y) <= 30) and miska:        #ko je razdalja med pritisnejeno zogo in katerokoli drugo manjsa od 30 absolutno
                    if krog not in ustavljeni_krogi:                           #to zogo povecamo na 30 jo samo enkrat dodamo v seznam ustavljeni_krogi in jih fiksiramo koordinate.
                        zaleten_krog()

            for a in range(len(ustavljeni_krogi)):                                  #ko katera koli žoga prileti na katerokoli od že ustavljenih se tudi sama ustavi in doda v seznam ustavljeni_krogi
                k = ustavljeni_krogi[a]
                if (abs(krog.x() - k.x()) <= 30) and (abs(krog.y() - k.y()) <= 30) and bool_krogi[a]:
                    if krog not in ustavljeni_krogi:
                        zaleten_krog()
                if cas-cas_ustavljenih_krogov[a] == 200:
                    k.hide()
                    bool_krogi[a] = False

            if not any(bool_krogi) and len(bool_krogi) > 0 :        #če so vsi eksplodirali, se igra konča
                if len(ustavljeni_krogi) < eksplozije:
                    QMessageBox.information(None, "Opozorilo", "Eksplodiralo je " + str(len(ustavljeni_krogi)) + " žog. Premalo.")
                    ista_stopnja = True
                    izhod = True
                else:
                    QMessageBox.information(None, "Opozorilo", "Eksplodiralo je " + str(len(ustavljeni_krogi)) + " žog. Uspelo ti je!")
                    izhod = True

            if len(bool_krogi) == 0 and not miska:
                QMessageBox.information(None, "Opozorilo", "Eksplodiralo je 0 žog. Premalo")
                ista_stopnja = True
                izhod = True

        if izhod:
            break

        cas += 1
        risar.cakaj(0.02)


seznam_zog = [5,10,15,20,25,30,40,50,70,100]
seznam_eksplozij= [1,3,5,8,11,13,18,40,60,90]

stevec = 0
ista_stopnja = True
while stevec < 10:
    ista_stopnja = True
    while ista_stopnja:
        QMessageBox.information(None, "Začetek stopnje {}!".format(stevec+1), "Eksplodirati moraš {} od {} žog".format(seznam_eksplozij[stevec], seznam_zog[stevec]))
        stopnja(seznam_zog[stevec], seznam_eksplozij[stevec])

    stevec += 1
