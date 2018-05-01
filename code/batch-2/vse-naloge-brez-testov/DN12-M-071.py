def preberi(ime_datoteke):
    stevec = 1
    krozisca = {}
    temp = open(ime_datoteke).read().split("\n")
    if temp[-1] == "":
        temp = temp[:-1]
    for k in temp:
        if k[0] == min(k):
            krozisca[stevec] = [int(k)]
        else:
            numbers = []
            count = 0
            ke = k.split()
            ke = list(map(int, ke))
            for e in ke:
                if e == min(ke):
                    numbers = ke[count:]
                    if ke[:count] != "":
                        numbers += ke[:count]
                    break
                count += 1
            krozisca[stevec] = numbers
        stevec += 1
    return krozisca

def mozna_pot(pot, zemljevid):
    stevec = 0
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1:
        return False
    for k in pot:
        if stevec == len(pot) -1:
            break
        if len(zemljevid[k]) == 1 and stevec != 0:
            return False
        x = zemljevid[k]
        if pot[stevec + 1] not in x:
            return False
        stevec += 1
    return True

def hamiltonova(pot, zemljevid):
    temp = []
    for e in pot:
        if e not in temp:
            temp.append(e)
        elif e in temp:
            return False
    for i in range(1,max(zemljevid)+1):
        if len(zemljevid[i]) != 1:
            if i not in pot:
                return False
    return mozna_pot(pot, zemljevid)

def navodila(pot, zemljevid):
    n = []
    stev1 = 0
    stev2 = 0
    pos = 0
    temp_1 = list(zip(pot, pot[1:], pot[2:]))
    for (x, y, z) in temp_1:
        temp_2 = list(enumerate(zemljevid[y], start=1))
        for (a, b) in temp_2:
            if b == z:
                stev2 = a
            if b == x:
                stev1 = a
        pos = (stev2 - stev1) % len(temp_2)
        n.append(abs(pos))
    return(n)

def prevozi(zacetek, navodila, zemljevid):
    n = []
    i = 0
    n.append(zacetek)
    x = zemljevid[zacetek]
    pos = x[0]
    n.append(pos)
    ind = 0
    for e in navodila:
        x = list(enumerate(zemljevid[pos]))
        for (a, b) in x:
            if b == n[i]:
                ind = a
                break
        ind += e
        if ind > len(x) -1:
            ind = ind - len(x)
        pos = x[ind][1]
        n.append(pos)
        i += 1
    return n

def sosedi(doslej, zemljevid):
    list = set()
    for element in doslej:
        list = list | set(zemljevid[element])
    for element in doslej:
        try:
            list.remove(element)
        except:
            continue
    return(list)

def razdalja(x, y, zemljevid):
    layer = 0
    temp = []
    c = False
    q = x
    if q == y:
        return 0
    q = zemljevid[q]
    q = set(q)
    layer += 1
    if y in q:
        c = True

    while c is False:
        for e in q:
            temp += zemljevid[e]
        q.update(temp)
        temp = []
        layer += 1
        if y in q:
            c = True
    return layer

def najkrajsa_navodila(x, y, zemljevid):
    c = False
    pot = dict()
    pot[x] = zemljevid[x]
    while c is False:
        for key in pot.items():
            temp = zemljevid[key]
            for e in temp:
                pot[e] = zemljevid[e]
