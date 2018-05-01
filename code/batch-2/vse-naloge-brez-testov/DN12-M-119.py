def vrniIzhodIzKrozisca(vhod, st_izvozov, krizisce):
    zacetni_index = krizisce.index(vhod)
    for i in range(st_izvozov):
        if zacetni_index == len(krizisce)-1:
            zacetni_index = 0
        else:
            zacetni_index +=1
    return krizisce[zacetni_index]


def preberi(ime_datoteke):
    dat = open(ime_datoteke)
    pod = dat.read().split("\n")
    dat.close()
    r = {}
    m = True
    for i in range(len(pod)):
        if not pod[i]:
            break
        r[i+1]= [int(j) for j in pod[i].split(" ")]
        while m:
            if(r[i+1][0] == min(r[i+1])):
                m = False
                break
            r[i+1].append(r[i+1][0])
            r[i+1].remove(r[i+1][0])
        m = True
    return r

def mozna_pot(p, z):
    if not len(z[p[0]]) == len(z[p[-1]]) == 1:
        return False
    if len(p) == 2:
        if p[0] in z[p[1]]:
            return True
        return False
    pr = p[0]
    p.remove(p[0])
    p.remove(p[-1])
    for i in p:
        if len(z[i]) == 1:
            return False
        if i == pr:
            return False
        if pr not in z[i]:
            return False
        pr = i
    return True

def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot,zemljevid):
        return False
    krozisca = 0
    for i in zemljevid.keys():
        if not len(zemljevid[i]) == 1:
            krozisca +=1
    if krozisca != len(pot):
        return False
    return True

def navodila(pot, zemljevid):
    s = []
    for i in range(len(pot)):
        if pot[i] == pot[-2] and pot[i+1] == pot[-1]:
            break
        s.append((zemljevid[pot[i+1]].index(pot[i+2])-zemljevid[pot[i+1]].index(pot[i])) % len(zemljevid[pot[i+1]]))
    return s

def prevozi(zacetek, navodila, zemljevid):
    tab = [zacetek,zemljevid[zacetek][0]] 
    for i in navodila:
        kon = zemljevid[tab[-1]]
        print(tab[-1], " ", i, " ", kon )
        novo_krozisce = vrniIzhodIzKrozisca(tab[-2], i, kon)
        tab.append(novo_krozisce)
    return tab




