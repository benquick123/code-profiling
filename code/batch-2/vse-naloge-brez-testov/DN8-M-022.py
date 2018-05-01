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
    ukazi = []
    for vrstica in open(ime_datoteke):
        if vrstica.strip() == "DESNO":
            ukazi.append("R")
        elif vrstica.strip() == "LEVO":
            ukazi.append("L")
        else:
            ukazi.append(int(vrstica.split()[-1]))
    stanja = [(0, 0, "N")]
    stanje = 0
    for ukaz in ukazi:
        stanja.append(premik(ukaz, stanja[stanje][0], stanja[stanje][1], stanja[stanje][2]))
        stanje += 1
    return stanja

def izpisi_stanje(x, y, znak):
    return "{0:>3}:{1:<4}{2}".format(x, y, znak)

def opisi_stanje(x, y, smer):
    if smer == "N":
        return izpisi_stanje(x, y, "^")
    elif smer == "S":
        return izpisi_stanje(x, y, "v")
    elif smer == "E":
        return izpisi_stanje(x, y, ">")
    else:
        return izpisi_stanje(x, y, "<")

def prevedi(ime_vhoda, ime_izhoda):
    nova_datoteka = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        nova_datoteka.write(opisi_stanje(x, y, smer) + "\n")

def izpisi_stanje_2(x, y, znak):
    return "{0}{1:>5}:{2})".format(znak, "(" + str(x), y)

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        return izpisi_stanje_2(x, y, "^")
    elif smer == "S":
        return izpisi_stanje_2(x, y, "v")
    elif smer == "E":
        return izpisi_stanje_2(x, y, ">")
    else:
        return izpisi_stanje_2(x, y, "<")


