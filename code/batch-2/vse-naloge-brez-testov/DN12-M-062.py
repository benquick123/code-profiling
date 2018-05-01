def preberi(data):
    from itertools import cycle
    a = open(data).read().split("\n")
    b = dict([])
    y = 1
    for x in a:
        x = x.split()
        o = len(x)
        if not x:
            break
        d = [int(c) for c in x]
        d.extend(d)
        d = d[d.index(min(d)):]
        d = d[:o]
        b[y] = d
        y += 1
    return b


def mozna_pot(pot,zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1:
        return False
    mesto = pot[0]
    for x in pot[1:-1]:
        if len(zemljevid[x]) == 1:
            return False
        if mesto not in zemljevid[x]:
            return False
        mesto = x
    if not pot[1:-1]:
            return False
    return True


def hamiltonova(pot,zemljevid):
    if mozna_pot(pot,zemljevid):
        y=2
        for x in zemljevid:
            if len(zemljevid[x]) > 1:
                y += 1
        if len(pot) != y:
            return False
        for x in pot:
            if pot.count(x) != 1:
                return False
        return True
    else:
        return False


def navodila(pot,zemljevid):
    navodila_r = []
    while pot:
        vhod = pot.pop(0)
        if len(pot) == 1:
            return navodila_r
        krozisce = zemljevid[pot[0]]
        dolzina_krozisca = len(krozisce)
        krozisce.extend(krozisce)
        krozisce = krozisce[krozisce.index(vhod):]
        krozisce = krozisce[:dolzina_krozisca]
        navodila_r.append(krozisce.index(pot[1]))


def prevozi(začetek, navodila, zemljevid):
    prevozi_r = [začetek]
    a = zemljevid[začetek]
    prevozi_r.append(a[0])
    for smer in navodila:
        krozisce = zemljevid[prevozi_r[-1]]
        dolzina_krozisca = len(krozisce)
        krozisce.extend(krozisce)
        krozisce = krozisce[krozisce.index(prevozi_r[-2]):]
        krozisce = krozisce[:dolzina_krozisca]
        prevozi_r.append(krozisce[smer])
    return prevozi_r








