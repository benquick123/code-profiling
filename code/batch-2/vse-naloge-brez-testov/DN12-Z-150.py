def preberi(ime_datoteke):
    mapa = {}
    i = 1
    for line in open(ime_datoteke):
        line = line.strip().split()
        mapa[i] = sortiraj(line)
        i += 1
    return mapa


def sortiraj(krozisce):
    krozisce = list(map(int, krozisce))
    najnizji = krozisce[0]
    for element in krozisce:
        if element < najnizji:
            najnizji = element

    for element in krozisce:
        if element != najnizji:
            krozisce.append(krozisce[0])
            krozisce = krozisce[1:]
        else:
            break

    return krozisce


def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) > 1:
        return False
    if len(zemljevid[pot[len(pot) - 1]]) > 1:
        return False
    for i in range(0, len(pot) - 1):
        if not veljavna_poteza(pot[i], pot[i + 1], zemljevid):
            return False
    for element in pot[1:-1]:
        if len(zemljevid[element]) == 1:
            return False
    return True


def veljavna_poteza(prva, druga, zemljevid):
    if (druga in zemljevid[prva]):
        return True
    else:
        return False


def stevilo_krozisc(zemljevid):
    i = 0
    for element in zemljevid:
        if len(zemljevid[element]) > 1:
            i += 1
    return i


def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid):
        if stevilo_krozisc(zemljevid) + 2 == len(pot):
            return True
    else:
        return False


