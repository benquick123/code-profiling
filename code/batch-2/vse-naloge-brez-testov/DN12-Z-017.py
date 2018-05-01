import collections

def preberi(ime_datoteke):
    i = 1
    zemljevid = collections.defaultdict(list)
    for vrstica in open(ime_datoteke):
        for j in (vrstica.strip()).split(" "):
            zemljevid[i].append(int(j))
        m = zemljevid[i].index(min(zemljevid[i]))
        zemljevid[i] = (zemljevid[i])[m:] + (zemljevid[i])[:m]
        i += 1
    return zemljevid

def mozna_pot(pot, zemljevid):
    zacetek = []
    i = 1
    while i in zemljevid:
        if len(zemljevid[i]) == 1:
            zacetek.append(i)
        i += 1
    # se zacne/konca
    if pot[0] not in zacetek:
        return False
    if pot[-1] not in zacetek:
        return False
    # ni koncnih tock vmes
    for j in zacetek:
        if j in pot[1:-2]:
            return False
    x = 1
    #se krožišče ne ponovi
    while x < len(pot):
        if pot[x] == pot[x-1]:
            return False
        x += 1
    #povezava
    a = 1
    for y in pot:
        if a < len(pot):
            if pot[a] not in zemljevid[y]:
                return False
        a += 1
    return True

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid) == False:
        return False
    zacetek = []
    i = 1
    while i in zemljevid:
        if len(zemljevid[i]) == 1:
            zacetek.append(i)
        i += 1
    #stevilo krožišč
    st = set(zemljevid)
    a = set(pot)
    if len(a) != len(pot):
        return False
    if len(a) == (len(st)-len(zacetek)+2):
        return True
    return False

def navodila(pot, zemljevid):
    j = 0
    x = 2
    izvor = []
    for i in pot[1:-1]:
        a = zemljevid[i] * 2
        b = a.index(pot[j])
        c = a[b:].index(pot[x])
        izvor.append(c)
        j += 1
        x += 1
    return izvor

def prevozi(zacetek, navodila, zemljevid):
    a = zemljevid[zacetek][0]
    krozisce = [zacetek, a]
    b = zemljevid[a]
    for i in navodila:
        c = b.index(krozisce[-2])
        d = (b*2)[c + i]
        krozisce.append(d)
        b = zemljevid[d]
    return krozisce

def sosedi(doslej, zemljevid):
    s = set()
    for i in doslej:
        for j in zemljevid[i]:
            s.add(j)
    return s - doslej

def razdalja(x, y, zemljevid):
    r = 0
    if type(x) == int:
        x = set([x])
    while y not in x:
        x = sosedi(x, zemljevid)
        r += 1
    return r

