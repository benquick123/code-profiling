def preberi(ime_datoteke):
    slovar = {}
    datoteka = open(ime_datoteke)
    i = 1
    for vrstica in datoteka:
        vrstica = vrstica.strip('\n')
        vrstica = vrstica.split(' ')
        seznam = [int(element) for element in vrstica]
        while(seznam[0] != min(seznam)):
            seznam.append(seznam[0])
            seznam[0] = seznam[1]
            seznam.remove(seznam[1])
        slovar[i] = seznam
        i += 1
    return slovar

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1:
        return False
    for korak in pot[1:-1]:
        if len(zemljevid[korak]) == 1:
            return False
    for korak in range(len(pot)-1):
        if pot[korak] == pot[korak + 1]:
            return False
        if pot[korak] not in zemljevid[pot[korak + 1]]:
            return False
    return True

def hamiltonova(pot, zemljevid):
    if len(set(pot)) != len(pot):
        return False
    mozna = mozna_pot(pot, zemljevid)
    if mozna != True:
        return False
    for kljuc, vrednost in zemljevid.items():
        if kljuc not in pot[1:-1] and len(vrednost) > 1:
            return False
    return True

def navodila(pot, zemljevid):
    sez = []
    for x in range(1, len(pot) - 1):
        izracun = ((zemljevid[pot[x]].index(pot[x + 1]) - zemljevid[pot[x]].index(pot[x - 1])) % len(zemljevid[pot[x]]))
        sez.append(izracun)
    return sez



