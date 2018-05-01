def preberi(ime_datoteke):

    krozisca = {el: list()  for el in range(1, len(open(ime_datoteke).readlines(  ))+1)}
    datoteka = open(ime_datoteke)
    for indeks in range(1, len(krozisca)+1):
        for vrstica in datoteka:
            for stolpec in vrstica.split(" "):
                if stolpec != " ":
                    krozisca[indeks].append(int(stolpec))
            break
        if krozisca[indeks][0] != min(krozisca[indeks]):
            krozisca[indeks] = krozisca[indeks][krozisca[indeks].index(min(krozisca[indeks])):len(krozisca[indeks])] + krozisca[indeks][0:krozisca[indeks].index(min(krozisca[indeks]))]
    return krozisca

def mozna_pot(pot, zemljevid):
    for poteza in range(0,len(pot)-1):
        if pot[poteza+1] not in zemljevid[pot[poteza]] or pot[poteza] == pot[poteza+1] or len(zemljevid[pot[len(pot)-1]]) != 1 or len(zemljevid[pot[0]]) != 1:
            return False
        for vmesnePoteze in range(1, len(pot)-2):
            if len(zemljevid[pot[vmesnePoteze]]) == 1:
                return False
    return True

def hamiltonova(pot, zemljevid):
    stevec = {el: 0 for el in zemljevid if len(zemljevid[el])>1}
    if not mozna_pot(pot, zemljevid):
        return False
    for poteza in range(0, len(pot)):
        if pot[poteza] in stevec:
            stevec[pot[poteza]]+=1
    for stevilka in stevec:
        if stevec[stevilka] != 1:
            return False
    return True

