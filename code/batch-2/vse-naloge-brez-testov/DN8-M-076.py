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
    f = open(ime_datoteke)
    polozaji = [(0, 0, 'N')]
    for line in f:
        line = line.replace("\n", "")
        line = line.split(" ")
        if line[0] == "DESNO":
            x, y, smer = polozaji[-1]
            x, y, smer = premik("R", x, y, smer)
            polozaji.append((x, y, smer))
        if line[0] == "LEVO":
            x, y, smer = polozaji[-1]
            x, y, smer = premik("L", x, y, smer)
            polozaji.append((x, y, smer))
        if line[0] == "NAPREJ":
            x, y, smer = polozaji[-1]
            x, y, smer = premik(int(line[1]), x, y, smer)
            polozaji.append((x, y, smer))
    f.close()
    return polozaji

def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    if smer == "W":
        smer = "<"
    if smer == "S":
        smer = "v"
    if smer == "E":
        smer = ">"
    return "{:>3}:{:<3} {}".format(x, y, smer)

def prevedi(ime_vhoda, ime_izhoda):
    izhod = open(ime_izhoda, "w")
    sez = izvedi(ime_vhoda)
    for x, y, smer in sez:
        izhod.write(opisi_stanje(x, y, smer) + "\n")
    izhod.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smer = "^"
    if smer == "W":
        smer = "<"
    if smer == "S":
        smer = "v"
    if smer == "E":
        smer = ">"
    return "{}{:>5}:{})".format(smer, "(" + str(x), y)


