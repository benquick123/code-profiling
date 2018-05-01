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
    x = 0
    y = 0
    smer = "N"
    seznamterk = [(0,0, "N")]
    for vrstica in datoteka:
        if vrstica.split()[0] == "DESNO":
            ukaz = "R"
        elif vrstica.split() [0] == "LEVO":
            ukaz = "L"
        else:
            ukaz = int(vrstica.split()[1])
        polozaj = premik(ukaz, x, y, smer)
        seznamterk.append(polozaj)
        x = polozaj [0]
        y = polozaj [1]
        smer = polozaj [2]
    return seznamterk

def opisi_stanje(x,y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "S":
        smer ="v"
    elif smer == "W":
        smer = "<"
    elif smer == "E":
        smer = ">"
    return "{x:>3}:{y:<3} {smer}".format(x=x, y=y, smer = smer)

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        datoteka.write("{}\n".format(opisi_stanje(x,y,smer)))

def opisi_stanje_2(x, y, smer):
    dolzina = len(str(x))
    razlika = 4 - dolzina
    if smer == "N":
        smer = "^"
    elif smer == "S":
        smer ="v"
    elif smer == "W":
        smer = "<"
    elif smer == "E":
        smer = ">"
    return '{}{:>5}:{}'.format(smer, "("+  str(x), str(y) + ")")


