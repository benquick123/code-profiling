#__________________________ NALOGA 9 ______________________________

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

#____________________________________________________________________

def izvedi(ime_datoteke):
    x, y = 0, 0
    s = 'N'
    pot = [(x, y, s)]
    for i in open(ime_datoteke):
        if i == "DESNO\n":
            x, y, s = premik("R",x, y, s)
            pot.append((x, y, s))
        elif i == "LEVO\n":
            x, y, s = premik("L", x, y, s)
            pot.append((x, y, s))
        elif i.split()[0] == "NAPREJ":
            stevilo = i.split()[1]
            x, y, s = premik(int(stevilo), x, y, s)
            pot.append((x, y, s))
    return pot

print(izvedi("primer.txt"))


def opisi_stanje(x,y,smer):
    smeri = {'N' : '^', 'E' : '>', 'S' : 'v', 'W' : '<'}

    sx = ' ' * (3-len(str(x))) + str(x)
    sy = str(y) + ' ' * (3 + 1 - len(str(y)))
    return (sx + ":" + sy + smeri[smer])

print(opisi_stanje(0, 12, "N"))


def prevedi(ime_vhoda, ime_izhoda):
    pot = izvedi(ime_vhoda)
    s = open(ime_izhoda, 'w')
    for i in pot:
        s.write(opisi_stanje(i[0], i[1], i[2]) + '\n')
    s.close()

def opisi_stanje_2(x, y, smer):
    smeri = {'N': '^', 'E': '>', 'S': 'v', 'W': '<'}
    sp = " " * (4 - len(str(x)))
    return (smeri[smer] + sp + "(" + str(x) + ":" + str(y) + ")")

print(opisi_stanje_2(0, 12, "N"))

#_________________________________________ TESTI  _________________________________________

