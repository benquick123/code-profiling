def preberi(ime_datoteke):
    zem = {}
    st_krozisca = 0
    zemljevid = open(ime_datoteke, encoding="utf-8")
    for vrstica in zemljevid:
        krozisca = vrstica.strip().split(" ")
        pre = []
        for stevilka in krozisca:
            pre.append(int(stevilka))
        st_krozisca += 1
        while pre[0] != min(pre):
            pre.insert(0, pre[-1])
            del pre[-1]
        zem[st_krozisca] = pre
    return zem

def mozna_pot(pot, zemljevid):
    vhodi = []
    izhodi = []
    nova = zip(pot,pot[1:])
    for a, b in nova:
        if len(zemljevid[a]) == 1:
            vhodi.append(a)
        elif len(zemljevid[b]) == 1:
            izhodi.append(b)
        if b in zemljevid[a]:
            pass
        else:
            return False
    #if len(zemljevid[pot[-1]]) != 1 or len(zemljevid[pot[0]]) != 1:
    for c in vhodi:
        if c not in pot:
            return False
        if c != pot[0]:
            return False
    for b in izhodi:
        if b not in pot:
            return False
        if b != pot[-1]:
            return False
    if not vhodi:
        return False
    elif not izhodi:
        return False
    return True

def hamiltonova(pot, zemljevid):
    m = mozna_pot(pot, zemljevid)
    if m == True:
        io = []
        krizisca = 0
        neki = 0
        for x in pot:
            g = pot.count(x)
            if g > 1:
                return False
            d = zemljevid[x]
            if len(d) == 1:
                io.append(d)
            if len(d) > 1:
                krizisca += 1
        for gg in zemljevid:
            if len(zemljevid[gg]) > 1:
                neki +=1
        if krizisca < neki:
            return False
        if len(io) > 2 or len(io) <= 1:
            return False
        return True
    return False

def navodila(pot, zemljevid):
    navodila = []
    potovanje = zip(pot,pot[1:],pot[2:])                    #pazi na poimenovanje ugh ˇˇ
    for prejsnji, trenutni, naslednji in potovanje:
         st = (zemljevid[trenutni].index(naslednji) - zemljevid[trenutni].index(prejsnji)) % len(zemljevid[trenutni])
         navodila.append(st)
    return navodila

def prevozi(zacetek, navodila, zemljevid):
    drugi = zemljevid[zacetek]
    prevoz = [zacetek, drugi[0]]
    for n in navodila:
        a = prevoz[-1]
        print(a)
        seznam = zemljevid[a]
        print(seznam)
        indeks = seznam.index(prevoz[-2])
        indek = seznam[indeks:] + seznam[:indeks]
        prevoz.append(indek[n])
    return prevoz






