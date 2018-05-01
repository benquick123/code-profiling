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

def opredeli_smer(smer):
    nsmer = ""
    if smer == "N":
        nsmer = "^"
    if smer == "E":
        nsmer = ">"
    if smer == "W":
        nsmer = "<"
    if smer == "S":
        nsmer = "v"
    return nsmer

def izvedi(ime_datoteke):
    sez = []
    trenutna = (0, 0, 'N')
    sez.append(trenutna)

    dat = open(ime_datoteke)
    for vrstica in dat:
        ukaz = vrstica[:1]
        if ukaz == "D":
            ukaz = "R"
        if ukaz == "N":
            stevilka1 = vrstica.split(" ")
            stevilka = int(stevilka1[1].replace("\n", ""))
            # Za X smer
            if trenutna[2] == "W" or trenutna[2] == "E":
                trenutna = (premik(stevilka, trenutna[0], trenutna[1], trenutna[2]))
                sez.append(trenutna)
            # Za Y smer
            if trenutna[2] == "N" or trenutna[2] == "S":
                trenutna = (premik(stevilka, trenutna[0], trenutna[1], trenutna[2]))
                sez.append(trenutna)
        else:
            sez.append(premik(ukaz, trenutna[0], trenutna[1], trenutna[2]))
            trenutna = premik(ukaz, trenutna[0], trenutna[1], trenutna[2])
    dat.close()
    return sez

def opisi_stanje(x, y, smer):
    return ("{:3}:{:<4}{}".format(x, y, opredeli_smer(smer)))


def prevedi(ime_vhoda, ime_izhoda):
    izvedeno = izvedi(ime_vhoda)
    dat = open(ime_izhoda, "w")

    for trojka in izvedeno:
        x = trojka[0]
        y = trojka[1]
        smer = trojka[2]
        dat.write("{}\n".format(opisi_stanje(x, y, smer)))

    dat.close()



