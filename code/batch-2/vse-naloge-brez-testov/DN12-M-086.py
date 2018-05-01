def preberi(ime_datoteke):
    dat = open(ime_datoteke, "r")
    slovar = {}
    stevec = 0

    for i in dat:
        kona = " ".join(i.split())

        sl = kona.rstrip().split(' ')
        rezultat = [int(k) for k in sl]
        min = sorted(rezultat)

        do_tega = rezultat[:min[0]]

        stevec = stevec + 1
        for e in do_tega:
            if e == min[0]:
                break
            else:
                rezultat.append(e)
                rezultat.remove(e)
        slovar[stevec] = rezultat
    dat.close()
    return slovar


def mozna_pot(pot, zemljevid):
    zad = len(pot) - 1
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[zad]]) == 1:
        for a, b in zip(pot, pot[1:]):
            if a not in zemljevid[b]:
                return False

        for i in pot[1:zad]:
            if len(zemljevid.get(i)) == 1:
                return False

        return True
    else:
        return False


def hamiltonova(pot, zemljevid):
    seznam = []
    zad = len(pot) - 1
    for a, b in zemljevid.items():
        if len(b) > 1:
            if a not in seznam:
                seznam.append(a)

    if mozna_pot(pot, zemljevid):
        if len(pot[1:zad]) == len(seznam) and set(pot[1:zad]) == set(seznam):
            return True
    else:
        return False


