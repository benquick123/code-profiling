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
    pot = [(0, 0, "N")]
    ukazi = open(ime_datoteke)
    for ukaz in ukazi:
        a = pot[len(pot)-1]
        if  ukaz.startswith("D"):
            pot.append(premik("R", a[0], a[1], a[2]))
        elif ukaz.startswith("L"):
            pot.append(premik("L", a[0], a[1], a[2]))
        else:
            naravnost = int(ukaz.split()[1])
            pot.append(premik(naravnost, a[0], a[1], a[2]))
    ukazi.close()
    return pot

def opisi_stanje(x, y, smer):
    kompas = "NESW"
    puscice = "^>v<"
    pravapuscica = puscice[kompas.index(smer)]
    while len(str(x)) < 3:
        x = " " + str(x)
    while len(str(y)) < 3:
        y = str(y) + " "
    return(str(x) + ":" + str(y) + " " + pravapuscica)

def prevedi(ime_vhoda, ime_izhoda):
    seznam = izvedi(ime_vhoda)
    izhod = open(ime_izhoda, "w")
    for ukaz in seznam:
        izhod.write(opisi_stanje(ukaz[0], ukaz[1], ukaz[2])+"\n")
    izhod.close()

def opisi_stanje_2(x, y, smer):
    kompas = "NESW"
    puscice = "^>v<"
    pravapuscica = puscice[kompas.index(smer)]
    x = "(" + str(x)
    while len(str(x)) < 5:
        x = " " + x
    return(pravapuscica + str(x) + ":" + str(y) + ")")

