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
    s = []
    x = 0
    y = 0
    smer = "N"
    s.append((x, y, smer))
    for vrstica in open(ime_datoteke, encoding="utf-8"):
        vrstica = vrstica.strip()
        if vrstica == "DESNO":
            t = premik("R", x, y, smer)
        elif vrstica == "LEVO":
            t = premik("L", x, y, smer)
        else:
            t = premik(int(vrstica[7:]), x, y, smer)
        s.append(t)
        x = t[0]
        y = t[1]
        smer = t[2]
    return s


def opisi_stanje(x, y, smer):
    smeri = "NESW"
    znaki = "^>v<"
    ismer = smeri.index(smer)
    stanje = "{:>3}:{:<3} {}".format(x, y, znaki[ismer])
    return stanje


def prevedi(ime_vhoda, ime_izhoda):
    stanja = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for x, y, smer in stanja:
        stanje = opisi_stanje(x, y, smer)
        datoteka.write(stanje + "\n")


def opisi_stanje_2(x, y, smer):
    smeri = "NESW"
    znaki = "^>v<"
    ismer = smeri.index(smer)
    stanje = "{} {:>4}:{:})".format(znaki[ismer], "(" + str(x), y)
    return stanje

