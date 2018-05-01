def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    vrstica = 0
    slovar = {}
    for ukaz in datoteka:
        ukazs = []
        ukaz = ukaz.strip().split()
        for stevilka in ukaz:
            ukazs.append(int(stevilka))
        vrstica += 1
        while ukazs[0] != min(ukazs):
            m = ukazs.pop(1)
            ukazs.append(ukazs[0])
            ukazs[0] = m
        slovar[vrstica] = ukazs
    return slovar

def mozna_pot(pot, zemljevid):
    st = 0
    ok = []
    test2 = 0
    for korak in pot:
        if st == 0 or st == (len(pot)-1):
            if len(zemljevid[korak]) == 1:
                ok.append(True)
            else:
                ok.append(False)
        if st >= 1 and st <= (len(pot) - 2) and len(zemljevid[korak]) == 1:
            ok.append(False)
        if st > 0:
            if korak in zemljevid[pot[st-1]]:
                ok.append(True)
            else:
                ok.append(False)
        if korak == test2:
            ok.append(False)
        else:
            ok.append(True)
        test2 = korak
        st += 1
    return all(ok)

def hamiltonova(pot, zemljevid):
    krozisca = set()
    izhodi = set()
    ok = []
    for krozisce in range(1,len(zemljevid)+1):
        if len(zemljevid[krozisce]) > 1:
            krozisca.add(krozisce)
        else:
            izhodi.add(krozisce)
    for krozisce in krozisca:
        if krozisce in pot:
            ok.append(True)
        else:
            ok.append(False)
    if mozna_pot(pot, zemljevid) and pot[0] in izhodi and pot[len(pot)-1] in izhodi and len(set(pot)) == len(pot):
        ok.append(True)
    else:
        ok.append(False)
    return all(ok)

def navodila(pot, zemljevid):
    i = 1
    rez = []
    while i + 1 < len(pot):
        vhod = pot[i-1]
        izhod = pot[i+1]
        krozisce = zemljevid[pot[i]]
        st = 0
        while vhod != krozisce[0]:
            pr = krozisce.pop(1)
            krozisce.append(krozisce[0])
            krozisce[0] = pr
        while izhod != krozisce[0]:
            pr = krozisce.pop(1)
            krozisce.append(krozisce[0])
            krozisce[0] = pr
            st += 1
        i += 1
        rez.append(st)
    return rez

def prevozi(zacetek, navodila, zemljevid):
    sez = [zacetek, zemljevid[zacetek][0]]
    for korak in navodila:
        prvi = zemljevid[zacetek][0]
        krozisce = zemljevid[prvi]
        st = 0
        while zacetek != krozisce[0]:
            pr = krozisce.pop(1)
            krozisce.append(krozisce[0])
            krozisce[0] = pr
        zacetek = prvi
        while st != korak:
            pr = krozisce.pop(1)
            krozisce.append(krozisce[0])
            krozisce[0] = pr
            st += 1
        sez.append(krozisce[0])
    return sez

def sosedi(doslej, zemljevid):
    sosedi = set()
    for krozisce in doslej:
        for vsak in zemljevid[krozisce]:
            sosedi.add(vsak)
    for krozisce in doslej:
        if krozisce in sosedi:
            sosedi.remove(krozisce)
    return sosedi

def razdalja(x, y, zemljevid):
    pot = set()
    pot.add(x)
    stevec = 0
    while y not in pot:
        korak = sosedi(pot, zemljevid)
        for kr in korak:
            pot.add(kr)
        stevec += 1
    return stevec












