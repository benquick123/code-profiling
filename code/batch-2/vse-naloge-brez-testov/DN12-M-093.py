def preberi(datoteka):
    d = dict()
    i = 1
    info = open(datoteka)
    for vrstica in info:
        vrstica = list(map(int, vrstica.strip().split()))
        while vrstica[0] != min(vrstica):
            vrstica.append(vrstica[0])
            del vrstica[0]
        d[i] = vrstica
        i += 1
    return d

def mozna_pot(pot, zemljevid):
    i = 1
    for x in pot:
        if i <= len(pot)-1:
            if (pot[i] in zemljevid[x]) and (zemljevid[pot[0]] == zemljevid[x] or len(zemljevid[x]) != 1):
                i += 1
                continue
            else:
                return False
        if len(zemljevid[x]) == 1 and len(zemljevid[pot[0]]) == 1:
            return True
        else:
            return False

def hamiltonova(pot, zemljevid):
    i = 0
    for x in zemljevid:
        if len(zemljevid[x]) == 1:
            i += 1
    if mozna_pot(pot, zemljevid) and len(pot) == len(zemljevid) - i + 2:
        for x in pot:
            if pot.count(x) == 1:
                continue
        return True
    return False

def navodila(pot, zemljevid):
    s = []
    a = 1
    for x in pot:
        d = zemljevid[x]
        b = 0
        if x == pot[0] or x == pot[-1]:
            vhod = x
            a += 1
            continue
        if a + 1 <= len(pot):
            i = d.index(vhod)
            while d[i] != pot[a]:
                d.append(d[0])
                del d[0]
                b += 1
            s.append(b)
            vhod = x
        a += 1
    return s

def rev_index(s, x):
    return - s[::-1].index(x) -1

def prevozi(zacetek, navodila, zemljevid):
    vhod, krozisce = zacetek, zemljevid[zacetek][0]
    s = [zacetek, krozisce]
    for izhod in navodila:
        a = 0
        d = zemljevid[krozisce]
        b = d.index(vhod)
        while a != izhod:
            d.append(d[0])
            del d[0]
            a += 1
        s.append(d[b])
        vhod, krozisce = krozisce, d[b]
    return s

def sosedi(doslej, zemljevid):
    s = set()
    for x in doslej:
        d = zemljevid[x]
        for a in d:
            if a not in doslej:
                s.add(a)
    return s

def razdalja(x, y, zemljevid):
    a = 1
    s = {x}
    while y not in sosedi(s, zemljevid):
        s = s | sosedi(s, zemljevid)
        a += 1
    return a

def najkrajsa_navodila(x, y, zemljevid):
    s = [[x] + list(sosedi({x}, zemljevid))]
    for a in s:
        if y in a:
            return navodila(a, zemljevid)
        else:
            for b in list(sosedi(set(a), zemljevid)):
                s.append(a + [b])
    return None

#================================ TESTI ================================#
