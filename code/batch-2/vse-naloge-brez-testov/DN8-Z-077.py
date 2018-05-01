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
# end def

def izvedi(ime_datoteke):
    x, y, smer = 0, 0, "N"
    ukazi = [(x, y, smer)]
    for vrstica in open(ime_datoteke):
        ukaz = vrstica.strip()
        ukaz = ukaz.split()

        if ukaz[0] == "LEVO":
            ukaz = "L"
        elif ukaz[0] == "DESNO":
            ukaz = "R"
        elif ukaz[0] == "NAPREJ":
            ukaz = int(ukaz[1])
        else:
            break

        ukazi.append(premik(ukaz, x, y, smer))
        x, y, smer = ukazi[-1]


    return ukazi
# end def

def opisi_stanje(x, y, smer):
    niz = "%3d:%-4d" % (x, y)
    if smer == "N":
        niz += "^"
    elif smer == "E":
        niz += ">"
    elif smer == "W":
        niz += "<"
    elif smer == "S":
        niz += "v"
    return niz
# end def


def prevedi (ime_vhoda, ime_izhoda):
    ukazi = izvedi(ime_vhoda)
    izhod = ""
    for e in ukazi:
        izhod += opisi_stanje(e[0], e[1], e[2])
        izhod += "\n"
    datoteka = open(ime_izhoda, "w")
    datoteka.write(izhod)
    datoteka.close()

