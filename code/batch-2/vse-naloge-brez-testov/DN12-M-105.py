def preberi(zemljevid):
    d = open(zemljevid)
    vrstice = sum(1 for _ in d)
    for i in range(1,vrstice-1):
        print(i, d.readline)

def preberi(ime_datoteke):
    slovar = {}
    with open(ime_datoteke) as d:
        for vrstica in enumerate(d,1):
            seznam = list(map(int,vrstica[1].strip().split()))
            a = seznam.index(min(seznam))
            seznam = [seznam[a]] + seznam[a+1:] + seznam[:a]
            slovar[vrstica[0]] = seznam
        return slovar

def mozna_pot(pot,zemljevid):
    path = zip(pot,pot[1:])
    brezpinz = pot[1:-1]
    return all([n2 in zemljevid[n1] for n1,n2 in path]) and len(zemljevid[pot[0]]) == len(zemljevid[pot[-1]]) == 1 and \
           all([len(zemljevid[n]) != 1 for n in brezpinz])

def hamiltonova(pot,zemljevid):
    return mozna_pot(pot,zemljevid) and all([n in zemljevid for n in pot]) and len(pot) == len(set(pot)) == sum(1 for n in zemljevid if len(zemljevid[n]) > 1)+2

def navodila(pot,zemljevid):
    return [(zemljevid[n2].index(n3)-zemljevid[n2].index(n1))%len(zemljevid[n2]) for n1,n2,n3 in zip(pot,pot[1:],pot[2:])]

def prevozi(zacetek, navodila, zemljevid):
    seznam = [zacetek, zemljevid[zacetek][0]]
    for n in navodila:
        zadnji = zemljevid[seznam[-1]][(zemljevid[seznam[-1]].index(seznam[-2])+n)%len(zemljevid[seznam[-1]])]
        seznam.append(zadnji)
    return seznam

def sosedi(doslej, zemljevid):
    sosed = set()
    for n in doslej:
        sosed.update(zemljevid[n])
    for t in doslej:
        if t in sosed:
            sosed.remove(t)
    return sosed

def razdalja(x, y, zemljevid):
    i = 1
    mnozica = {x}
    while True:
        for n in mnozica:
            if y in zemljevid[n]:
                return i
        s = mnozica.pop()
        mnozica.update(sosedi({s},zemljevid))
        i+=1

