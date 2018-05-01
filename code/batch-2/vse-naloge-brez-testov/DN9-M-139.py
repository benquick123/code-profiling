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
    ukazi = [(0, 0, "N")]
    tre_ukaz = (0, 0, "N")

    dat = open(ime_datoteke)
    vrstice = dat.readlines()
    dat.close()

    for vrstica in vrstice:

        vrstica = vrstica.strip()

        if vrstica == "DESNO":
            nov_ukaz = premik("R", tre_ukaz[0], tre_ukaz[1], tre_ukaz[2])
            ukazi.append(nov_ukaz)
            tre_ukaz = nov_ukaz
            continue

        elif vrstica == "LEVO":
            nov_ukaz = premik("L", tre_ukaz[0], tre_ukaz[1], tre_ukaz[2])
            ukazi.append(nov_ukaz)
            tre_ukaz = nov_ukaz
            continue

        else:
            ukaz = vrstica.split()
            nov_ukaz = premik(int(ukaz[1]), tre_ukaz[0], tre_ukaz[1], tre_ukaz[2])
            ukazi.append(nov_ukaz)
            tre_ukaz = nov_ukaz
            continue

    return ukazi


def opisi_stanje(x, y, smer):
    if smer == "N":
        smer_puscica = "^"

    elif smer == "E":
        smer_puscica = ">"

    elif smer == "S":
        smer_puscica = "v"

    else:
        smer_puscica = "<"

    izpis = "{:>3}:{:<3} {}".format(x, y, smer_puscica)

    return izpis


def prevedi(ime_vhoda, ime_izhoda):
    osnovna_pot = izvedi(ime_vhoda)
    koncna_pot = []

    for korak in osnovna_pot:
        koncna_pot.append(opisi_stanje(korak[0], korak[1], korak[2]))

    pisanje = open(ime_izhoda, "w")

    for korak in koncna_pot:
        pisanje.write(korak)
        pisanje.write("\n")

    pisanje.close()


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smer_puscica = "^"

    elif smer == "E":
        smer_puscica = ">"

    elif smer == "S":
        smer_puscica = "v"

    else:
        smer_puscica = "<"

    str_x = "(" + str(x)

    izpis = "{} {:>4}:{})".format(smer_puscica, str_x, y)

    return izpis


