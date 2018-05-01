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
    ukazi = open(ime_datoteke)
    x, y = 0, 0
    smer = "N"
    s = []
    s.append((x,y,smer))
    for ukaz in ukazi:
        if len(ukaz.split()) > 1:
            x, y, smer = premik(int(ukaz.split()[1]), x, y, smer)
            s.append((x, y, smer))
        if ukaz.strip() == "DESNO":
            x, y, smer = premik("R", x, y, smer)
            s.append((x, y, smer))
        elif ukaz.strip() == "LEVO":
            x, y, smer = premik("L", x, y, smer)
            s.append((x, y, smer))
    return s

def opisi_stanje(x, y, smer):
    sme = "NESW"
    sm = sme.index(smer)
    s = "^>v<"
    return "{:>3}:{:<4}{}".format(x, y, s[sm])

def prevedi(ime_vhoda, ime_izhoda):
    polja = izvedi(ime_vhoda)
    stanja = open(ime_izhoda, "w")
    for x, y, smer in polja:
        stanja.write(opisi_stanje(x, y, smer) + "\n")

def opisi_stanje_2(x, y, smer):
    sme = "NESW"
    sm = sme.index(smer)
    s = "^>v<"
    return "{:<2}{:>4}:{}".format(s[sm], ("(" + str(x)), (str(y) + ")"))


