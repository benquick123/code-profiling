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
    x = 0
    y = 0
    smer = "N"
    tab = [(x, y, smer)]
    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        if "DESNO" in vrstica.split()[0]:
            x, y, smer = premik("R", x, y, smer)
        elif "LEVO" in vrstica.split()[0]:
            x, y, smer = premik("L", x, y, smer)
        else:
            x, y, smer = premik(int(vrstica.split()[1]), x, y, smer)
        tab.append((x, y, smer))
    return tab


def opisi_stanje(x, y, smer):
    smeri = "NESW"
    znaki = "^>v<"
    return "{x:>3}:{y:<3} {znaki}".format(x=x, y=y, znaki=znaki[smeri.index(smer)])


def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    for ukaz in izvedi(ime_vhoda):
        tmp = opisi_stanje(ukaz[0], ukaz[1], ukaz[2])
        datoteka.write("{blabla}\n".format(blabla=tmp))


def opisi_stanje_2(x, y, smer):
    smeri = "NESW"
    znaki = "^>v<"
    return "{znaki} {x:>4}:{y})".format(x="("+str(x), y=y, znaki=znaki[smeri.index(smer)])


