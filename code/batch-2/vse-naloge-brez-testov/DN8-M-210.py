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

    datoteka = open(ime_datoteke,"r")
    stanja = [(0,0,"N")]

    for vrstica in datoteka:

        ko1,ko2,smer = stanja[-1]

        ukaz = vrstica.strip()[0]

        if ukaz == "N":
            u = int(vrstica.split()[1])
        elif ukaz == "D":
            u = "R"
        else:
            u = "L"

        stanja.append(premik(u,ko1,ko2,smer))

    datoteka.close()
    return stanja

def opisi_stanje(x, y, smer):

    if smer == "N":
        s = "^"
    elif smer == "E":
        s = ">"
    elif smer == "S":
        s = "v"
    else:
        s  = "<"

    return "{:>3}:{:<3} {}".format(x,y,s)

def prevedi(ime_vhoda, ime_izhoda):

    stanja = izvedi(ime_vhoda)

    datoteka = open(ime_izhoda, "w")

    for ko1,ko2,smer in stanja:
        datoteka.write("{}\n".format(opisi_stanje(ko1,ko2,smer)))

    datoteka.close()

def opisi_stanje_2(x, y, smer):

    if smer == "N":
        s = "^"
    elif smer == "E":
        s = ">"
    elif smer == "S":
        s = "v"
    else:
        s = "<"

    return "{0}{1:{2}}({3}:{4})".format(s," ", 4-len(str(x)), x, y,)

