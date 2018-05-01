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
    seznam = []
    smer = "N"
    x, y = 0, 0
    seznam += ([(x, y, smer)])
    for ukaz in datoteka:
        if ukaz == "DESNO\n":
            u = "R"
        elif ukaz == "LEVO\n":
            u = "L"
        else:
            stevilo = int(ukaz.split(" ")[1])
            u = stevilo
        x, y, smer = (premik(u, x, y, smer))
        seznam.append((x, y, smer))
    datoteka.close()
    return seznam


def opisi_stanje(x, y, smer):
    if smer == "N":
        return str("{:3}:{:<4}".format(x, y) + "^")
    elif smer == "S":
        return str("{:3}:{:<4}".format(x, y) + "v")
    elif smer == "E":
        return str("{:3}:{:<4}".format(x, y) + ">")
    elif smer == "W":
        return str("{:3}:{:<4}".format(x, y) + "<")

def prevedi(ime_vhoda, ime_izhoda):
    seznam = izvedi(ime_vhoda)
    file = open(ime_izhoda, "w")
    for x, y, smer in seznam:
        file.write(opisi_stanje(x, y, smer)+ "\n")
    file.close()
'''
def opisi_stanje_2(x, y, smer):
    if smer == "N":
        return str("{:3}:{:<4}".format(x, y) + "^")
    elif smer == "S":
        return str("{:3}:{:<4}".format(x, y) + "v")
    elif smer == "E":
        return str("{:3}:{:<4}".format(x, y) + ">")
    elif smer == "W":
        return str("{:3}:{:<4}".format(x, y) + "<")
'''

