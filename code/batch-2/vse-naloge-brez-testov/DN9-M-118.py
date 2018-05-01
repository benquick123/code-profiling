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
    datoteka = open(ime_datoteke).readlines()
    x = 0
    y = 0
    smer = 'N'
    vsiPremiki = [(0, 0, 'N')]
    
    for vrstica in datoteka:
        if 'DESNO' in vrstica:
            ukaz = 'R'
        elif 'LEVO' in vrstica:
            ukaz = 'L'
        elif 'NAPREJ' in vrstica:
            for crka in vrstica:
                if crka.isalpha():
                    vrstica = vrstica.replace(crka, '', 1)
            ukaz = int(vrstica)
        rezultat = premik(ukaz, x, y, smer)
        x = rezultat[0]
        y = rezultat[1]
        smer = rezultat[2]
        
        vsiPremiki.append(rezultat)

    return vsiPremiki


def opisi_stanje(x, y, smer):
    if smer == 'N':
        puscica = '^'
    elif smer == 'E':
        puscica = '>'
    elif smer == 'S':
        puscica = 'v'
    else:
        puscica = '<'

    return '{:>3}:{:<4}{}'.format(x, y, puscica)


def prevedi(ime_vhoda, ime_izhoda):
    vhod = izvedi(ime_vhoda)
    izhod = open(ime_izhoda, 'w')
    for _ in vhod:
        x = _[0]
        y = _[1]
        smer = _[2]
        izhod.write(opisi_stanje(x, y, smer) + '\n')
    


def opisi_stanje_2(x, y, smer):
    if smer == 'N':
        puscica = '^'
    elif smer == 'E':
        puscica = '>'
    elif smer == 'S':
        puscica = 'v'
    else:
        puscica = '<'
    temp = '{:>4}:{:<4}'.format(x, y)
    for index, value in enumerate(temp):
        if value.isalnum() or value == '-':
            break
    temp = temp[0:index] + '(' + temp[index:-1].rstrip() + ')'
    return '{}{}'.format(puscica, temp)


    
