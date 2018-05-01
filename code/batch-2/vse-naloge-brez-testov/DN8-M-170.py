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
    x, y, smer = 0, 0, 'N'
    dat = open(ime_datoteke, 'r')
    stanja = [(x, y, smer)]
    for vrstica in dat:
        if vrstica.strip() == "DESNO":
            ukaz = "R"
        elif vrstica.strip() == "LEVO":
            ukaz = "L"
        else:
            ukaz = int(str.split(vrstica.strip())[1])
        x, y, smer = premik(ukaz, x, y, smer)
        stanja.append((x, y, smer))
    dat.close()
    return stanja

def opisi_stanje(x, y, smer):
    znaki = {'N' : '^', 'E' : '>', 'S' : 'v', 'W' : '<'}
    return "{:>3}:{:<3} {:}".format(x, y, znaki[smer])

def prevedi(ime_vhoda, ime_izhoda):
    dat1 = open(ime_vhoda, 'r')
    dat2 = open(ime_izhoda, 'w')
    ukazi = izvedi(ime_vhoda)
    for x,y ,smer in ukazi:
        dat2.write(opisi_stanje(x, y, smer) + '\n')
    dat1.close()
    dat2.close()
    return None

def opisi_stanje_2(x, y, smer):
    znaki = {'N' : '^', 'E' : '>', 'S' : 'v', 'W' : '<'}
    return "{:2}{:>4}:{:<}".format(znaki[smer], '(' + str(x), str(y) +')')

