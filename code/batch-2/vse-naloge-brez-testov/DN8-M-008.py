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
    seznam = [(x, y, smer)]
    i = 1
    datoteka = open(ime_datoteke, encoding="UTF-8")
    for vrstica in datoteka:
        vrstica = vrstica.rstrip("\n")
        if vrstica == "DESNO":
            ukaz = "R"
        elif vrstica == "LEVO":
            ukaz = "L"
        else:
            vrstica = vrstica.split()
            ukaz = int(vrstica[1])
        seznam.append((premik(ukaz, x, y, smer)))
        x = seznam[i][0]
        y = seznam[i][1]
        smer = seznam[i][2]
        i = i + 1
    return seznam

def opisi_stanje(x, y, smer):
    if smer == "N":
        znak = "^"
    elif smer == "E":
        znak = ">"
    elif smer == "S":
        znak = "v"
    else:
        znak = "<"
    return("{:>3}:{:<3} {}".format(x, y, znak))

def prevedi(ime_vhoda, ime_izhoda):
    zapis = open(ime_izhoda, "w", encoding="UTF-8")
    seznam = izvedi(ime_vhoda)
    for x, y, smer in seznam:
        zapis.write(opisi_stanje(x, y, smer) + "\n")
    zapis.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        znak = "^"
    elif smer == "E":
        znak = ">"
    elif smer == "S":
        znak = "v"
    else:
        znak = "<"

    x = str(x)
    y = str(y)

    return("{} {:>4}:{:<2}".format(znak, ("(" + x), (y + ")")))


