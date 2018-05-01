import collections

def preberi(ime_datoteke):
    i=1
    slovar=collections.defaultdict(list)
    datoteka = open(ime_datoteke,"r")
    for e in datoteka:
        e=e.replace("\n","")
        z=e.split()
        z=[int(x) for x in z]
        najm=z.index(min(z))
        a=z[najm:]+z[:najm]
        for x in a:
            slovar[i].append(x)
        i+=1
    return slovar

def mozna_pot(pot, zemljevid):
    t=[]
    i=1
    prvi=zemljevid[pot[0]]
    zadnji=zemljevid[pot[-1]]
    if len(prvi)!=1 or len(zadnji)!=1:
        return False
    prava=pot[1:-1]
    for e in prava:
        if len(zemljevid[e])==1:
            return False
    for e in pot:
        if i>len(pot)-1:
            break
        j=zemljevid[e]
        z=[str(x) for x in j]
        if str(pot[i]) in z:
            t.append(True)
        else:
            return False
        i+=1
    return all(t)

def hamiltonova(pot, zemljevid):
    t=[]
    if mozna_pot(pot, zemljevid) == False:
        return False
    for kateri, stevilka in zemljevid.items():
        if len(stevilka)>1:
            t.append(kateri)
    for e in pot[1:-1]:
        if pot.count(e)>1:
            return False
    if len(t)==len(pot[1:-1]):
        return True
    return False

def navodila(pot, zemljevid):
    navodilo=[]
    for i in range(len(pot)-2):
        pot1=pot[i:i+3]
        kam=zemljevid[pot1[1]][::-1]
        izvoz1=kam.index(pot1[2])
        izvoz2=kam.index(pot1[0])
        navodilo.append((izvoz2-izvoz1) % len(kam))
    return navodilo

def prevozi(zacetek, navodila, zemljevid):
    pot = [zacetek, zemljevid[zacetek][0]]
    for i in range(len(navodila)):
        r = zemljevid[pot[i+1]][::-1]
        izvoz2 = r.index(pot[i])
        for e in r:
            izvoz1 = r.index(e)
            if (izvoz2-izvoz1) % len(r) == navodila[i]:
                pot += [e]
        i += 1
    return pot

def sosedi(doslej, zemljevid):
    t=set()
    for e in doslej:
        sosedi=zemljevid[e]
        for sosed in sosedi:
            t.add(sosed)
    return t-doslej

def razdalja(x, y, zemljevid):
    if type(x)==int:
        x={x}
    x=sosedi(x, zemljevid)
    if y in x:
        return 1
    return razdalja(x, y, zemljevid) + 1


