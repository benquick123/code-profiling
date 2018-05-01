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
    seznam = []
    x = 0
    y = 0
    smer = 'N'
    datoteka = open(ime_datoteke)
    for ukaz in datoteka:
        slecen = ukaz.strip('\n')
        if (0, 0, 'N') not in seznam:
            seznam.append((0, 0, 'N'))
        if slecen[0:7:1] == 'NAPREJ ':
            spremeni = ukaz.lstrip('NAPREJ ')
            posli = spremeni.rstrip('\n')
            i = int(posli)
            x, y, smer = premik(i, x, y, smer)
        if 'DESNO' == slecen:
            spremeni = ukaz.replace('DESNO', 'R')
            posli = spremeni.rstrip('\n')
            x, y, smer = premik(posli, x, y, smer)
        if 'LEVO' == slecen:
            spremeni = ukaz.replace('LEVO', 'L')
            posli = spremeni.rstrip('\n')
            x, y, smer = premik(posli, x, y, smer)
        seznam.append((x, y, smer))
    datoteka.close()
    return seznam

def opisi_stanje(x, y, smer):
    if smer == 'N':
        smer = '^'
    if smer == 'E':
        smer = '>'
    if smer == 'S':
        smer = 'v'
    if smer == 'W':
        smer = '<'
    vrni = '{:3}:{:<3} {:1}'.format(x,y,smer)
    return vrni

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, 'w')
    for x, y, smer in izvedi(ime_vhoda):
        datoteka.write(opisi_stanje(x, y, smer) + '\n')
    datoteka.close()




