def preberi(ime_datoteke):
    with open(ime_datoteke) as datoteka:
        zemljevid = {}
        vozlisce = 1
        for i in datoteka.readlines():
            zemljevid[vozlisce] = []
            for j in i.split():
                zemljevid[vozlisce].append(int(j))
            vozlisce += 1
    for i in zemljevid:
        povezave = zemljevid[i]
        najmanj = min(povezave)
        while povezave[0] != najmanj:
            a = povezave[0]
            povezave.remove(a)
            povezave.append(a)

    return zemljevid


def mozna_pot(pot, zemljevid):
    zadnja = pot[-1]
    prva = pot[0]
    if len(zemljevid[zadnja]) > 1:
        return False
    elif len(zemljevid[prva]) > 1:
        return False
    for k, i in enumerate(pot[:-1]):
        if pot[k + 1] not in zemljevid[i]:
            return False
        if i != pot[0] and i != pot[-1] and len(zemljevid[i]) == 1:
            return False

    return True


def hamiltonova(pot, zemljevid):
    for i in pot:
        if pot.count(i) > 1:
            return False
    for i in zemljevid:
        if len(zemljevid[i]) > 1:
            if i not in pot:
                return False

    return mozna_pot(pot, zemljevid)


