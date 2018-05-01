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
    t = [(0, 0, 'N'), ]
    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        i = vrstica.strip()
        if i == "DESNO":
            smer = 'R'
        elif i == "LEVO":
            smer = 'L'
        else:
            smer = int(i.split(" ")[1])
        t.append(premik(smer, t[len(t) - 1][0], t[len(t) - 1][1], t[len(t) - 1][2]))
    return t


def opisi_stanje(x, y, smer):
    if smer == 'N':
        z = '^'
    elif smer == 'E':
        z = '>'
    elif smer == 'S':
        z = 'v'
    else:
        z = '<'

    return "{x:>3}:{y:<3} {z:}".format(x=x, y=y, z=z)


def prevedi(ime_vhoda, ime_izhoda):
    c = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for i in c:
        datoteka.write(opisi_stanje(i[0], i[1], i[2]) + "\n")


