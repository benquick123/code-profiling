def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    st = 1
    slovar = {}
    urejen=[]
    for vrstica in datoteka:
        urejen.clear()
        b = vrstica.strip()
        a = list(b.split(' '))
        a = list(map(int, a))
        abba = a.index(min(a))
        for prvi in a[abba:]:
            urejen.append(prvi)
        for drugi in a[:abba]:
            urejen.append(drugi)
        slovar[st] = urejen[:]
        st += 1
    return slovar

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1:
        poo = True
    else:
        return False
    b = 0

    for krog in pot[1:-1]:
        a = pot[b]
        if len(zemljevid[krog]) == 1:
            return False
        if a == krog:
            return False
        b += 1
    b = 0
    for krog in pot[1:]:
        a = pot[b]
        aa = [a]
        if not bool(set(aa) & set(zemljevid[krog])):
            return False
        b += 1
    return bool(poo)

def hamiltonova(pot, zemljevid):
    poo = True
    a = pot[:]
    a.sort()
    prim = zemljevid
    ah = list(prim.keys())
    for key in zemljevid:
        if len(zemljevid[key]) == 1:
            if key in a:
               a.remove(key)
            if key in ah:
                ah.remove(key)

    if not a == ah:
        return False
    if not mozna_pot(pot, zemljevid):
        return False
    return poo