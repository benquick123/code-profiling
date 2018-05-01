def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "DESNO":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "LEVO":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer

def izvedi(ime_datoteke):
    smeri = "NESW"
    for smer in smeri:
        ismer = smeri.index(smer)
    x, y, smer = 0, 0, "N"
    a = []
    a.append((x, y, smer))
    b = open(ime_datoteke).read().split()
    for c in b:
        if c == "NAPREJ":
            continue
        if c == "DESNO":
            ukaz = c
        if c == "LEVO":
            ukaz = c
        elif c.isdigit():
            ukaz = int(c)
        a.append(premik(ukaz, x, y, smer))
        x, y, smer = premik(ukaz, x, y, smer)
    return a

def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    if smer == "E":
        smer = ">"
    if smer == "S":
        smer = "v"
    if smer == "W":
        smer = "<"
    return "{:3}:{:<4}{:}".format(x, y, smer)

def prevedi(ime_vhoda, ime_izhoda):
    a = []
    l = izvedi(ime_vhoda)
    k = []
    for x, y, smer in l:
        k.append(opisi_stanje(x, y, smer))
    z = open(ime_izhoda, "wt", encoding="utf-8")
    for e in k:
        z.write("{}\n".format(e))

