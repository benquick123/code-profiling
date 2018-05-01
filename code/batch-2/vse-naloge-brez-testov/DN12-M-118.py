def preberi(ime_datoteke):
    index = 1
    newList = []
    slovar = {}
    datoteka = open(ime_datoteke)
    for i in datoteka:
        temp = i.strip().split()
        for j in temp:
            newList.append(int(j))
        while newList[0] != min(newList):
            tmp = newList[0]
            newList.pop(0)
            newList.append(tmp)
        slovar[index] = newList
        index += 1
        newList = []
    return slovar


def mozna_pot(pot, zemljevid):
    x = 1
    zacKon = []
    for i in range(1, len(zemljevid)):
        if len(zemljevid[i]) == 1:
            zacKon.append(i)
    if len(zemljevid[pot[0]]) > 1 or len(zemljevid[pot[len(pot) - 1]]) > 1:
        return False
    else:
        while x < len(pot):   
            y = pot[x - 1]
            if pot[x] not in zemljevid[y] or y in zacKon and x+1 != len(pot) and x != 1: # or y in zacKon and x < len(pot)
                return False
            x += 1
        return True


def hamiltonova(pot, zemljevid):
    vsaKrizisca = []
    for i in range(1, len(zemljevid) + 1):
        if len(zemljevid[i]) > 1:
            vsaKrizisca.append(i)
    for i in pot[1:-1]:
        if i not in vsaKrizisca:
            return False
    if len(vsaKrizisca) != len(pot[1:-1]):
        return False
    return all([mozna_pot(pot, zemljevid)] and [len(set(pot)) == len(pot)])


def navodila(pot, zemljevid):
    '''
    navodilaPoti = []
    for i in range(len(pot)):
        if len(zemljevid[pot[i]]) > 1:
            navodilaPoti.append((zemljevid[pot[i]].index(pot[i + 1]) - (zemljevid[pot[i]].index(pot[i - 1]))) % len(zemljevid[pot[i]]))
    return navodilaPoti
    '''
    return [((zemljevid[pot[i]].index(pot[i + 1])) - (zemljevid[pot[i]].index(pot[i - 1]))) % len(zemljevid[pot[i]]) for i in range(len(pot)) if len(zemljevid[pot[i]]) > 1]


def prevozi(zacetek, navodila, zemljevid):
    pot = [zacetek, zemljevid[zacetek][0]]
    x = 1
    for i in navodila:
        while pot[x - 1] != zemljevid[pot[x]][0]:
            temp = zemljevid[pot[x]][0]
            zemljevid[pot[x]].pop(0)
            zemljevid[pot[x]].append(temp)
        pot.append(zemljevid[pot[x]][i])
        x += 1
    return pot


def sosedi(doslej, zemljevid):
    '''
    mnozica = set()
    for i in doslej:
        for _ in zemljevid[i]:
            if _ not in doslej:
                mnozica.add(_)
    return mnozica
    '''
    return set([_ for i in doslej for _ in zemljevid[i] if _ not in doslej])

def najkrajsa(zacetek, konec, zemljevid, pot =[]):
    pot = pot + [zacetek]
    if zacetek == konec:
        return pot
    minimum = None
    for i in zemljevid[zacetek]:
        if i not in pot:
            novaPot = najkrajsa(i, konec, zemljevid, pot)
            if novaPot:
                if not minimum or len(novaPot) < len(minimum):
                    minimum = novaPot
    return minimum


def razdalja(x, y, zemljevid):
    return len(najkrajsa(x, y, zemljevid)) - 1


def najkrajsa_navodila(x, y, zemljevid):
    navodilaPoti = []
    pot = najkrajsa(x, y, zemljevid)
    for i in range(len(pot)):
        if len(zemljevid[pot[i]]) > 1:
            navodilaPoti.append((zemljevid[pot[i]].index(pot[i + 1]) - (zemljevid[pot[i]].index(pot[i - 1]))) % len(zemljevid[pot[i]]))
    return navodilaPoti


