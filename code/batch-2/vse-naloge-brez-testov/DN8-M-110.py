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

#########################################
#            POMOŽNA FUNKCIJA           #
#########################################

def prevedi_smer(smer):
    """
    Vrni smer v obliki:
    ^, >, v, < za smeri
    N, E, S, W

    Args:
        smer (string): smer v obliki N, E, S, W

    Returns:
        string: smer v obliki ^, >, v, <
    """
    if smer == 'N':
        return '^'
    elif smer == 'E':
        return '>'
    elif smer == 'S':
        return 'v'
    else:
        return '<'

#########################################
#                OBVEZNE                #
#########################################

def izvedi(ime_datoteke):
    file = open(ime_datoteke)
    datoteka = file.read().splitlines()
    x = 0
    y = 0
    smer = 'N'
    s = [(x, y, smer)]
    for ukaz in datoteka:
        if ukaz == 'DESNO':
            ukaz = 'R'
        elif ukaz == 'LEVO':
            ukaz = 'L'
        else:
            ukaz = int(ukaz.split()[1])
        x, y, smer = premik(ukaz, x, y, smer)
        s.append((x, y, smer))
    file.close()
    return s

def opisi_stanje(x, y, smer):
    smer = prevedi_smer(smer)
    return "{:>3}:{:<3} {}".format(x, y, smer)

def prevedi(ime_vhoda, ime_izhoda):
    stanja = izvedi(ime_vhoda)
    pisanje = open(ime_izhoda, 'w')
    for x, y, smer in stanja:
        pisanje.write(opisi_stanje(x, y, smer) + "\n")
    pisanje.close()

#########################################
#                DODATNA                #
#########################################

def opisi_stanje_2(x, y, smer):
    smer = prevedi_smer(smer)
    x_oklepaj = "({}".format(x)
    return "{} {:>4}:{})".format(smer, x_oklepaj, y)

#########################################
#                 TESTI                 #
#########################################

