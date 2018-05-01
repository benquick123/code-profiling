def od_najmanjsega(seznam):
    najmanjsi = float("inf")
    for stev in seznam:
        if stev < najmanjsi:
            najmanjsi = stev
    nov_seznam = seznam[seznam.index(najmanjsi):]
    for stev in seznam[:seznam.index(najmanjsi)]:
        nov_seznam.append(stev)
    return nov_seznam

def preberi(ime_datoteke):
    x = 1
    slovar = {}
    for vrstica in open(ime_datoteke):
        seznam = []
        split = vrstica.split()
        for znak in split:
            seznam.append(int(znak))
        slovar[x] = seznam
        x += 1
    for kljuc in slovar:
        slovar[kljuc] = od_najmanjsega(slovar[kljuc])
    return slovar

def mozna_pot(pot, zemljevid):
    y = pot[0]
    mozno = None
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1:
        for x in pot[1:]:
            if x in zemljevid[y]:
                mozno = True
            else:
                mozno = False
                break
            y = x
    else:
        mozno = False
    if mozno == True:
        for x in pot[1:-1]:
            if len(zemljevid[x]) == 1:
                mozno = False
                break
    return mozno

def hamiltonova(pot, zemljevid):
    mozno = False
    if mozna_pot(pot, zemljevid):
        vsi = []
        for kljuc in zemljevid:
            if len(zemljevid[kljuc]) != 1:
                vsi.append(kljuc)
        urejeno = sorted(pot)
        for x in urejeno:
            if len(zemljevid[x]) == 1:
                del urejeno[urejeno.index(x)]
        if vsi == urejeno:
            mozno = True
    return mozno

