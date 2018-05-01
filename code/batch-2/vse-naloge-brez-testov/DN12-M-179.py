def uredi_zemljevid(zemljevid):
    for krozisce in zemljevid:
        krozisca = zemljevid[krozisce]
        urejeno_krozisce = krozisca[krozisca.index(min(krozisca)):]
        for stevka in krozisca[:krozisca.index(min(krozisca))]:
            urejeno_krozisce.append(stevka)
        zemljevid[krozisce] = urejeno_krozisce
    return zemljevid


def preberi(ime_datoteke):
    datoteka, zemljevid, st_krozisca = open(ime_datoteke), {}, 1
    for vrstica in datoteka:
        krozisca, vrstica = [], vrstica.split()
        for krozisce in vrstica:
            if krozisce.isalnum():
                krozisca.append(int(krozisce))
        zemljevid[st_krozisca] = krozisca
        st_krozisca += 1
    return uredi_zemljevid(zemljevid)


def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) > 1 or len(zemljevid[pot[len(pot)-1]]) > 1:
        return False
    for krozisce in range(len(pot)):
        if (krozisce + 1) <= (len(pot) - 1):
            if pot[krozisce] == pot[krozisce + 1] or pot[krozisce] not in zemljevid[pot[krozisce + 1]]:
                return False
            if krozisce != 0 and krozisce != len(pot)-1:
                if len(zemljevid[pot[krozisce]]) == 1:
                    return False
    return True


def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid) and len(pot) != len(set(pot)):
        return False
    vsa_krozisca = []
    for vsi in zemljevid:
        if len(zemljevid[vsi]) > 1:
            vsa_krozisca.append(vsi)
    for krozisce in pot[1:-1]:
        if krozisce not in vsa_krozisca or len(pot[1:-1]) != len(vsa_krozisca):
            return False
    return True


def navodila(pot, zemljevid):
    nav = []
    for krozisce in range(1, len(pot) - 1, 1):
        razlika = zemljevid[pot[krozisce]].index(pot[krozisce+1]) - zemljevid[pot[krozisce]].index(pot[krozisce-1])
        nav.append(razlika % len(zemljevid[pot[krozisce]]))
    return nav


def prevozi(zacetek, navodila, zemljevid):
    vozlisca, i = [zacetek, zemljevid[zacetek][0]], 1
    for izvoz in navodila:
        n, nov_zemljevid = 0, zemljevid[vozlisca[i]]
        while vozlisca[i-1] != nov_zemljevid[0]:
            nov_zemljevid = zemljevid[vozlisca[i]][n:] + zemljevid[vozlisca[i]][:n]
            n += 1
        i += 1
        vozlisca.append(nov_zemljevid[izvoz])
    return vozlisca


def sosedi(doslej, zemljevid):
    povezave = set()
    for krozisce in doslej:
        for element in zemljevid[krozisce]:
            if element not in doslej and element not in povezave:
                povezave.add(element)
    return povezave


def razdalja(x, y, zemljevid):
    dolzina, prva = 1, set(zemljevid[x])
    while y not in prva:
        prva.update(sosedi(prva, zemljevid))
        dolzina += 1
    return dolzina

