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
    kordinate = ([0, 0, 'N'])
    izpis = [(0, 0, 'N')]
    datoteka = open(ime_datoteke)
    for a in datoteka:
        e = (a.strip().split())
        if e[0] == "DESNO":
            kordinate = premik("R", int(kordinate[0]), int(kordinate[1]), kordinate[2])
        elif e[0] == "LEVO":
            kordinate = premik("L", int(kordinate[0]), int(kordinate[1]), kordinate[2])
        else:
            kordinate = premik(int(e[1]), int(kordinate[0]), int(kordinate[1]), kordinate[2])
        izpis.append(kordinate)
    return izpis

def opisi_stanje(x, y, smer):
    if smer == "N":
        return "{x:>3}:{y:<4}{smer}".format(x=x, y=y, smer="^")
    elif smer == "S":
        return "{x:>3}:{y:<4}{smer}".format(x=x, y=y, smer="v")
    if smer == "E":
        return "{x:>3}:{y:<4}{smer}".format(x=x, y=y, smer=">")
    if smer == "W":
        return "{x:>3}:{y:<4}{smer}".format(x=x, y=y, smer="<")

def prevedi(ime_vhoda, ime_izhoda):
    prva = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for e in prva:
        datoteka.write(opisi_stanje(e[0], e[1], e[2])+"\n")
    datoteka.close()



