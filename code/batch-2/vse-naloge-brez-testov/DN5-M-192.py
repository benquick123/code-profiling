def unikati(s):
    x = ""
    list = []
    for x in s:
        if x not in list:
            list.append(x)
    return list


def avtor(tvit):
    return tvit.split(":")[0]


def vsi_avtorji(tviti):
    avtorji = []
    for x in tviti:
        z = x.split(":")[0]
        avtorji.append(z)
    unikati = []
    for x in avtorji:
        if x not in unikati:
            unikati.append(x)
    return unikati


def izloci_besedo(beseda):
    nova_beseda = ""
    for x in beseda:
        if x.isalnum():
            nova_beseda += x
        elif x == "-":
            nova_beseda += x
    return nova_beseda


def se_zacne_z(tvit, c):
    besede = tvit.split()
    izluščene_besede = []
    i = 0
    for x in besede:
        if x[0][0] == c:
            izluščene_besede.append(izloci_besedo(x))
    return izluščene_besede


def zberi_se_zacne_z(tviti, c):
    seznam_besed = []
    for vrstica in tviti:
        seznam_besed.extend(se_zacne_z(vrstica, c))
    return unikati(seznam_besed)


def vse_afne(tviti):
    besede = []
    for x in tviti:
        besede.extend(se_zacne_z(x, "@"))
    return unikati(besede)


def vsi_hashtagi(tviti):
    besede = []
    for x in tviti:
        besede.extend(se_zacne_z(x, "#"))
    return unikati(besede)


def vse_osebe(tviti):
    osebe = []
    for x in tviti:
        osebe.append(x.split(":")[0])
    osebe.extend(vse_afne(tviti))
    osebe = unikati(osebe)
    return sorted(osebe)


def custva(tviti, hashtagi):
    ljudje = []
    for x in tviti:
        vrstica = []
        vrstica.extend(x.split())
        for beseda in vrstica:
            if izloci_besedo(beseda) in hashtagi:
                ljudje.append(izloci_besedo(vrstica[0]))
    return sorted(unikati(ljudje))


def se_poznata(tviti, oseba1, oseba2):
    znanci = [oseba1, oseba2]
    rezultat = False
    if len(list(set(znanci) & set(vse_osebe(tviti)))) == 2:
        for x in tviti:
            vrstica = []
            vrstica.extend(x.split())
            if izloci_besedo(vrstica[0]) in znanci:
                vrstica.pop(0)
                for beseda in vrstica:
                    if izloci_besedo(beseda) in znanci:
                        rezultat = True
                        break

    return rezultat
