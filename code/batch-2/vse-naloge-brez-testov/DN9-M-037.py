def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "R":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "L":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer


def izvedi(ime_datoteke):
    datoteka = open(ime_datoteke, "r", encoding="utf-8")
    x, y, tr_smer = 0, 0, "N"
    vsi_trojcki = [(x, y, tr_smer)]
    for ukaz in datoteka:
        if ukaz.strip() == "DESNO":
            x, y, tr_smer = premik("R", x, y, tr_smer)
        elif ukaz.strip() == "LEVO":
            x, y, tr_smer = premik("L", x, y, tr_smer)
        else:
            ukaz = int(ukaz.strip().split()[1])
            x, y, tr_smer = premik(ukaz, x, y, tr_smer)
        vsi_trojcki.append((x, y, tr_smer))
    datoteka.close()
    return vsi_trojcki

def opisi_stanje(x, y, smer):
    smeri = "NESW"
    nebesa = "^>v<"
    nebo = nebesa[smeri.index(smer)]
    return ("{X:>3}:{Y:<3} {S}".format(X = x, Y = y, S = nebo))


def prevedi(ime_vhoda, ime_izhoda):
    nujni_izhod = open(ime_izhoda, "w", encoding="utf-8")
    izvedenec = izvedi(ime_vhoda)
    for x, y, smer in izvedenec:
        nujni_izhod.write(opisi_stanje(x, y, smer)+"\n")
    nujni_izhod.close()
    return


def opisi_stanje_2(x, y, smer):
    smeri = "NESW"
    nebesa = "^>v<"
    nebo = nebesa[smeri.index(smer)]
    prva = "(" + str(x)
    druga = str(y) + ")"
    return ("{S} {X:>4}:{Y}".format(S=nebo, X= prva, Y= druga))












