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

def izvedi(datoteka):
    datoteka = open(datoteka, "r")
    seznam = [(0,0,"N")]
    smer = "N"
    x, y = 0, 0
    i = 1
    for ukaz in datoteka:
        if ukaz.strip() == "DESNO":
            ukaz = "R"
        elif ukaz.strip() == "LEVO":
            ukaz = "L"
        else:
            ukaz = int(ukaz.split()[1].strip())
        seznam.append(premik(ukaz,x,y,smer))
        x = seznam[i][0]
        y = seznam[i][1]
        smer = seznam[i][2]
        i += 1
    return seznam

def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "S":
        smer = "v"
    elif smer == "E":
        smer = ">"
    elif smer == "W":
        smer = "<"
    return("{:>3}:{:<3} {}".format(x, y, smer))

def prevedi(ime_vhoda, ime_izhoda):
    izhod = open(ime_izhoda, "w")
    seznam = izvedi(ime_vhoda)
    for x, y, smer in seznam:
        izhod.write(opisi_stanje(x, y, smer) + "\n")
    izhod.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "S":
        smer = "v"
    elif smer == "E":
        smer = ">"
    elif smer == "W":
        smer = "<"
    dvopicje = ":"
    oklepaj = "("
    return("{}{:>4}{:<}{}{})".format(smer,oklepaj, x,dvopicje, y))



