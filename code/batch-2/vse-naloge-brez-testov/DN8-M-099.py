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
    stanja = [(0,0,"N")]
    i = 0
    dat = open(ime_datoteke)
    for vrstica in dat:
        x, y, smer = stanja[i]
        if vrstica == "DESNO\n":
            stanja.append(premik("R", x, y, smer))

        elif vrstica == "LEVO\n":
            stanja.append(premik("L", x, y, smer))

        else:
            nap = vrstica.split()
            stanja.append(premik(int(nap[1]), x, y, smer))

        i += 1
    dat.close()
    return stanja

def opisi_stanje(x, y, smer):
    if smer == "N":
        return "{:>3}:{:<3} ^".format(x, y)
    elif smer == "S":
        return "{:>3}:{:<3} v".format(x, y)
    elif smer == "E":
        return "{:>3}:{:<3} >".format(x, y)
    else:
        return "{:>3}:{:<3} <".format(x, y)

def prevedi(ime_vhoda, ime_izhoda):
    izhod = open(ime_izhoda, "w")

    stanja = izvedi(ime_vhoda)
    for x, y, smer in stanja:
        izhod.write(opisi_stanje(x, y, smer) + "\n")

    izhod.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        return "^ {:>4}:{})".format("(" + str(x), y)
    elif smer == "S":
        return "v {:>4}:{})".format("(" + str(x), y)
    elif smer == "E":
        return "> {:>4}:{})".format("(" + str(x), y)
    else:
        return "< {:>4}:{})".format("(" + str(x), y)

