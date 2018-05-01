def unikati(s):
    seznam = []
    for element in s:
        if element not in seznam:
            seznam.append(element)
    return seznam


def avtor(tvit):
    ime = ""
    for znak in tvit:
        if znak == ":":
            break
        ime += znak
    return ime


def vsi_avtorji(tviti):
    seznam = []
    for tvit in tviti:
        seznam.append(avtor(tvit))
    return unikati(seznam)


def izloci_besedo(beseda):
    koncna = beseda
    for crka in beseda:
        if crka.isalnum():
            break
        koncna = koncna[1:]

    for crka in beseda[::-1]:
        if crka.isalnum():
            break
        koncna = koncna[:-1]
    return koncna


def se_zacne_z(tvit, c):
    seznam = []
    for beseda in tvit.split():
        if beseda[0] == c:
            seznam.append(izloci_besedo(beseda))
    return seznam


def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        seznam += se_zacne_z(tvit, c)
    return unikati(seznam)


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne((tviti))))


#DOOOODAAAAAAATNAAAAAAAAAAAAAAAAAAA


def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        for hashtag in hashtagi:
            if hashtag in se_zacne_z(tvit, "#"):
                avtorji.append(avtor(tvit))
                break
    return sorted(unikati(avtorji))


def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            if oseba2 in se_zacne_z(tvit, "@"):
                return True
        if avtor(tvit) == oseba2:
            if oseba1 in se_zacne_z(tvit, "@"):
                return True


