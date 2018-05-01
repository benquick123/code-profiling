def izvedi(ime_datoteke):
    dat = open(ime_datoteke)
    sled = [(0, 0, "N")]

    for vrstica in dat:
        podatki = vrstica.split()
        if podatki[0] == "DESNO":
            ukaz = "R"
        elif podatki[0] == "LEVO":
            ukaz = "L"
        else:
            ukaz = int(podatki[1])
        sled.append(premik(ukaz, sled[-1][0], sled[-1][1], sled[-1][2]))

    return sled

def opisi_stanje(x, y, smer):
    if smer == "N":
        s = "^"
    elif smer == "E":
        s = ">"
    elif smer == "S":
        s = "v"
    else:
        s = "<"
    return "{:>3}:{:<3} {}".format(x, y, s)

def prevedi(ime_vhoda, ime_izhoda):
    zzz = izvedi(ime_vhoda)
    pisi = open(ime_izhoda, "w")
    for x, y, smer in zzz:
        pisi.write(opisi_stanje(x, y, smer)+"\n")
    pisi.close()

#----------------------------------------------------------------------------------
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


