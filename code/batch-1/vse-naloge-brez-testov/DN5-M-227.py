def unikati(s):
    sez_unikatov = []

    for element in s:
        if element in sez_unikatov:
            continue

        else:
            sez_unikatov.append(element)

    return sez_unikatov


def avtor(tvit):
    besede = tvit.split()

    return besede[0][:-1]


def vsi_avtorji(tviti):
    seznam_avtorjev = []
    for tvit in tviti:
        seznam_avtorjev.append(avtor(tvit))

    return unikati(seznam_avtorjev)


def izloci_besedo(beseda):
    indeks_zac = 0
    indeks_kon = len(beseda) - 1

    for i in range(0, len(beseda)):
        if beseda[i].isalnum():
            break

        else:
            indeks_zac += 1

    for j in range(len(beseda) - 1, -1, -1):
        if beseda[j].isalnum():
            break

        else:
            indeks_kon -= 1

    return beseda[indeks_zac:indeks_kon+1]


def se_zacne_z(tvit, c):
    seznam_besed = []
    tvit_besede = tvit.split()
    for beseda in tvit_besede:
        if beseda[0] == c:
            seznam_besed.append(izloci_besedo(beseda))

    return unikati(seznam_besed)


def zberi_se_zacne_z(tviti, c):
    seznam_besed = []

    for tvit in tviti:
        if c in tvit:
            tvit_besede = tvit.split()
            for beseda in tvit_besede:
                if beseda[0] == c:
                    seznam_besed.append(izloci_besedo(beseda))

                else:
                    continue
        else:
            continue

    return unikati(seznam_besed)


def vse_afne(tviti):
    seznam_afn = zberi_se_zacne_z(tviti, "@")
    seznam_afn = unikati(seznam_afn)

    for i in range(0, len(seznam_afn)):
        seznam_afn[i] = izloci_besedo(seznam_afn[i])

    return seznam_afn


def vsi_hashtagi(tviti):
    seznam_hashov = zberi_se_zacne_z(tviti, "#")
    seznam_hashov = unikati(seznam_hashov)

    for i in range(0, len(seznam_hashov)):
        seznam_hashov[i] = izloci_besedo(seznam_hashov[i])

    return seznam_hashov


def vse_osebe(tviti):
    sez_avtorjev = vsi_avtorji(tviti)
    sez_omenjenih = vse_afne(tviti)

    sez_vseh = sez_avtorjev+sez_omenjenih
    sez_vseh.sort()

    return unikati(sez_vseh)


def custva(tviti, hashtagi):
    sez_avtorjev = []

    for tvit in tviti:
        if "#" not in tvit:
            continue

        else:
            tvit_besede = tvit.split()

            for beseda in tvit_besede:
                if beseda[0] == "#":
                    if beseda[1:] in hashtagi:
                        sez_avtorjev.append(avtor(tvit))

                    else:
                        continue

                else:
                    continue

    sez_avtorjev = unikati(sez_avtorjev)
    sez_avtorjev.sort()

    return sez_avtorjev


def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if "@" not in tvit:
            continue

        else:
            tvit_besede = tvit.split()

            for beseda in tvit_besede:
                if beseda[0] == "@":
                    if (izloci_besedo(beseda) == oseba1 and avtor(tvit) == oseba2) or \
                            (izloci_besedo(beseda) == oseba2 and avtor(tvit) == oseba1):
                        return True

                    else:
                        continue

                else:
                    continue

    return False


