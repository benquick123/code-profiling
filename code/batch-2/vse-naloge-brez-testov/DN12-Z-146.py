def preberi(ime_datoteke):
    i = 1
    slovar = {}
    x = open(ime_datoteke)
    for vrstica in x:
        vrstica = vrstica.strip()
        z = vrstica.split(" ")
        for a in range(len(z)):
            z[a] = int(z[a])
        r = z.index(min(z))
        slovar[i] = z[r:] + z[:r]
        i += 1
    return slovar

def mozna_pot(pot, zemljevid):
    if not len(zemljevid[pot[0]]) == 1:
        return False
    if not len(zemljevid[pot[-1]]) == 1:
        return False
    for i in range(len(pot) - 1):
        if len(zemljevid[pot[i]]) == 1 and not i == 0:
            return False
        if not pot[i+1] in zemljevid[pot[i]]:
            return False
    return True

def hamiltonova(pot, zemljevid):
    krozisca = {}
    for a in zemljevid:
        if not len(zemljevid[a]) == 1:
            krozisca[a] = zemljevid[a]
    if mozna_pot(pot, zemljevid):
        if len(set(pot)) == len(pot):
            if len(pot) == (len(krozisca) + 2):
                return True
    return False

def navodila(pot, zemljevid):
    x = []
    for i in range(len(pot)-2):
        a = zemljevid[pot[i+1]].index(pot[i])
        b = zemljevid[pot[i+1]].index(pot[i+2])
        if b > a:
            x.append(b-a)
        elif a == b:   #Narobe, zapelješ se cel krog.
            x.append(0)
        else:
            x.append(len(zemljevid[pot[i+1]])-a+b)
    return x

def prevozi(zacetek, navodila, zemljevid):
    x = [zacetek, zemljevid[zacetek][0]]
    for navodilo in navodila:
        izvoz = zemljevid[x[-1]].index(x[-2]) + navodilo
        b = izvoz % len(zemljevid[x[-1]])
        x.append(zemljevid[x[-1]][b])
    return x

def sosedi(doslej, zemljevid):
    x = set()
    for a in doslej:
        x |= set(zemljevid[a])
    for b in doslej:
        if b in x:
            x.remove(b)
    return x


