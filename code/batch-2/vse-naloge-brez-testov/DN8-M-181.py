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
    datoteka = open(ime_datoteke)
    x, y = 0, 0
    sm = "N"
    s = [(x, y, sm)]
    for ukaz in datoteka:
        if ukaz[0] == "D":
            p = premik("R", x, y, sm)
            s.append(p)
            x = p[0]
            y = p[1]
            sm = p[2]
        elif ukaz[0] == "L":
            p = premik("L", x, y, sm)
            s.append(p)
            x = p[0]
            y = p[1]
            sm = p[2]
        else:
            st = int(ukaz.split()[1])
            p = premik(st, x, y, sm)
            s.append(p)
            x = p[0]
            y = p[1]
            sm = p[2]
    return s


def opisi_stanje(x, y, smer):
    if smer == "N":
        znak = '^'
    elif smer == "E":
        znak = '>'
    elif smer == "W":
        znak = '<'
    else:
        znak = 'v'
    return("{x:>3}:{y:<3} {znak}".format(y=y, x=x, znak=znak))



def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    s = izvedi(ime_vhoda)
    for ukaz in s:
        bla = opisi_stanje(ukaz[0], ukaz[1], ukaz[2])
        datoteka.write("{}\n".format(bla))
    datoteka.close()


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        znak = '^'
    elif smer == "E":
        znak = '>'
    elif smer == "W":
        znak = '<'
    else:
        znak = 'v'
    oklepaj = "({x}".format(x=x)
    return ("{znak} {x:>4}:{y})".format(y=y, x=oklepaj, znak=znak))



