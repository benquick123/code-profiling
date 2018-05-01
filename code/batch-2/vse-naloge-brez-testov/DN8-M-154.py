def izvedi(ime_datoteke):
    x = 0
    y = 0
    smer = 'N'
    D = open(ime_datoteke)
    S =[(0,0,'N')]
    for u in D:
        u = u.split()
        if u[0] == 'DESNO':
            ukaz = 'R'
        elif u[0] == 'LEVO':
            ukaz = 'L'
        elif u[0] == 'NAPREJ':
            ukaz = int(u[1])
        S.append(premik(ukaz,x,y,smer))
        (x,y,smer) = (premik(ukaz,x,y,smer))
    return S

def opisi_stanje(x, y, smer):
    if smer == 'N':
        s = '^'
    elif smer =='E':
        s = '>'
    elif smer == 'S':
        s = 'v'
    elif smer == 'W':
        s = '<'
    return '{:>3}:{:<3} {}'.format(x,y,s)


def prevedi(ime_vhoda, ime_izhoda):
    i = open(ime_izhoda, 'w')
    for x,y,smer in izvedi(ime_vhoda):
        i.write(opisi_stanje(x,y,smer)+'\n')

def opisi_stanje_2(x, y, smer):
    if smer == 'N':
        s = '^'
    elif smer =='E':
        s = '>'
    elif smer == 'S':
        s = 'v'
    elif smer == 'W':
        s = '<'
    x = '({}'.format(x)
    return '{} {:>4}:{})'.format(s,x,y)

def premik(ukaz, x, y, smer):
    smeri = 'NESW'
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == 'R':
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == 'L':
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer


