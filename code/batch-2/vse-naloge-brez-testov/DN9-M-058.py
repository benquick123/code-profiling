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
    izvedeni_ukazi = [(0, 0, "N")]
    x = 0
    y = 0
    smer = "N"
    for vrstica in open(ime_datoteke):
        ukaz = vrstica.split()
        if ukaz[0] == "DESNO" or ukaz[0] == "LEVO":
            if (smer == "W" and ukaz[0] == "DESNO") or (smer == "E" and ukaz[0] == "LEVO"):
                smer = "N"
            elif (smer == "N" and ukaz[0] == "DESNO") or (smer == "S" and ukaz[0] == "LEVO"):
                smer = "E"
            elif (smer == "E" and ukaz[0] == "DESNO") or (smer == "W" and ukaz[0] == "LEVO"):
                smer = "S"
            elif (smer == "S" and ukaz[0] == "DESNO") or (smer == "N" and ukaz[0] == "LEVO"):
                smer = "W"
        elif ukaz[0] == "NAPREJ":
            if smer == "N":
                y -= int(ukaz[1])
            elif smer == "E":
                x += int(ukaz[1])
            elif smer == "S":
                y += int(ukaz[1])
            else:
                x -= int(ukaz[1])
        else:
            if smer == "N":
                y += int(ukaz[1])
            elif smer == "E":
                x -= int(ukaz[1])
            elif smer == "S":
                y -= int(ukaz[1])
            else:
                x += int(ukaz[1])
        izvedeni_ukazi.append((x, y, smer))
    return izvedeni_ukazi

def opisi_stanje(x, y, smer):
    if smer == "N":
        znak = "^"
    elif smer == "E":
        znak = ">"
    elif smer == "S":
        znak = "v"
    else:
        znak = "<"
    return "{:>3}:{:<3} {}".format(x, y, znak)

def prevedi(ukazi, stanja):
    datoteka = open(stanja, "w")
    izvedeni_ukazi = izvedi(ukazi)
    for x, y, smer in izvedeni_ukazi:
        datoteka.write((opisi_stanje(x, y, smer)))
        datoteka.write("\n")
    datoteka.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        znak = "^"
    elif smer == "E":
        znak = ">"
    elif smer == "S":
        znak = "v"
    else:
        znak = "<"
    koordinata = "(" + str(x)
    return "{} {:>4}:{})".format(znak, koordinata, y,)


