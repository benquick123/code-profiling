def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    slovar = dict()
    st_vrst = 0
    sez = []
    for vrstica in datoteka:
        st_vrst += 1
        neurejen_sez = [int(x) for x in vrstica.rstrip().split(" ")]
        ind = neurejen_sez.index(min(neurejen_sez))
        for element in neurejen_sez[ind:]:
            sez.append(element)
        for element in neurejen_sez[:ind]:
            sez.append(element)
        slovar[st_vrst] = sez
        sez = []
    return slovar

def mozna_pot(pot, zemljevid):
    return len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[len(pot) - 1]]) == 1 and \
           all(pot[x] != pot[x + 1] for x in range(len(pot) - 1)) and \
           all(len(zemljevid[pot[x]]) != 1 for x in range(1, len(pot) - 1)) and \
           all(pot[x] in zemljevid[pot[x + 1]] for x in range(len(pot) - 1))

def hamiltonova(pot, zemljevid):
    return len(set(pot)) == len(pot) and mozna_pot(pot, zemljevid) and \
    len(set(pot)) == len(zemljevid) - (len([x for x in zemljevid if len(zemljevid[x]) == 1]) - 2)

def navodila(pot, zemljevid):
    return [(zemljevid[pot[x]].index(pot[x + 1]) - zemljevid[pot[x]].index(pot[x - 1])) % len(zemljevid[pot[x]])
                for x in range(1, len(pot) - 1)]

def prevozi(zacetek, navodila, zemljevid):
    prej = zacetek
    trenutno = zemljevid[zacetek][0]
    sez = [prej, trenutno]
    for x in navodila:
        ind = (zemljevid[trenutno].index(prej) + x) % len(zemljevid[trenutno])
        sez.append(zemljevid[trenutno][ind])
        prej = trenutno
        trenutno = zemljevid[trenutno][ind]
    return sez


