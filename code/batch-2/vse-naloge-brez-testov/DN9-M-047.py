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
    komande = []
    x0      = 0
    y0      = 0
    smer    = 'N'
    pot     = [(x0, y0, smer)]

    with open(ime_datoteke) as datoteka:
        lista = datoteka.readlines()
    for i in lista:
        komande.append(i.strip())

    for komanda in komande:
        if komanda == 'DESNO':
            tmp  = premik('R', x0, y0, smer)
            x0   = tmp[0]
            y0   = tmp[1]
            smer = tmp[2]
            pot.append(tmp)
        elif komanda == 'LEVO':
            tmp  = premik('L', x0, y0, smer)
            x0   = tmp[0]
            y0   = tmp[1]
            smer = tmp[2]
            pot.append(tmp)
        else:
            podkomanda = komanda.split(' ')
            tmp  = premik(int(podkomanda[1]), x0, y0, smer)
            x0   = tmp[0]
            y0   = tmp[1]
            smer = tmp[2]
            pot.append(tmp)

    return pot

def opisi_stanje(x, y, smer):
    if smer == 'N':
        znak = '^'
    elif smer == 'E':
        znak = '>'
    elif smer == 'W':
        znak = '<'
    else:
        znak = 'v'

    format = '{0:>%d}:{1:<%d} {2:>%d}' % (3, 3, 1)

    return format.format(x, y, znak)

def prevedi(ime_vhoda, ime_izhoda):
    komande = izvedi(ime_vhoda)

    file = open(ime_izhoda, 'w')
    for komanda in komande:
        vrstica = opisi_stanje(komanda[0], komanda[1], komanda[2])
        file.write(vrstica + '\n')

    file.close()

def opisi_stanje_2(x, y, smer):
    if smer == 'N':
        znak = '^'
    elif smer == 'E':
        znak = '>'
    elif smer == 'W':
        znak = '<'
    else:
        znak = 'v'

    format = '{0:<%d} {1:>%s}:{2:<%s}' % (1, 4, 1)

    return format.format(znak, '(' + str(x), str(y) + ')')

