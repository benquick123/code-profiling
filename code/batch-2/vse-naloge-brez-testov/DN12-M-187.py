def preberi(ime_datoteke):
    dat = open(ime_datoteke)
    s = {}
    c = 1
    for vrstica in dat:
        k = []
        for kriz in vrstica.split():
            k.append(int(kriz))
        m = k.index(min(k))
        k2 = k[m:] + k[:m]
        s[c] = k2
        c += 1
    return s

# Pot je možno prevoziti, če se začne in konča s končno povezavo (prepoznate jo po tem, da je povezana le z enim krožiščem),
# če vmes ni končnih povezav, če se nobeno krožišče ne ponovi (iz krožišča 6 ne moremo zapeljati v krožišče 6) in
# če so vsa krožišča na poti dejansko povezana.

def mozna_pot(pot, zemljevid):
    s = zemljevid
    for e in pot[1:-1]:
        if len(s[e]) == 1:
            return False
    for n in range(len(pot)-1):
        if pot[n] == pot[n+1]:
            return False
        if pot[n+1] not in s[pot[n]]:
            return False

    return len(s[pot[0]]) == 1 and len(s[pot[-1]]) == 1

def hamiltonova(pot, zemljevid):
    s =[]
    for e in zemljevid:
        if len(zemljevid[e]) > 1:
            s.append(e)

    return mozna_pot(pot, zemljevid) and len(set(pot)) == len(pot) and set(s) <= set(pot)

def navodila(pot, zemljevid):

    s = []
    for e in range(1, len(pot)-1):
        izhod = zemljevid[pot[e]].index(pot[e+1])
        vhod = zemljevid[pot[e]].index(pot[e-1])
        z = len(zemljevid[pot[e]])
        x = (izhod - vhod) % z
        s.append(x)
    return s

def prevozi(zacetek, navodila, zemljevid):
    s = [zacetek, zemljevid[zacetek][0]]
    for x in navodila:
        vhod = s[-1]
        krizisce = zemljevid[vhod] + (zemljevid[vhod])
        izhod = krizisce.index(s[-2]) + x
        s.append(krizisce[izhod])
    return s

def sosedi(doslej, zemljevid):
    m = set()
    for e in doslej:
        for f in zemljevid[e]:
            m.add(f)
    return m - set(doslej)

def razdalja(x, y, zemljevid):
    s = set(zemljevid[x])
    c = 1
    while not y in s:
        c += 1
        s = s | (sosedi(s, zemljevid))
    return c

# def najkrajsa_navodila(x, y, zemljevid):



