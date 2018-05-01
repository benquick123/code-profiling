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
    s = [( 0, 0, 'N')]
    for vrstica in open(ime_datoteke, 'r', encoding='UTF8' ).read().splitlines():
        if vrstica[0] == 'L' or vrstica[0] == 'D':
            ukaz = 'R' if vrstica[0] == 'D' else 'L'
        else:
            ukaz = int(vrstica[7:])
        x, y, smer = premik(ukaz, x, y, smer)
        s.append((x, y, smer))
    return s

def opisi_stanje(x, y, smer):
    return '{:>3}:{:<3} {s}'.format(x, y, s='^' if smer == 'N' else '>' if smer == 'E' else 'v' if smer == 'S' else '<')

def prevedi(ime_vhoda, ime_izhoda):
    s = izvedi(ime_vhoda)
    f = open(ime_izhoda, 'w', encoding='UTF8')
    for x, y, smer in s:
        f.write(opisi_stanje(x, y, smer) + '\n')
    f.close()

def opisi_stanje_2(x, y, smer):
    return '{s} {a:>4}{b}'.format(a='(' + str(x), b= ':' + str(y) +')',
                                  s='^' if smer == 'N' else '>' if smer == 'E' else 'v' if smer == 'S' else '<')
























