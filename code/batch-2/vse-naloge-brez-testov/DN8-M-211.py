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
    x = y = 0
    n = "N"
    s = [(0, 0, "N")]
    d = open(ime_datoteke)
    for vrstica in d:
        vrstica = vrstica.strip()
        v = vrstica.split()
        if len(v) == 1:
            if v[0] == "DESNO":
                x, y, n = premik("R", x, y, n)
            elif v[0] == "LEVO":
                x, y, n = premik("L", x, y, n)
        elif len(v) == 2:
            x, y, n = premik(int(v[1]), x, y, n)
        s.append((x, y, n))
    return s


def opisi_stanje(x, y, smer):
    if smer == "N":
        s = "^"
    elif smer == "S":
        s = "v"
    elif smer == "E":
        s = ">"
    elif smer == "W":
        s = "<"
    return "{x:3}:{y:<3} {s}".format(x=x, y=y, s=s)


def prevedi(ime_vhoda, ime_izhoda):
    s = izvedi(ime_vhoda)
    o = open(ime_izhoda, "w")
    for x, y, smer in s:
        o.write(opisi_stanje(x, y, smer)+"\n")


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        s = "^"
    elif smer == "S":
        s = "v"
    elif smer == "E":
        s = ">"
    elif smer == "W":
        s = "<"
    return "{s} {x:>4}:{y:}".format(x="("+str(x), y=str(y)+")", s=s)


