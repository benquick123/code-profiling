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
    datoteka = open(ime_datoteke, encoding="UTF8").read().split("\n")

    ukazi = []
    for item in datoteka:
        g = item.lstrip()
        ukazi.append(g)

    x = 0
    y = 0
    smer = "N"
    pot = []
    pot.append((x, y, smer))

    for ukaz in ukazi:
        if ukaz == "DESNO":
            del_poti = premik("R", x, y, smer)
            x, y, smer = del_poti
            pot.append(del_poti)

        elif ukaz == "LEVO":
            del_poti = premik("L", x, y, smer)
            x, y, smer = del_poti
            pot.append(del_poti)

        elif "NAPREJ" in ukaz:
            tabelca = ukaz.split("NAPREJ")
            stevilo = int(tabelca[1])

            del_poti = premik(stevilo, x, y, smer)
            x, y, smer = del_poti
            pot.append(del_poti)

    return pot

def opisi_stanje(x, y, smer):
    if smer == "N":
        puscica = "^"

    elif smer == "S":
        puscica = "v"

    elif smer == "E":
        puscica = ">"

    elif smer == "W":
        puscica = "<"

    dvopicje = ":"
    odgovor = ("{x:>3}{dvopicje}{y:<3}".format(x=x, y=y, dvopicje=dvopicje)) + " " + puscica

    return odgovor

def prevedi(ime_vhoda, ime_izhoda):
    izvor = izvedi(ime_vhoda)
    cilj = open(ime_izhoda, "w")
    for item in izvor:
        x, y, smer = item
        dodatek = opisi_stanje(x, y, smer)+"\n"
        cilj.write(dodatek)

    cilj.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        puscica = "^"

    elif smer == "S":
        puscica = "v"

    elif smer == "E":
        puscica = ">"

    elif smer == "W":
        puscica = "<"

    dvopicje = ":"
    prazno = 3 - len(str(x))
    dodatek = prazno * " "
    odgovor = puscica+" "+dodatek+("{}{x:>}{dvopicje}{y:<}".format("(",x=x, y=y, dvopicje=dvopicje))+")"

    return odgovor


