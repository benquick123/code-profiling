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
    smer = 'N'
    x = 0
    y = 0
    stanja = [(0, 0, 'N')]
    datoteka = open(ime_datoteke, encoding='utf-8')
    b = datoteka.read().splitlines()
    for ukaz in b:
        if ukaz == 'DESNO':
            raz = 'R'
        if ukaz == 'LEVO':
            raz = 'L'
        if ukaz.split(" ")[0] == "NAPREJ":
            dm = ukaz.split(" ")[1]
            raz = float(dm)
        c = premik(raz, x, y, smer)
        x = c[0]
        y = c[1]
        smer = c[2]
        stanja.append(c)
    return stanja

def opisi_stanje(x, y, smer):
    if smer == 'N':
        smer = '^'
    elif smer == 'E':
        smer = '>'
    elif smer == 'S':
        smer = 'v'
    elif smer == 'W':
        smer = '<'
    x = x
    y = y
    c = "{x:>3}:{y:<3}{s:>2}".format(s=smer, x=x, y=y)
    return c

def prevedi(ime_vhoda, ime_izhoda):
    b = izvedi(ime_vhoda)
    ime_izhoda = open(ime_izhoda, "w")
    for tocka in b:
        x = tocka[0]
        y = tocka[1]
        smer = tocka[2]
        c = opisi_stanje(int(x), int(y), smer)
        d = c[8]
        z = "{x:>3.0f}:{y:<3.0f}{d:>2}".format(x=x, y=y, d=d)
        ime_izhoda.write(z + '\n')
    ime_izhoda.close()

def opisi_stanje_2(x, y, smer):
    z = opisi_stanje(x, y, smer)
    h = "{:<2}{:>4}:{:<0}".format(z[8], '('+str(x), str(y)+')')
    return h


