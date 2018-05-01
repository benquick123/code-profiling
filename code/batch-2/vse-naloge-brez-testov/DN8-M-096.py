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


def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz.strip() == "DESNO":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz.strip() == "LEVO":
        smer = smeri[(ismer - 1) % 4]
    else:
        s = 0
        for e in ukaz.split():
            if e.isdigit():
                s = int(e)
        dx, dy = premiki[ismer]
        x += dx * s
        y += dy * s
    return x, y, smer




def izvedi(ime_datoteke):
    datoteka = open(ime_datoteke)
    sez = [(0, 0, "N")]
    x, y, smer = 0, 0, "N"
    for e in datoteka:
        n = premik(e, x, y, smer)
        sez.append(n)
        x = n[0]
        y = n[1]
        smer = n[2]
    return sez


def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer = "<"
    return "{:>3}:{:<3} {}".format(x, y, smer)

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    sez = izvedi(ime_vhoda)
    for e in sez:
        a = opisi_stanje(e[0], e[1], e[2])
        datoteka.write(a+"\n")
    datoteka.close()

