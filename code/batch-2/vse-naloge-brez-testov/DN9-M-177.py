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
    smer = "N"
    seznam_premikov = [(0, 0, "N")]
    x = 0
    y = 0
    ukazi = open(ime_datoteke, encoding="utf-8")
    for vrstica in ukazi:
        ukaz = vrstica.strip().split(" ")
        if ukaz[0] == "DESNO":
            jojo = "R"
            ukaz.append(0)
            x += ukaz[1]
        if ukaz[0] == "LEVO":
            jojo = "L"
            ukaz.append(0)
            y += ukaz[1]
        if ukaz[0] == "NAPREJ":
            jojo = int(ukaz[1])
        premiki = premik(jojo, x, y, smer)
        x = premiki[0]
        y = premiki[1]
        smer = premiki[2]
        seznam_premikov.append(premiki)
    return seznam_premikov

def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer = "<"
    return ("{x:>3}:{y:<4}{smer}".format(x=x, y=y, smer=smer))

def prevedi(ime_vhoda, ime_izhoda):
    nova_dat = open(ime_izhoda, "w")
    izveden = izvedi(ime_vhoda)
    for iz in izveden:
        x, y, smer = iz
        opis = opisi_stanje(x, y, smer)
        nova_dat.write(opis+"\n")

def opisi_stanje_2(x, y, smer):
    x = "(" + str(x)
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer = "<"
    return ("{smer}{x:>5}:{y})".format(x=x, y=y, smer=smer))



