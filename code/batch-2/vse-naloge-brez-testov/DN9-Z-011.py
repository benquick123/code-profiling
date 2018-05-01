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
    x0, y0 = 0, 0
    zacetna_smer = "N"
    navodila = [(0, 0, zacetna_smer)]
    for ukaz in datoteka.readlines():
        ukaz = ukaz.rstrip()
        if ukaz == "DESNO":
            ukaz = "R"
        elif ukaz == "LEVO":
            ukaz = "L"
        else:
            ukaz = int(ukaz[6:])
        x1, y1, nova_smer = premik(ukaz, x0, y0, zacetna_smer)
        navodila.append((x1, y1, nova_smer))
        x0, y0 = x1, y1
        zacetna_smer = nova_smer
    return navodila

def opisi_stanje(x, y, smer):
    smeri = ("N", "E", "S", "W")
    zsmeri = ("^", ">", "v", "<")
    for s, znak in zip(smeri, zsmeri):
        if s == smer:
            return "{:>3}:{:<3} {}".format(x, y, znak)


def prevedi(ime_vhoda, ime_izhoda):
    datoteka = izvedi(ime_vhoda)
    nova = open(ime_izhoda, "w")
    for x, y, smer in datoteka:
        element = opisi_stanje(x, y, smer)
        nova.write(element+"\n")
    nova.close()


def opisi_stanje_2(x, y, smer):
    smeri = ("N", "E", "S", "W")
    zsmeri = ("^", ">", "v", "<")
    for s, znak in zip(smeri, zsmeri):
        if s == smer:
            return "{}{:>5}:{:<0})".format(znak, "("+str(x), y)

