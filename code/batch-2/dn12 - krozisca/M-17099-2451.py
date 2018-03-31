def preberi(ime_datoteke):
    dat = open(ime_datoteke)
    i = 1
    s = {}

    for vrstica in dat:
        s[i] = (list(map(int, vrstica.split())))
        i += 1

    dat.close()

    for st in s:
        najm = s[st][0]
        for el in s[st]:
            if najm > el:
                najm = el
        premik = s[st].index(najm)
        if premik:
            s[st] = s[st][premik:] + s[st][:premik]

    return s

def mozna_pot(pot, zemljevid):
    s = zemljevid
    if len(s[pot[0]]) == 1 and len(s[pot[len(pot) - 1]]) == 1:

        for el in pot[1:-1]:        #če je vmesni člen končni
            if len(s[el]) == 1:
                return False

        for i in range(len(pot) - 1): #če se kakšen člen ponovi
            if pot[i] == pot[i+1]:
                return False

        for i in range(len(pot) - 1): #ali so krozisca povezana
            if not pot[i+1] in s[pot[i]]:
                return False

        return True
    return False



def hamiltonova(pot, zemljevid):
    d = len(zemljevid)
    for el in zemljevid:
        if len(zemljevid[el]) == 1:
            d -= 1

    if len(pot) == d + 2:
        return mozna_pot(pot, zemljevid)

    return False


def navodila(pot, zemljevid):
    nav = []
    for i in range(1, len(pot) - 1):
        prej = pot[i - 1]
        nasl = pot[i + 1]
        mesto_prej = zemljevid[pot[i]].index(prej)
        mesto_nasl = zemljevid[pot[i]].index(nasl)
        d = len(zemljevid[pot[i]])
        premik = (mesto_nasl - mesto_prej) % d
        nav.append(premik)
    return nav

def prevozi(zacetek, navodila, zemljevid):
    krozisca = [zacetek, zemljevid[zacetek][0]]
    for nav in navodila:
        s = []
        for k, el in enumerate(zemljevid[krozisca[-1]]):
            if krozisca[-2] == el:
                s.append(k)
        d = len(zemljevid[krozisca[-1]])
        krozisca.append(zemljevid[krozisca[-1]][(max(s) + nav) % d])
    return krozisca


def sosedi(doslej, zemljevid):
    tmp = set()
    rez = set()
    tmp.update(doslej)
    for el in doslej:
        for ell in zemljevid[el]:
            if ell not in tmp:
                rez.add(ell)
                tmp.add(ell)
    return rez

def razdalja(x, y, zemljevid):
    mx = {x}
    sosedi(mx, zemljevid)
    raz = 0
    while y not in mx:
        raz += 1
        mx.update(sosedi(mx, zemljevid))
    return raz
