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

def smer(ukaz):
    if ukaz == "DESNO":
        return 'R'
    elif ukaz == "LEVO":
        return 'L'
    else:
        return int(ukaz)

def izvedi(ime_datoteke):
    s = [(0, 0, 'N')]
    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        vrstica = tuple(vrstica.split())
        s.append(premik(smer(vrstica[-1]), s[-1][0], s[-1][1], s[-1][2]))
    return s

def opisi_stanje(x, y, smer):
    d = {'N':'^', 'E':'>', 'S':'v', 'W':'<'}
    return "{:>3}:{:<4}{:<}".format(x, y, d[smer])

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, 'w')
    for e in izvedi(ime_vhoda):
        datoteka.write(opisi_stanje(*e) + '\n')

def opisi_stanje_2(x, y, smer):
    d = {'N':'^', 'E':'>', 'S':'v', 'W':'<'}
    return "{:<}{:>}".format(d[smer], ' '*(4 - len(str(x))) + '(' + str(x) + ":" + str(y) + ')' )

