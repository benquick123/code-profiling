def preberi(ime_datoteke):
    slovar = {}
    index = 1
    f = open(ime_datoteke, "r")
    for line in f:
        line = line.replace("\n", "")
        krozisca = line.split(" ")
        for i in range(len(krozisca)):
            krozisca[i] = int(krozisca[i])
        zacetek = min(krozisca)
        while krozisca[0] != zacetek:
            krozisca.append(krozisca.pop(0))
        slovar[index] = krozisca
        index += 1
    return slovar


def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) > 1:
        return False
    if len(zemljevid[pot[-1]]) > 1:
        return False

    for i in range(len(pot) - 1):
        if pot[i] == pot[i + 1]:
            return False
        if 0 < i < len(pot) - 1:
            if len(zemljevid[pot[i]]) < 2:
                return False
        if pot[i + 1] not in zemljevid[pot[i]]:
            return False

    return True


def hamiltonova(pot, zemljevid):
    poti = {}
    zacetek = pot[0]
    konec = pot[-1]
    for key in zemljevid.keys():
        if len(zemljevid[key]) == 1:
            if key != zacetek and key != konec:
                continue
            else:
                poti[key] = 0
        else:
            poti[key] = 0

    if not mozna_pot(pot, zemljevid):
        return False

    for x in pot:
        poti[x] += 1

    for key in poti.keys():
        if not 0 < poti[key] < 2:
            return False

    return True
