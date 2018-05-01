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
    x = 0
    y = 0
    sme = "N"

    seznam = []
    seznam.append((x, y, sme))

    for v in open(ime_datoteke).read().splitlines():

        if v == "DESNO":
            x, y, sme = premik("R", x, y, sme)
            seznam.append((x, y, sme))

        if v == "LEVO":
            x, y, sme = premik("L", x, y, sme)
            seznam.append((x, y, sme))

        if "NAPREJ" in v:
            kam, za = v.split()
            x, y, sme = premik(int(za), x, y, sme)
            seznam.append((x, y, sme))

    return seznam

def opisi_stanje(x,y,smer):

    if smer == "N":
        return "{:>3}:{:<3} ^".format(x, y)
    elif smer == "E":
        return "{:>3}:{:<3} >".format(x, y)
    elif smer == "S":
        return "{:>3}:{:<3} v".format(x, y)
    elif smer == "W":
        return "{:>3}:{:<3} <".format(x, y)

def prevedi(ime_vhoda, ime_izhoda):

    datoteka = open(ime_izhoda, "w")

    for x,y,smer in izvedi(ime_vhoda):
        datoteka.write(opisi_stanje(x,y,smer)+"\n")



    datoteka.close()


