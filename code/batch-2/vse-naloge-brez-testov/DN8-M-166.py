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
    datoteka = open(ime_datoteke, "r")
    s = [(0, 0, "N")]
    i = -1
    for vrstica in datoteka:
        i += 1
        x = s[i][0]
        y = s[i][1]
        smer = s[i][2]
        if vrstica[0] == "D":
            ukaz = "R"
        elif vrstica[0] == "L":
            ukaz = "L"
        else:
            ukaz = int((vrstica.strip().split(" "))[1])
        s.append(premik(ukaz, x, y, smer))
    return s



def opisi_stanje(x, y, smer):
    if smer == "N":
        z = "^"
    if smer == "S":
        z = "v"
    if smer == "W":
        z = "<"
    if smer == "E":
        z = ">"
    return ("{x:>3}:{y:<4}{z}".format(x=x, y=y, z=z))


def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    for navodilo in izvedi(ime_vhoda):
        datoteka.write(opisi_stanje(navodilo[0], navodilo[1], navodilo[2]))
        datoteka.write("\n")
    datoteka.close()


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        z = "^"
    if smer == "S":
        z = "v"
    if smer == "W":
        z = "<"
    if smer == "E":
        z = ">"
    return ("{z}{x:>5}:{y})".format(x="(" + str(x), y=y, z=z))



