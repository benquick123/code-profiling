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
    x, y, smer = 0, 0, 'N'
    stanje = [(0, 0, 'N')]
    for ukaz in datoteka:
        if ukaz == 'DESNO\n':
            x, y, smer = premik('R', x, y, smer)
        elif ukaz == 'LEVO\n':
            x, y, smer = premik('L', x, y, smer)
        else:
            cifra = int(ukaz.replace('NAPREJ ', ''))
            x, y, smer = premik(cifra, x, y, smer)
        stanje.append((x, y, smer))
    print(stanje)
    return stanje

def opisi_stanje(x, y, smer):
    stL = 3 - len(str(x))
    stD = 3 - len(str(y))
    LP = ''
    DP = ''
    for i in range(stL):
        LP = LP + ' '
    for i in range(stD):
        DP = DP + ' '
    if smer == 'N':
        smer2 = '^'
    elif smer == 'S':
        smer2 = 'v'
    elif smer == 'W':
        smer2 = '<'
    elif smer == 'E':
        smer2 = '>'
    return LP + str(x) + ':' + str(y) + DP + ' ' + smer2

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_vhoda, 'r')
    stanja = izvedi(ime_vhoda)
    print(stanja)
    for i in range(len(stanja)):
        stanja[i] = opisi_stanje(stanja[i][0], stanja[i][1], stanja[i][2])
    F = open(ime_izhoda, 'w')
    for stvar in stanja:
        F.write(str(stvar) + '\n')

prevedi('ukazi.txt', 'stanja.txt')


