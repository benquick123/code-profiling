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
    datoteka = open(ime_datoteke)

    robot = (0, 0, 'N')
    stanja = []
    stanja.append(robot)

    for vrstica in datoteka:
        if vrstica == "LEVO\n":
            ukaz = "L"
        elif vrstica == "DESNO\n":
            ukaz = "R"
        else:
            ukaz = int(vrstica.split()[1])
        robot = premik(ukaz, robot[0], robot[1], robot[2])
        stanja.append(robot)

    datoteka.close()
    return stanja


def opisi_stanje(x, y, smer):
    smeri = "^>v<"
    if smer == "N":
        nova_smer = "^"
    elif smer == "E":
        nova_smer = ">"
    elif smer == "S":
        nova_smer = "v"
    else:
        nova_smer = "<"
    return "{:>3}:{:<3} {}".format(x, y, nova_smer)


def prevedi(ime_vhoda, ime_izhoda):
    stanja = izvedi(ime_vhoda)
    izhod = open(ime_izhoda, "w+")
    for stanje in stanja:
        niz = opisi_stanje(stanje[0], stanje[1], stanje[2])
        izhod.write(niz + "\n")

    izhod.close()


def opisi_stanje_2(x, y, smer):
    smeri = "^>v<"
    if smer == "N":
        nova_smer = "^"
    elif smer == "E":
        nova_smer = ">"
    elif smer == "S":
        nova_smer = "v"
    else:
        nova_smer = "<"

    niz_x = "(" + str(x)
    niz_x = niz_x.rjust(5)
    return "{}{}:{})".format(nova_smer, niz_x, y)

