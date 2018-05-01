
# Ocena 6
def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    zemljevid = {}
    x = 0
    for krizisce in datoteka:
        krizisce = krizisce.strip()
        x += 1
        seznam = []
        for e in krizisce.split():
            st = int(e)
            seznam.append(st)
        indeks = seznam.index(min(seznam))
        izhodi = seznam[indeks:] + seznam[:indeks]
        zemljevid[x]= izhodi
    return zemljevid

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[len(pot)-1]]) != 1:
        return False
    for e in pot[1:len(pot)-1]:
        if len(zemljevid[e]) <= 1:
            return False
    for x, y in zip(pot, pot[1:]):
        if x == y or y not in zemljevid[x]:
            return False
    return True

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid) != True:
        return False
    for indeks, krizisce in enumerate(pot):
        if krizisce in pot[:indeks] + pot[indeks+1:]:
            return False
    for k in zemljevid:
        if len(zemljevid[k])>1:
            if not k in pot[1:len(pot)-1]:
                return False
    return True

# Ocena 7
def navodila(pot, zemljevid):
    s = []
    for indeks, e in enumerate(pot[1:len(pot)-1]):
        trenutni = indeks + 1
        x = zemljevid[e].index(pot[trenutni-1])
        y = zemljevid[e].index(pot[trenutni+1])
        korak = (y-x)
        if korak < 0:
            korak = korak % len(zemljevid[e])
        s.append(korak)
    return s

# Ocena 8
def prevozi(zacetek, navodila, zemljevid):
    krozisce = zemljevid[zacetek][0]
    s = [zacetek,krozisce]
    for e in navodila:
        vhod = zemljevid[krozisce].index(s[len(s)-2])
        izhod = vhod + e
        if izhod > (len(zemljevid[krozisce])-1):
            izhod = izhod % len(zemljevid[krozisce])
        s.append(zemljevid[krozisce][izhod])
        krozisce = zemljevid[krozisce][izhod]
    return s


# Ocena 9

# def sosedi(doslej, zemljevid):

# def razdalja(x, y, zemljevid):

# Ocena 10

# def najkrajsa_navodila(x, y, zemljevid):













