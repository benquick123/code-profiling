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
    seznam = [(0, 0, 'N')]
    x0, y0 = 0, 0
    smer = 'N'

    for vrstica in open(ime_datoteke, encoding='utf8'):
        if vrstica[0]== 'N':
            x0, y0, smer = premik(int(vrstica[7:]), x0, y0, smer)
        elif vrstica[0] == 'D':
            x0, y0, smer = premik('R', x0, y0, smer)
        elif vrstica[0] == 'L':
            x0, y0, smer = premik('L', x0, y0, smer)
        seznam.append((x0, y0, smer))
    return seznam

def opisi_stanje(x, y, smer):
    if smer == 'N':
        tmp = '^'
    elif smer == 'E':
        tmp = '>'
    elif smer == 'S':
        tmp = 'v'
    elif smer == 'W':
        tmp = '<'
    return ('{0:3d}:{1:<3d} {2:1s}'.format(x, y, tmp))

def prevedi(ime_vhoda, ime_izhoda):
    seznam = izvedi(ime_vhoda)
    file = open(ime_izhoda, "w")
    for stanje in seznam:
        file.write(opisi_stanje(stanje[0], stanje[1], stanje[2]) + '\n')

    file.close()

def opisi_stanje_2(x, y, smer):
    if smer == 'N':
        tmp = '^'
    elif smer == 'E':
        tmp = '>'
    elif smer == 'S':
        tmp = 'v'
    elif smer == 'W':
        tmp = '<'
    return ('{0:1s}{1:>5s}:{2:d})'.format(tmp, '('+str(x), y))



