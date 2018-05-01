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
    a = [(0, 0, 'N')]
    x = 0
    y = 0
    smer = "N"
    counter = 1
    for ukaz in ukazi:
        if ukaz.strip() == "DESNO":
            ukaz = "R"
        elif ukaz.strip() =="LEVO":
            ukaz = "L"
        else:
            ukaz = int(ukaz.strip().split()[1])
        a.append(premik(ukaz, x, y, smer))
        x = a[counter][0]
        y = a[counter][1]
        smer = a[counter][2]
        counter += 1
    ukazi.close()
    return a

def opisi_stanje(x, y, smer):
    if smer  == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer = "<"

    return "{:>3}:{:<3} {}".format(x, y, smer)

def prevedi(ime_vhoda, ime_izhoda):
    ukazi = izvedi(ime_vhoda)
    izhod = open(ime_izhoda, "w")
    for ukaz in ukazi:
        g = opisi_stanje(ukaz[0], ukaz[1], ukaz[2])
        izhod.write(g + "\n")
    izhod.close()

def opisi_stanje_2(x, y, smer):
    if smer  == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer = "<"

    x = "(" + str(x)
    return "{}{:>5}:{})".format(smer, x, y)

