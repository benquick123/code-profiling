def preberi(ime_datoteke):
    s = {}
    dat = open(ime_datoteke)
    i = 1
    for vrstica in dat:
        vrstica = vrstica.strip().split(" ")
        vrstica = list(map(int, vrstica))
        naj_i = vrstica.index(min(vrstica))
        vrstica = [vrstica[naj_i]] + vrstica[naj_i+1:] + vrstica[:naj_i]
        s[i] = vrstica
        i += 1
    dat.close()
    return s

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1:
        for p1, p2 in zip(pot[:-1], pot[1:]):
            if p2 not in zemljevid[p1]:
                return False
            if len(zemljevid[p2]) == 1 and p2 != pot[-1]:
                return False
        return True
    return False

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid):
        st = 2
        for key, value in zemljevid.items():
            if len(value) > 1:
                st += 1
        if len(set(pot)) == len(pot) == st:
            return True
    return False

def navodila(pot, zemljevid):
    return [(zemljevid[p2].index(p3) - zemljevid[p2].index(p1)) %
            len(zemljevid[p2]) for p1, p2, p3 in
                zip(pot[:-1], pot[1:], pot[2:])]

def prevozi(zacetek, navodila, zemljevid):
    zap = [zacetek, zemljevid[zacetek][0]]
    for nav in navodila:
        zem = zemljevid[zap[-1]]
        st = zem.index(zap[-2]) + nav
        if st >= len(zem):
            st -= len(zem)
        zap.append(zem[st])
    return zap

def sosedi(doslej, zemljevid):
    s = set()
    for dos in doslej:
        for z in zemljevid[dos]:
            s.add(z)
    for dos in doslej:
        if dos in s:
            s.remove(dos)
    return s

def razdalja(x, y, zemljevid):
    vsi = set()
    vsi.add(x)
    st = 0
    while y not in vsi:
        vsi = sosedi(vsi, zemljevid)
        st += 1
    return st

def najkrajsa_navodila(x, y, zemljevid):
    vsi = [x, zemljevid[x][0]]
    pot = [[0, x, zemljevid[x][0]]]
    index = 0
    stop = 0
    while y not in vsi:
        for i, x1, x2 in pot:
            if stop:
                break
            if i == index:
                for z in zemljevid[x2]:
                    if z not in vsi:
                        vsi.append(z)
                        pot.append([index+1, x2, z])
                    if z == y:
                        stop = 1
                        break
        index += 1
    prava_pot = [pot[-1][2], pot[-1][1]]
    for i in range(index - 1, -1, -1):
        for ix, x1, x2 in pot:
            if i == ix and x2 == prava_pot[-1]:
                prava_pot.append(x1)
    return navodila(prava_pot[::-1], zemljevid)






