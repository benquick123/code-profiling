def preberi(ime_datoteke):
    count = 1
    slovar = {}
    with open(ime_datoteke) as dat:
        content = dat.readlines()
    content = [x.strip() for x in content]
    for line in content:
        lst = list(map(int, line.split()))
        mini = lst.index(min(lst))
        lst[:] = lst[mini:] + lst[:mini]
        slovar[count] = lst
        count+=1
    return slovar

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[len(pot)-1]]) != 1:
        return False
    for i in range(0, len(pot)-1):
        if pot[i+1] not in zemljevid[pot[i]] or pot[i] == pot[i+1]:
            return False
    for i in range(1, len(pot)-1):
        if len(zemljevid[pot[i]]) == 1:
            return False
    return True

def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False
    if  len(pot) != len(set(pot)):
        return False
    count = 2
    for key, value in zemljevid.items():
        if len(value) != 1:
            count+=1
    if count != len(pot):
        return False
    return True

def navodila(pot, zemljevid):
    list = []
    for i in range(1, len(pot)-1):
        bef = zemljevid[pot[i]].index(pot[i-1])
        aft = zemljevid[pot[i]].index(pot[i+1])
        list.append((aft-bef) % len(zemljevid[pot[i]]))
    return list

def prevozi(zacetek, navodila, zemljevid):
    list = [zacetek]
    prev = zacetek
    curr = zemljevid[zacetek][0]
    list.append(curr)
    for el in navodila:
        bef = zemljevid[curr].index(prev)
        aft = (bef + el) % len(zemljevid[curr])
        tmp = zemljevid[curr][aft]
        list.append(zemljevid[curr][aft])
        prev = curr
        curr = tmp
    return list

