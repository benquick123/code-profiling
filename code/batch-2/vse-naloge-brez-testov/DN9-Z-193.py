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


def prevod(ukaz):
    ukaz1 = ukaz.split()
    if ukaz1[0] == 'DESNO':
        ukaz2 = 'R'
    elif ukaz1[0] == 'LEVO':
        ukaz2 = 'L'
    elif ukaz1[0] == 'NAPREJ':
        ukaz2 = int(ukaz1[1])
    return ukaz2


def izvedi(ime_datoteke):
    dat = open(ime_datoteke)
    s = []
    e = (0, 0, 'N')
    s.append(e)
    for v in dat:
        dir = prevod(v)
        x = e[0]
        y = e[1]
        smer = e[2]
        e = premik(dir, x, y, smer)
        s.append(e)
    return s


def opisi_stanje(x,y,smer):
    s = {"N":"^", "S":"v", "W":"<", "E":">"}
    b = s[smer]
    return "{:>3}:{:<4}{:<}".format(x,y,b)


def prevedi(vhod, izhod):
    dat1 = izvedi(vhod)
    dat2 = open(izhod, "w")
    for e in dat1:
        dat2.write(opisi_stanje(*e) + "\n")








