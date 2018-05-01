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
    datoteka = open(ime_datoteke)
    seznam = [(0, 0, 'N')]
    x = y = 0
    smer = "N"
    for vrstica in datoteka:
        #vrsta = vrstica.strip()
        if "DESNO" in vrstica:
            ukaz = "R"
        elif "LEVO" in vrstica:
            ukaz = "L"
        elif "NAPREJ" in vrstica:
            ukaz = int(vrstica.split(" ")[1])
        seznam.append(premik(ukaz, x, y, smer))
        x, y, smer = premik(ukaz, x, y, smer)
    return seznam


def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    if smer == "E":
        smer = ">"
    if smer == "W":
        smer = "<"
    if smer == "S":
        smer = "v"
    return ("{x:>3}:{y:<3} {smer}".format(x=x, y=y, smer=smer))


def prevedi(ime_vhoda, ime_izhoda):
    vhod = izvedi(ime_vhoda)
    s = open(ime_izhoda, "w")
    for x, y, smer in vhod:
        s.write(opisi_stanje(x, y, smer) + "\n")


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smer = "^"
    if smer == "E":
        smer = ">"
    if smer == "W":
        smer = "<"
    if smer == "S":
        smer = "v"
    x = "(" + str(x)
    return ("{smer}{x:>5}:{y})".format(x=x, y=y, smer=smer))



