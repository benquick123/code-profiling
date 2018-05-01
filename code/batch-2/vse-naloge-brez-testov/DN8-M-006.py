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
    y = x = 0
    smer = "N"
    seznam = []
    seznam.append((0, 0, 'N'))
    ukazi = []
    for ukaz in open(ime_datoteke):
        ukaz = ukaz.strip()
        # print(ukaz)
        if ukaz == 'DESNO':
            ukazi.append("R")
        elif ukaz == 'LEVO':
            ukazi.append("L")
        else:
            ukazi.append(int(ukaz.split()[1]))

    for ukaz in ukazi:
        terka = premik(ukaz, x, y, smer)
        seznam.append(terka)
        x, y, smer = terka
    return seznam

def opisi_stanje(x, y, smer):
    if smer == "N":
        s = "^"
    elif smer == "E":
        s = ">"
    elif smer == "S":
        s = "v"
    elif smer == "W":
        s = "<"
    return ("{:>3}:{:<3} {}".format(x, y, s))

def prevedi(ime_vhoda, ime_izhoda):
    izhod = open(ime_izhoda, "w")

    seznam = izvedi(ime_vhoda)

    for el in seznam:
        x, y, smer = el
        izhod.write(opisi_stanje(x, y, smer) + "\n")
    izhod.close()

def opisi_stanje_2(x ,y, smer):
    if smer == "N":
        s = "^"
    elif smer == "E":
        s = ">"
    elif smer == "S":
        s = "v"
    elif smer == "W":
        s = "<"
    return ("{:6{}({:3}:{})".format(s, x, y))




