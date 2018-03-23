import collections


def unikati(s):
    seznam = []
    for x in s:
        if x not in seznam:
            seznam.append(x)
    return seznam

def avtor(tvit):
    return (tvit.split(":")[0])

def vsi_avtorji(tviti):
    seznam = []
    for x in tviti:
        seznam.append(avtor(x))
    return unikati(seznam)

def izloci_besedo(beseda):
    for x in beseda:
        if x.isalnum():
            prvi = beseda.index(x)
            break

    for y in range(len(beseda)-1,0,-1):
        if beseda[y].isalnum():
            zadnji = y+1
            break

    return beseda[prvi:zadnji]

def se_zacne_z(tvit,c):
    seznam = tvit.split()
    seznam2 = []
    for x in seznam:
        if c in x:
            seznam2.append(izloci_besedo(x))

    return seznam2

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for x in tviti:
        if len(se_zacne_z(x,c)) != 0:
            seznam.extend(se_zacne_z(x,c))

    return unikati(seznam)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    seznam = []
    for x in tviti:
        seznam.append(avtor(x))
    seznam.extend(vse_afne(tviti))

    return sorted(unikati(seznam))

############################################################

def besedilo(tvit):
    for x in tvit:
        if x == ":":
            st = tvit.index(x) + 2
            break

    return tvit[st:]

def zadnji_tvit(tviti):
    slovar = {}

    for x in tviti:
        slovar[avtor(x)] = besedilo(x)

    return slovar

def prvi_tvit(tviti):
    slovar = {}

    for x in tviti:
        if avtor(x) not in slovar:
            slovar[avtor(x)] = besedilo(x)

    return slovar

def prestej_tvite(tviti):
    slovar = {}

    for x in tviti:
        if avtor(x) not in slovar:
            slovar[avtor(x)] = 1
        else:
            slovar[avtor(x)] += 1

    return slovar


def omembe(tviti):
    slovar = collections.defaultdict(str)

    for x in tviti:
        if avtor(x) not in slovar:
            slovar[avtor(x)] = se_zacne_z(x,"@")
        else:
            slovar[avtor(x)].extend(se_zacne_z(x,"@"))

    return slovar


def neomembe(ime,omembe):
    seznam = []

    for x in omembe:
        if x not in omembe[ime]:
            seznam.append(x)

    seznam.remove(ime)
    return seznam


