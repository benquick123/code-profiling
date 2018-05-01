

def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    slovar = {}
    i = 1
    for vrstica in datoteka:
        stevila = []
        for x in vrstica.split():
            stevila.append(int(x))
        index = stevila.index(min(stevila))
        s = stevila[index:] + stevila[:index]
        slovar[i] = s
        i += 1
    return slovar


def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) > 1:
        return False
    if len(zemljevid[pot[len(pot) - 1]]) > 1:
        return False

    for i in range(1, len(pot) - 1):
        if len(zemljevid[pot[i]]) == 1:
            return False

    for i in range(len(pot) - 1):
        x = pot[i]
        new_x = pot[i + 1]
        stevila = zemljevid[x]
        if new_x not in stevila:
            return False
    return True


def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False;

    temp = []
    for x in pot:
        if x in temp:
            return False
        else:
            temp.append(x)

    krizisca = 0
    for i, stevila in zemljevid.items():
        if len(stevila) > 1:
            krizisca += 1

    if len(temp) - 2 == krizisca:
        return True
    else:
        return False

def navodila(pot, zemljevid):
    seznam = []
    for i in range(1, len(pot) - 1):
        curr = pot[i]
        prev = pot[i - 1]
        next = pot[i + 1]

        stevila = zemljevid[curr]
        prev_i = stevila.index(prev)
        next_i = stevila.index(next)
        index = (next_i - prev_i) % len(stevila)
        seznam.append(index)
    return seznam


def prevozi(zacetek, navodila, zemljevid):
    krozisca = [zacetek, zemljevid[zacetek][0]]
    for index in navodila:
        curr = krozisca[len(krozisca) - 1]
        prev = krozisca[len(krozisca) - 2]

        stevila = zemljevid[curr]
        prev_i = stevila.index(prev)
        next_i = (index + prev_i) % len(stevila)

        next = stevila[next_i]
        krozisca.append(next)
    return krozisca


def sosedi(doslej, zemljevid):
    m = set()
    for x in doslej:
        stevila = zemljevid[x]
        for s in stevila:
            if s not in doslej:
                m.add(s)
    return m


def razdalja(x, y, zemljevid):
    m = set()
    m.add(x)
    i = 1
    while (True):
        m = sosedi(m, zemljevid)
        if y in m:
            return i
        i += 1
    return 0

