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
    s = []
    x = 0
    y = 0
    smer = "N"
    klic = tuple()
    if (0, 0, "N") not in s:
        s.append((0, 0, "N"))
    datoteka = open(ime_datoteke)
    for ukaz in datoteka:
        ukaz = ukaz.strip()
        if ukaz == "DESNO":
            klic = premik("R", x, y, smer)
        if ukaz == "LEVO":
            klic = premik("L", x, y, smer)
        splitaj = ukaz.split()
        if splitaj[0] == "NAPREJ":
            st = int(splitaj[1])
            klic = premik(st, x, y, smer)
        x, y, smer = klic
        s.append((x, y, smer))
    datoteka.close()
    return s

def opisi_stanje(x, y, smer):
    if smer == "N":
        return "{:>3}:{:<4}^".format(x, y)
    if smer == "E":
        return "{:>3}:{:<4}>".format(x, y)
    if smer == "S":
        return "{:>3}:{:<4}v".format(x, y)
    if smer == "W":
        return "{:>3}:{:<4}<".format(x, y)

def prevedi(ime_vhoda, ime_izhoda):
    spr = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for e in spr:
        x, y, smer = e
        i = opisi_stanje(x, y, smer)
        datoteka.write(i)
        datoteka.write("\n")
    datoteka.close()





