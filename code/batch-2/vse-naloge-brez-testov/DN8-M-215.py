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
    seznam = [(0,0,"N")]
    x = 0
    y = 0
    sm = "N"
    datoteka = open(ime_datoteke)
    for vrstice in datoteka.read().splitlines():
        if ' ' in vrstice:
            ukaz = int(vrstice.split()[1])
            rez = premik(ukaz,y,x,sm)
            seznam.append(rez)
            x = rez[1]
            y = rez[0]
        elif vrstice == "DESNO":
            seznam.append(premik("R",y,x,sm))
            sm = premik("R",y,x,sm)[2]
        elif vrstice == "LEVO":
            seznam.append(premik("L",y,x,sm))
            sm = premik("L",y,x,sm)[2]
    return seznam

def opisi_stanje(x,y,smer):
    if smer == "N":
        s = "^"
    elif smer == "E":
        s = ">"
    elif smer == "S":
        s = "v"
    else:
        s = "<"
    niz = "{:3}:{:<4}{}".format(x,y,s)
    return niz

def prevedi(ime_vhoda, ime_izhoda):
    rez = []
    seznam = izvedi(ime_vhoda)
    for x in seznam:
        x,y,sm = x[0],x[1],x[2]
        rez.append(opisi_stanje(x,y,sm))
    file = open(ime_izhoda, "w")
    for i in rez:
        file.write(i + '\n')
    file.close()




