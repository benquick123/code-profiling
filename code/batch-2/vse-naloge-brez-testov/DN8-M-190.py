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
    file = open(ime_datoteke)
    t = []
    t.append((0, 0, 'N'))
    i = 0
    for vrstica in file:
        e = vrstica.split()
        if e[0] == 'DESNO':
            ukaz = 'R'
        elif e[0] == 'LEVO':
            ukaz = 'L'
        else:
            ukaz = int(e[1])
        t.append(premik(ukaz, t[i][0], t[i][1], t[i][2]))
        i += 1
    file.close()
    return t

def opisi_stanje(x, y, smer):
    tsmer = {'N': '^', 'E': '>', 'S': 'v', 'W': '<'}
    str = '{:3}:{:<3}{:>2}'.format(x, y, tsmer[smer])
    return str

def prevedi(ime_vhoda, ime_izhoda):
    file = open(ime_izhoda, 'w')
    for x,y,smer in izvedi(ime_vhoda):
        file.write(opisi_stanje(x,y,smer) + '\n')
    file.close()

def opisi_stanje_2(x, y, smer):
    tsmer = {'N': '^', 'E': '>', 'S': 'v', 'W': '<'}
    x = '({}'.format(x)
    str = '{}{x:>5}:{y:})'.format(tsmer[smer], x=x, y=y)
    return str


