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
    datoteka = open("{}".format(ime_datoteke))
    seznam_ukazov = datoteka.read()
    seznam_ukazov = seznam_ukazov.split("\n")
    pot = [(0, 0, 'N')]
    x = y = 0
    smer = "N"
    for ukaz in seznam_ukazov:
        del_ukaza = ukaz.split(" ")
        if "DESNO" in del_ukaza:
            ukaz = "R"
        elif "LEVO" in del_ukaza:
            ukaz = "L"
        elif ukaz == "":
            return pot
        else:
            ukaz = int(del_ukaza[1])
        korak = premik(ukaz, x, y, smer)
        x = korak[0]
        y = korak[1]
        smer = korak[2]
        pot += [korak]
    return pot

def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    if smer == "E":
        smer = ">"
    if smer == "S":
        smer = "v"
    if smer == "W":
        smer = "<"
    return "{x:>3.0f}:{y:<3.0f} {smer}".format_map(locals())

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        datoteka.write(opisi_stanje(x, y, smer)+"\n")
    datoteka.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smer = "^"
    if smer == "E":
        smer = ">"
    if smer == "S":
        smer = "v"
    if smer == "W":
        smer = "<"
    izpis = "{}".format(smer) + " "*(4-len(str(x))) + "(" + "{x}:{y}".format_map(locals()) + ")"
    return izpis

