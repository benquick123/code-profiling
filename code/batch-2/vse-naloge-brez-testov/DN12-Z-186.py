def preberi(ime_datoteke):
    slov = {}
    i = 1
    for vrstica in open(ime_datoteke):
        vrstica1 = [int(x) for x in (vrstica.strip()).split()]
        z = vrstica1.index(min(y for y in vrstica1))
        vrstica2 = vrstica1[z:]
        for x in vrstica1[:z]:
            vrstica2.append(x)
        slov[i] = vrstica2
        i += 1
    return slov

def mozna_pot(pot, zemljevid):
    a = 0
    b = 0
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[len(pot)-1]]) == 1:
        for x in range(len(pot)-1):
                if pot[x+1] in zemljevid[pot[x]]:
                    a += 1

    for y in pot[1: (len(pot) - 1)]:
        if len(zemljevid[y]) != 1:
            b += 1

    if a == len(pot)-1 and b == len(pot)-2:
        return True

def hamiltonova(pot, zemljevid):
    kroz = []
    a = 0
    for k in zemljevid:
        if len(zemljevid[k]) > 1:
            kroz.append(k)

    for x in kroz:
        if x in pot and pot.count(x) == 1 and mozna_pot(pot, zemljevid) == True:
            a += 1

    if a == len(kroz):
        return True

def navodila(pot, zemljevid):
    sz = []
    for x in range(1, len(pot)-1):
        sz.append(zemljevid[pot[x]].index(pot[x+1]))
    return sz

