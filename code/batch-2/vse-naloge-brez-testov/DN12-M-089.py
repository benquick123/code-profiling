def preberi(ime_datoteke):
    neo = []
    krozisce = {}
    datoteka = open(ime_datoteke, 'r')
    b = datoteka.read().splitlines()
    datoteka.close()
    for item in b:
        c = item.split(" ")
        ne = []
        for i in c:
            ne.append(int(i))
        neo.append(ne)
    for u in neo:
        while u[0] != min(u):
            last = u[-1]
            del u[-1]
            u.insert(0, last)
        for key, u in zip(range(1, len(neo) + 1), neo):
            krozisce[key] = u
    return krozisce

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1:
        if pot[0] in zemljevid[pot[1]]:
            for last, kroz in zip(pot[1:], pot[2:]):
                if len(zemljevid[last]) == 1:
                    return False
                elif last not in zemljevid[kroz]:
                    return False
            return True

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid):
        for c in zemljevid:
            v = pot.count(c)
            if v != 1:
                if len(zemljevid[c]) != 1:
                    return False
        return True
    else:
        return False

def navodila(pot, zemljevid):
    sez = []
    for last, kroz, next in zip(pot[0:], pot[1:], pot[2:]):
        z = (zemljevid[kroz].index(next) - zemljevid[kroz].index(last)) % len(zemljevid[kroz])
        sez.append(z)
    return sez





