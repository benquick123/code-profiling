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
    ukazi = [(0, 0, "N")]
    for line in open(ime_datoteke):
        s = line.split()[-1]
        if s == "DESNO":
            s = "R"
        elif s == "LEVO":
            s = "L"
        else:
            s = int(s)
        x, y, smer = ukazi[-1]
        ukazi.append((premik(s, x, y, smer)))
    return ukazi


def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "W":
        smer = "<"
    else:
        smer = "v"
    return "{:3}:{:<4}{}".format(x, y, smer)


def prevedi(ime_vhoda, ime_izhoda):
    f = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        f.write(opisi_stanje(x, y, smer) + "\n")


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "W":
        smer = "<"
    else:
        smer = "v"
    x = "(" + str(x)
    y = str(y) + ")"
    return "{}{:>5}:{}".format(smer, x, y)


