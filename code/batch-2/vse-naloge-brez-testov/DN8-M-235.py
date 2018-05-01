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

def izvedi(ime):
    datoteka = open(ime)
    x, y = 0, 0
    smer = "N"
    seznam = []
    seznam.append((x, y, smer))
    for vrstica in datoteka:
        vrstica = vrstica.strip()
        if vrstica == "LEVO":
            x, y, smer = premik("L", x, y, smer)
        if vrstica == "DESNO":
            x, y, smer = premik("R", x, y, smer)
        if ' ' in vrstica:
            neki = vrstica.split(' ')
            x, y, smer = premik(int(neki[1]), x, y, smer)
        seznam.append((x, y, smer))
    datoteka.close()
    return(seznam)


def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer = "<"
    return("{x:>3}:{y:<4}{smer:1}".format(x=x, y=y, smer=smer))

def prevedi(ime_vhoda, ime_izhoda):
    seznam = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for ena in seznam:
        x,y,smer=ena
        pisi=opisi_stanje(x,y,smer)
        datoteka.write(("{}{}".format(pisi, "\n")))
    datoteka.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer = "<"
    i=5
    i = i - len(str(x))
    return("{smer:<{i}}({x}:{y})".format(i=i,x=x, y=y, smer=smer))

