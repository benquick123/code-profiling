def preberi(ime_datoteke):
    slovar = {}
    a = open(ime_datoteke)
    b = a.read().splitlines()
    ada = []

    for i in b:
        d = i.split(" ")
        niz = []
        for a in d:
            ab = int(a)
            niz.append(ab)
        ada.append(niz)
    stevec = 1
    for c in ada:
        while c[0] is not min(c):
            a = c.pop(0)
            c.append(a)
        slovar[stevec] = c
        stevec += 1
    print(slovar)
    return slovar


def mozna_pot(pot, zemljevid):
    start = pot[0]
    cilj = pot[-1]
    if len(zemljevid[start]) == 1 and len(zemljevid[cilj]) == 1:
        for x, y in zip(pot, pot[1:]):
            if x not in zemljevid[y]:
                return False
        for i in pot[1:-1]:
            if len(zemljevid[i]) == 1:
                return False
        return True
    else:
        return False

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid):
        for i in zemljevid:
            if len(zemljevid[i]) > 1:
                if pot.count(i) != 1:
                    return False
        return True

    else:
        return False












