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
    a = open(ime_datoteke)
    seznam = [(0, 0, "N")]
    smer = "N"
    x, y = 0, 0
    for vrstica in a:
        if vrstica[0] == "D":
            ukaz = "R"
            seznam.append(premik(ukaz, x, y, smer))
            b = premik(ukaz, x, y, smer)
            smer = b[2]
            x = b[0]
            y = b[1]
        if vrstica[0] == "L":
            ukaz = "L"
            seznam.append(premik(ukaz, x, y, smer))
            b = premik(ukaz, x, y, smer)
            smer = b[2]
            x = b[0]
            y = b[1]
        if vrstica[0] == "N":
            ukaz = int(vrstica[7:])
            seznam.append(premik(ukaz, x, y, smer))
            b = premik(ukaz, x, y, smer)
            smer = b[2]
            x = b[0]
            y = b[1]

    return seznam

def opisi_stanje(x, y, smer):
    a = "{:>3}:{:<3} {}"
    if smer == "N":
        smer = "^"
    if smer == "S":
        smer = "v"
    if smer == "E":
        smer = ">"
    if smer == "W":
        smer = "<"
    return(a.format(x, y, smer))

def prevedi(ime_vhoda, ime_izhoda):
    a = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        a.write(opisi_stanje(x, y, smer),)
        a.write("\n")

