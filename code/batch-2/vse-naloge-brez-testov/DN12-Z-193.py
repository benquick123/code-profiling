import os.path

def preberi(zemljevid):
    pot = {}
    i = 1
    if not os.path.exists(zemljevid):
        pot[1] = None
        return pot
    for vrstica in open(zemljevid):
        vecji = []
        krozisca= []
        presega = False
        tocke = [int(x) for x in vrstica.split(" ")]
        najmanjsi = min(tocke)
        for krozisce in tocke:
            if krozisce == najmanjsi:
                presega = True
            if presega:
                krozisca.append(krozisce)
            else:
                vecji.append(krozisce)
        krozisca.extend(vecji)
        pot[i] = krozisca
        i += 1
    return pot


def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[len(pot) - 1]]) != 1:
        return False
    for i in range(0, len(pot) - 1):
        if len(zemljevid[pot[i]]) == 1 and i != 0 and i != len(pot) - 1:
            return False
        if pot[i+1] == pot[i]:
            return False
        if pot[i+1] not in zemljevid[pot[i]]:
            return False
    return True

def stevilo_koncnih(zemljevid):
    i = 0
    for krozisce in zemljevid.values():
        if len(krozisce) == 1:
            i += 1
    return i

def hamiltonova(pot, zemljevid):
    krozisca = []
    if len(pot) != len(zemljevid) - stevilo_koncnih(zemljevid) + 2:
        return False
    for i in pot:
        if i in krozisca:
            return False
        krozisca.append(i)
    return mozna_pot(pot, zemljevid)

def navodila(pot, zemljevid):
    izvozi = []
    for i in range(1, len(pot) - 1):
        tocke = zemljevid[pot[i]]
        vecji = []
        krozisca = []
        presega = False
        najmanjsi = pot[i-1]
        for krozisce in tocke:
            if krozisce == najmanjsi:
                presega = True
            if presega:
                krozisca.append(krozisce)
            else:
                vecji.append(krozisce)
        krozisca.extend(vecji)
        izvozi.append(krozisca.index(pot[i+1]))
    return izvozi








