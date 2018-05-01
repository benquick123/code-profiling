# za 6

def najmanjsi_spredaj(polje):
    polje = list(map(int, polje))
    while True:
        if polje[0]==min(polje):
            return polje
        else:
            prva=polje[0]
            del polje[0]
            polje.append(prva)
            continue

def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    krozisce=1
    krozisca_slovar={}
    for vrsta in datoteka:
        krozisca_slovar[krozisce]=[]
        povezave=vrsta.split()
        krozisca_slovar[krozisce]=najmanjsi_spredaj(povezave)
        krozisce+=1
    return krozisca_slovar

def mozna_pot(pot, zemljevid):
    # najprej preveri ce se zacne in konca na vhodu/izhodu
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[len(pot) - 1]]) != 1:
        return False

    stevec = 0
    while stevec<len(pot):
        # preveri ce obstaja to krozisce
        if pot[stevec] not in zemljevid:
            return False
        # preveri samo ce ni to zadnje krozisce v poti
        if stevec != len(pot)-1:
            # preveri ce se krozisce ponovi
            if pot[stevec]==pot[stevec+1]:
                return False
            # preveri ce je povezava med trenutnim in naslednjim kroziscem
            if pot[stevec + 1] not in zemljevid[pot[stevec]]:
                return False
            # preveri ce gre vmes ven
            if stevec != 0 and len(zemljevid[pot[stevec]])==1 and stevec != len(pot)-1:
                return False
        stevec+=1
    return True

def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False
    kljuci = list(zemljevid.keys())
    #dobi vse izhode
    izhodi=[]
    for k in zemljevid:
        if len(zemljevid[k])==1:
            izhodi.append(k)
    # odstrani izhode iz poti in vseh krozisc
    kljuci = [n for n in kljuci if n not in izhodi]
    pot = [n for n in pot if n not in izhodi]

    if sorted(kljuci)==sorted(pot):
        return True
    return False

# za 7

def navodila(pot, zemljevid):
    navodila_=[]
    stevec=1
    while stevec<len(pot)-1:
        uvoz_indeks = zemljevid[pot[stevec]].index(pot[stevec-1])
        izvoz_indeks = zemljevid[pot[stevec]].index(pot[stevec+1])
        krozisce = zemljevid[pot[stevec]]
        zavoji = 0
        while True:
            if uvoz_indeks==izvoz_indeks:
                navodila_.append(0)
                break
            uvoz_indeks+=1
            zavoji+=1
            if uvoz_indeks>len(krozisce)-1: uvoz_indeks=0
            if krozisce[uvoz_indeks]==krozisce[izvoz_indeks]:
                navodila_.append(zavoji)
                break
            else:
                continue
        stevec+=1
    return navodila_

