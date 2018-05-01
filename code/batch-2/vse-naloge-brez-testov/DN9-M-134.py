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
        sez = [(0, 0, "N")]
        datoteka = open(ime_datoteke, "r")
        tekst = datoteka.readlines()
        for vsebina in tekst:
            vsebina = vsebina.strip()
            if "DESNO" in vsebina:
                pozicija = premik("R", x, y, smer)
                x, y, smer = pozicija
                sez.append((x, y, smer))
            elif "LEVO" in vsebina:
                pozicija = premik("L", x, y, smer)
                x, y, smer = pozicija
                sez.append((x, y, smer))
            elif "NAPREJ" in vsebina:
                neki = (vsebina.split(" "))
                pozicija = premik(int(neki[1]), x, y, smer)
                x, y, smer = pozicija
                sez.append((x, y, smer))
        datoteka.close()
        return sez


def opisi_stanje(x, y, smer):
    spremenjenaSmer = ""
    if smer == 'N':
        spremenjenaSmer = '^'
    elif smer == 'E':
        spremenjenaSmer = '>'
    elif smer == 'S':
        spremenjenaSmer = 'v'
    elif smer == 'W':
        spremenjenaSmer = '<'
    return ("{:>3}:{:<4}{}".format(str(x), str(y), spremenjenaSmer))


def prevedi(ime_vhoda, ime_izhoda):
    seznam = izvedi(ime_vhoda)
    with open(ime_izhoda, 'w') as datoteka:
        for x, y, smer in seznam:
            datoteka.write(opisi_stanje(x, y, smer) + '\n')
    datoteka.close()


