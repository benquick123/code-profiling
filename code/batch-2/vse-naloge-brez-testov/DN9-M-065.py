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
    seznam = [(0, 0, 'N')]
    datoteka = open(ime_datoteke)

    for vrstica in datoteka:
        ukaz = vrstica.strip().split(' ')[-1]

        if ukaz.startswith('D'):
            seznam.append(premik('R', seznam[-1][0], seznam[-1][1], seznam[-1][2]))
        elif ukaz.startswith('L'):
            seznam.append(premik('L', seznam[-1][0], seznam[-1][1], seznam[-1][2]))
        else:
            seznam.append(premik(int(ukaz), seznam[-1][0], seznam[-1][1], seznam[-1][2]))

    datoteka.close()

    return seznam


def opisi_stanje(x, y, smer):
    smeri = {
        'N': '^',
        'E': '>',
        'S': 'v',
        'W': '<'
    }

    return '{0:>3d}:{1:<3d} {2}'.format(x, y, smeri[smer])


def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, 'w')
    izpis = ""

    for vrstica in izvedi(ime_vhoda):
        izpis += "{0}{1}".format(opisi_stanje(vrstica[0], vrstica[1], vrstica[2]), '\n')

    datoteka.write(izpis[:-1])

    datoteka.close()


def opisi_stanje_2(x, y, smer):
    smeri = {
        'N': '^',
        'E': '>',
        'S': 'v',
        'W': '<'
    }

    return '{0} {1:>4}:{2:d})'.format(smeri[smer], '(' + str(x), y)


