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
    seznam = [(0, 0, "N")]
    d = 0
    n = "N"
    x, y = 0, 0
    a = open(ime_datoteke)
    b = a.read().splitlines()
    for i in b:
        if i == "DESNO":
            d = "R"

        if i == "LEVO":
            d = "L"
        if i.split(" ")[0] == "NAPREJ":
            d = int(i.split(" ")[1])


        l = premik(d, x, y, n)
        seznam.append(l)
        x = l[0]
        y = l[1]
        n = l[2]

    return seznam

def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer = "<"
    return ("{:>3}:{:<4}{}".format(x, y, smer))

def prevedi(ime_vhoda, ime_izhoda):
    enter = "\n"
    a = open(ime_izhoda, "w")
    b = izvedi(ime_vhoda)
    for i in b:
        x, y, smer = i
        a.write(opisi_stanje(x, y, smer)+enter)
    return


