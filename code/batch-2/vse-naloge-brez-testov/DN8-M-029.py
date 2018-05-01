
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

def izvedi(datoteka):
    l = []
    x = y = 0
    smer = "N"
    l.append((x, y, smer))
    for line in open(datoteka):
        if line == "DESNO\n":
            ukaz = "R"
        elif line == "LEVO\n":
            ukaz = "L"
        else:
            ukaz = int(line.split()[1])
        x, y, smer = premik(ukaz, x, y, smer)
        l.append((x, y, smer))
    return l

def opisi_stanje(x, y, smer):
    s = lambda smer: "^" if smer == "N" else (">" if smer == "E" else ("<" if smer == "W" else "v"))
    return "{:>3}:{:<3} {}".format(x, y, s(smer))

def prevedi(ime_vhoda, ime_izhoda):
    d = open(ime_izhoda, "w")
    l = izvedi(ime_vhoda)
    for x, y, smer in l:
        d.write(opisi_stanje(x, y, smer) + "\n")


def opisi_stanje_2(x, y, smer):
    s = lambda smer: "^" if smer == "N" else (">" if smer == "E" else ("<" if smer == "W" else "v"))
    return "".join(s(smer) + (" " * (4 - len(str(x)))) + "(" + str(x) + ":" + str(y) + ")")





