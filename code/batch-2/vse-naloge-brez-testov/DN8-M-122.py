def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "DESNO\n":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "LEVO\n":
        smer = smeri[(ismer - 1) % 4]
    else:
        ukaz = int((ukaz.split(" ")[1]))
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer

def izvedi(ime_datoteke):
    seznam = []
    x = 0
    y = 0
    smer = "N"

    seznam.append((x, y, smer))
    for vrstica in open(ime_datoteke):
        trojka = premik(vrstica, x, y, smer)
        x = trojka[0]
        y = trojka[1]
        smer = trojka[2]
        seznam.append((x, y, smer))
    return seznam

def opisi_stanje(x, y, smer):

    if smer == "N":
        arrow = "^"
    if smer == "E":
        arrow = ">"
    if smer == "S":
        arrow = "v"
    if smer == "W":
        arrow = "<"

    s = "{:>3}:{:<4}{}"
    return s.format(x, y, arrow)

def prevedi(ime_vhoda, ime_izhoda):

    seznam = izvedi(ime_vhoda)
    izhod = open(ime_izhoda, "w")
    for x, y, smer in seznam:
        s = opisi_stanje(x, y, smer)
        izhod.write("{}\n".format(s))
    izhod.close()

def opisi_stanje_2(x, y, smer):

    if smer == "N":
        arrow = "^"
    if smer == "E":
        arrow = ">"
    if smer == "S":
        arrow = "v"
    if smer == "W":
        arrow = "<"

    koorX = "({}".format(x)
    koorY = "{})".format(y)

    s = "{}{:>5}:{}"
    return s.format(arrow, koorX, koorY)


