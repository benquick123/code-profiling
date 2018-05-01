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
    seznam, orders = [], []
    orders.append((0,0,"N"))
    for vrstica in open(ime_datoteke, encoding='utf8'):
        this_line = vrstica.strip()
        seznam.append((this_line))

    stevec = 0

    for e in seznam:
        last_x, last_y, last_smer = orders[stevec][0], orders[stevec][1], orders[stevec][2]

        if e == 'DESNO':
            orders.append(premik('R', last_x, last_y, last_smer))
        elif e == "LEVO":
            orders.append(premik('L', last_x, last_y, last_smer))
        else:
            distance = int(e.split()[1])
            orders.append(premik(distance,last_x,last_y,last_smer))
        stevec+=1

    return orders

def opisi_stanje(x, y, smer):
    if smer == "N": smer = "^"
    elif smer == "E": smer = ">"
    elif smer == "S": smer = "v"
    elif smer == "W": smer = "<"

    return '{:>3}:{:<4}{}'.format(x, y, smer)

def opisi_stanje_2(x, y, smer):
    if smer == "N": smer = "^"
    elif smer == "E": smer = ">"
    elif smer == "S": smer = "v"
    elif smer == "W": smer = "<"
    x="("+str(x)

    return '{}{:>5}:{})'.format(smer, x, y)



def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    for (x,y,smer) in izvedi(ime_vhoda):
        datoteka.write(opisi_stanje(x,y,smer)+"\n")



