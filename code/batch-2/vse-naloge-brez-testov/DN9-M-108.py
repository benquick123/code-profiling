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

    seznam = [(0, 0, "N")]
    x, y = 0, 0
    smer = "N"

    for vrstica in open(ime_datoteke):
        if vrstica[0] == "D":
            x, y, smer = premik("R", x, y, smer)
            seznam.append((x, y , smer))

        elif vrstica[0] == "L":
            x, y, smer = premik("L", x, y, smer)
            seznam.append((x, y, smer))

        else:
            ukaz = int(vrstica.split(" ")[1])
            x, y, smer = premik(ukaz, x, y, smer)
            seznam.append((x, y, smer))

    return seznam

def opisi_stanje(x, y, smer):
    smeri = "NESW"
    znaki = "^>v<"
    ismeri = smeri.index(smer)

    return "{:>3}:{:<3} {}".format(x, y, znaki[ismeri])

def prevedi(ime_vhoda, ime_izhoda):

    datoteka_izhod = open(ime_izhoda, "w")

    seznam = izvedi(ime_vhoda)

    for x, y, smer in seznam:
        datoteka_izhod.write(opisi_stanje(x, y, smer)+"\n")


    datoteka_izhod.close()

def opisi_stanje_2(x, y, smer):
    smeri = "NESW"
    znaki = "^>v<"
    ismeri = smeri.index(smer)


    return "{} {:>4}:{})".format(znaki[ismeri], "(" + str(x), y)



