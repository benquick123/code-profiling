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
    s = [(0, 0, 'N')]
    for u in open(ime_datoteke):
        if u.strip() == "DESNO":
            s.append(premik('R', s[-1][0], s[-1][1], s[-1][2]))
        elif u.strip() == "LEVO":
            s.append(premik('L', s[-1][0], s[-1][1], s[-1][2]))
        else:
            s.append(premik(int(u.split()[1]), s[-1][0], s[-1][1], s[-1][2]))
    return s


def opisi_stanje(x, y, smer):
    if smer == 'N':
        return "{:>3}:{:<3} {}".format(x, y, "^")
    elif smer == 'E':
        return "{:>3}:{:<3} {}".format(x, y, ">")
    elif smer == 'S':
        return "{:>3}:{:<3} {}".format(x, y, "v")
    else:
        return "{:>3}:{:<3} {}".format(x, y, "<")


def prevedi(ime_vhoda, ime_izhoda):
    nov_file = open(ime_izhoda, 'w')
    for x, y, smer in izvedi(ime_vhoda):
        nov_file.write(opisi_stanje(x, y, smer)+"\n")
    nov_file.close()



def opisi_stanje_2(x, y, smer):
    return "{} {x:>4}:{y})".format(opisi_stanje(x, y, smer)[-1], x="("+str(x), y=y)




