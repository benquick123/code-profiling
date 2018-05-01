def preberi(ime_datoteke):
    krizisca = []
    pot={}
    for vrstica in open(ime_datoteke):
        sklop = [int(e) for e in vrstica.split()]
        najmanj=min(sklop)
        if sklop.index(najmanj) == 0:
            krizisca.append(sklop)
        elif sklop.index(najmanj) == len(sklop):
            krizisca.append([najmanj] + sklop[:sklop.index(najmanj)])
        else:
            krizisca.append([najmanj] + sklop[sklop.index(najmanj) + 1:] + sklop[:sklop.index(najmanj)])
    for indeks, x in enumerate(krizisca):
        pot[indeks+1] = x
    return pot

def mozna_pot(pot, zemljevid):
    koncna=[]
    enojna=[]
    for i, krizisca in zemljevid.items():
        if len(krizisca)==1:
            enojna.append((i))
    if (pot[0] in enojna) and (pot[-1] in enojna):
        koncna.append(1)
    else:
        return False
    for e in pot[1:-2]:
        if e not in enojna:
            koncna.append(1)
        else:
            return False
    potka = []
    for e in pot:
        for i, krizisca in zemljevid.items():
            if e==i:
                potka.append((i,krizisca))
    potkica=list(enumerate(potka))
    for indeks, par in potkica:
        if indeks!=len(potkica)-1:
            if par[0] in potkica[indeks+1][1][1]:
                koncna.append(1)
            else:
                return False
    return bool(koncna)

def hamiltonova(pot, zemljevid):
    krozisca = []
    for i, krizisca in zemljevid.items():
        if len(krizisca) != 1:
            krozisca.append((i))
    unikati = []
    for e in pot:
        if e not in unikati:
            unikati.append(e)
    if mozna_pot(pot, zemljevid) and pot==unikati and len(pot)==(len(krozisca)+2):
        return True
    else:
        return False

def navodila(pot, zemljevid):
    stevilo_mejnih = []
    nav=[]
    for e in pot:
        for i, krozisca in zemljevid.items():
            if e == i:
                stevilo_mejnih.append((e, len(krozisca)))
    for a, b in stevilo_mejnih[1:-1]:
        for i, krozisca in zemljevid.items():
            if i==a:
                nav.append(krozisca[b-1])
    return nav


