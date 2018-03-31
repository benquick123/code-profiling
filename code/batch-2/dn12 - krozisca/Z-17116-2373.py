def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    sez = []
    for krozisce in datoteka:
        krozisce = krozisce.strip().split()
        m = []
        for deli in krozisce:
            deli = int(deli)
            m.append(deli)
        najmanjsi = m.index(min(m))
        for x in range(0, najmanjsi):
            m.append(m[x])
        for x in range(0, najmanjsi):
            m.remove(m[0])
        sez.append(m)
    datoteka.close()
    return {x+1:sez[x] for x in range(0, len(sez))}

def povezave(pot,zemljevid):
    for n in range(0, len(pot)-1):
        if pot[n+1] not in zemljevid[pot[n]]:
            return False
    return True

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1:
        return False
    if len(zemljevid[pot[-1]]) != 1:
        return False
    for i in range(1,len(pot)-1):
        if len(zemljevid[pot[i]]) == 1:
            return False
    for i in range(1, len(pot) - 1):
        if pot[i] == pot[i+1]:
            return False
    for n in range(0, len(pot)-1):
        if pot[n+1] not in zemljevid[pot[n]]:
            return False
    return True

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid):
        x = 0
        for stevilke in zemljevid:
            if len(zemljevid[stevilke]) != 1:
                x += 1
        return len(pot) == (x+2)

#ZA OCENO 7
def navodila(pot, zemljevid):
    sez = []
    for deli in range(1, len(pot)-1):
        zacetek = zemljevid[pot[deli]].index(pot[deli-1])
        konec = zemljevid[pot[deli]].index(pot[deli+1])
        if zacetek > konec:
            sez.append(len(zemljevid[pot[deli]]) - zacetek + konec)
        else:
            sez.append(abs(konec-zacetek))
    return sez

#ZA OCENO 8
def prevozi(zacetek, navodila, zemljevid):
    sez = [zacetek]
    for z in zemljevid[zacetek]:
        sez.append(z)
    for stevila in navodila:
        vhodni_index = zemljevid[sez[-1]].index(sez[-2])
        sestevek = vhodni_index + stevila
        if sestevek >= len(zemljevid[sez[-1]]):
            sestevek -= len(zemljevid[sez[-1]])
        sez.append(zemljevid[sez[-1]][sestevek])
    return sez

#ZA OCENO 9
def sosedi(dolsej, zemljevid):
    mnozica = set()
    for deli in zemljevid:
        if deli in dolsej:
            for stevilke in zemljevid[deli]:
                if stevilke not in dolsej:
                    mnozica.add(stevilke)
    return mnozica