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
    t = open(ime_datoteke).read()
    t = t.split()
    terka = (0, 0, "N")
    seznam = [(0, 0, "N")]
    for e in t:
        if e == "DESNO":
            terka = premik("R", terka[0], terka[1], terka[2])
            seznam.append(terka)
        elif e == "NAPREJ":
            continue
        elif e == "LEVO":
            terka = premik("L", terka[0], terka[1], terka[2])
            seznam.append(terka)
        else:
            terka = premik(int(e), terka[0], terka[1], terka[2])
            seznam.append(terka)
    return seznam

def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer = "<"
    return  "{:>3}:{:<3} {}".format(x, y, smer)

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda,"w",  encoding = "utf-8")
    for x, y, smer in izvedi(ime_vhoda):
        datoteka.write("{}\n".format(opisi_stanje(x, y, smer)))
    datoteka.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer = "<"
    d = len(str(x))
    s = 4 - d
    return  "{} {:>{}}{:>}:{:<}{}".format(smer,"(", s, x, y, ")")


