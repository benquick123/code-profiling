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
    premiki = []
    seznam = []
    x = 0
    y = 0
    smer = "N"
    premiki.append((x, y, smer))
    for ukaz in open(ime_datoteke):
        if ukaz == "DESNO\n":
            seznam.append("R")
        elif ukaz == "LEVO\n":
            seznam.append("L")
        else:
            seznam.append(int(ukaz.split()[1]))
    for ukazi in seznam:
        premiki.append(premik(ukazi, x, y, smer))
        x = premiki[-1][0]
        y = premiki[-1][1]
        smer = premiki[-1][2]
    return premiki

def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    if smer == "S":
        smer = "v"
    if smer == "E":
        smer = ">"
    if smer == "W":
        smer = "<"
    return "{x:>3}:{y:<3} {smer}".format(x=x, y=y, smer = smer)

def prevedi(ime_vhoda, ime_izhoda):
    stara = izvedi(ime_vhoda)
    nova = open(ime_izhoda, "w")
    for korak in stara:
        stanje = opisi_stanje(korak[0], korak[1], korak[2])
        nova.write("{}{}".format(stanje, "\n"))


