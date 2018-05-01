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
    d = open(ime_datoteke)
    x = 0
    y = 0
    smer = 'N'
    poz = [(x, y, smer)]
    for navodilo in d:
        if navodilo.strip() == 'DESNO':
            x, y, smer = premik('R', x, y, smer)
        elif navodilo.strip() == 'LEVO':
            x, y, smer = premik('L', x, y, smer)
        else:
            x, y, smer = premik(int(navodilo.split()[1]), x, y, smer)
        poz.append((x, y, smer))
    return poz

def opisi_stanje(x, y, smer):
    if smer == 'N':
        return('{:3}:{:<3} {}').format(x, y, '^')
    elif smer == 'S':
        return ('{:3}:{:<3} {}').format(x, y, 'v')
    elif smer == 'W':
        return ('{:3}:{:<3} {}').format(x, y, '<')
    else:
        return ('{:3}:{:<3} {}').format(x, y, '>')

def prevedi(ime_vhoda, ime_izhoda):
    d = open(ime_izhoda, "w")
    for vrstica in izvedi(ime_vhoda):
        s = opisi_stanje(vrstica[0], vrstica[1], vrstica[2]) #(*vrstica)
        d.write(s + '\n')
    d.close()

    def opisi_stanje_2(x, y, smer):
        if smer == 'N':
            return ('({}:{:<3}) {:<3}').format('^', x, y)
        elif smer == 'S':
            return ('{:3}:{:<3} {}').format('v' ,x, y)
        elif smer == 'W':
            return ('{:3}:{:<3} {}').format('<', x, y,)
        else:
            return ('{:3}:{:<3} {}').format('>', x, y,)


