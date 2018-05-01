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

def ukaz_v_anglescino(slovenski_ukaz):
    if slovenski_ukaz == "DESNO":
        return "R"
    elif slovenski_ukaz == "LEVO":
        return "L"

def izvedi(ime_datoteke):
    x = 0
    y = 0
    smer = "N"
    seznam = [(x, y, smer)]

    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        ukaz_slo = vrstica.split()[0]

        if ukaz_slo != "NAPREJ":
            ukaz = ukaz_v_anglescino(ukaz_slo)
        else:
            ukaz = int(vrstica.split()[1])

        x, y, smer = premik(ukaz, x, y, smer)
        seznam.append((x, y, smer))
    datoteka.close()
    return seznam

def opisi_stanje(x, y, smer):
    znak = "^>v<"["NESW".index(smer)]
    return "{:>3}:{:<3} {}".format(x, y, znak)

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        datoteka.write(opisi_stanje(x, y, smer) + "\n")
    datoteka.close()

def opisi_stanje_2(x, y, smer):
    znak = "^>v<"["NESW".index(smer)]
    return "{} {:>4}:{})".format(znak, "(" + str(x), y)


