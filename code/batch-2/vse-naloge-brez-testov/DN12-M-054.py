def preberi(ime_datoteke):
    file = open(ime_datoteke)
    krozisca = {}
    i = 0
    for line in file:
        intline = [int(x) for x in line.strip("\n").split()]
        startind = intline.index(min(intline))
        start = intline[startind:]
        intline = start + intline[:startind]
        i += 1
        krozisca[i] = intline
    return krozisca

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1:
        return False
    for indx in range(len(pot[:-1])):
        if pot[indx] == pot[indx + 1]:
            return False
        if len(zemljevid[pot[indx]]) == 1 and indx > 0:
            return False
        if pot[indx + 1] not in zemljevid[pot[indx]]:
            return False
    return True

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid) and\
            len(set(pot)) == len(pot) and\
            len(pot) - 2 == len([x for x in zemljevid.values() if len(x) > 1]):
        return True
    else:
        return False



















