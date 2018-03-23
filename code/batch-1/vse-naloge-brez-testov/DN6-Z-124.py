import collections


def unikati(s):
    novi = []
    for element in s:
        if element not in novi:
            novi.append(element)
    return novi

def avtor(tvit):
    s = tvit.find(":")
    return tvit[:s]

def vsi_avtorji(tviti):
    seznam = []
    for s in tviti:
        seznam.append(avtor(s))
    return unikati(seznam)

def izloci_besedo(beseda):
    i = 0
    while beseda[i].isalnum() == False:
        i += 1
    j = -1
    while beseda[j].isalnum() == False:
        j -= 1
    if j == -1:
        j = len(beseda)
    else:
        j += 1
    return beseda[i:j]

def se_zacne_z(tvit, c):
    seznam = []
    s = tvit.split()
    for beseda in s:
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
    osebe = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    return sorted(osebe)

def besedilo(tvit):
    s = tvit.split(":")[1:]
    return ":".join(s).strip()

def zadnji_tvit(tviti):
    slovar = collections.defaultdict()
    for tvit in tviti:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = collections.defaultdict()
    pisci = []
    for tvit in tviti:
        if avtor(tvit) not in pisci:
            slovar[avtor(tvit)] = besedilo(tvit)
            pisci.append(avtor(tvit))
    return slovar

def prestej_tvite(tviti):
    slovar = collections.defaultdict(int)
    for tvit in tviti:
        slovar[avtor(tvit)] += 1
    return slovar

def omembe(tviti):
    slovar = collections.defaultdict(list)
    for tvit in tviti:
        s = tvit.split()
        av = avtor(tvit)
        if av not in slovar:
            slovar[av] = []
        for beseda in s:
            if beseda[0] == "@":
                ime = izloci_besedo(beseda)
                slovar[av].append(ime)
    return slovar

def neomembe(ime, omembe):
    seznam = []
    neomenjeni = []
    for a in omembe:
        seznam.append(a)
    for avtor in seznam:
        if avtor not in omembe[ime] and ime != avtor:
            neomenjeni.append(avtor)
    return neomenjeni

def se_poznata(ime1, ime2, omembe):
    if ime1 not in omembe or ime2 not in omembe:
        return False
    if ime1 in omembe[ime2] or ime2 in omembe[ime1]:
        return True
    return False

def hashtagi(tviti):
    slovar = collections.defaultdict(list)
    for tvit in tviti:
        s = tvit.split()
        for beseda in s:
            if beseda[0] == "#":
                hash = izloci_besedo(beseda)
                av = avtor(tvit)
                slovar[hash].append(av)
                slovar[hash].sort()
    return slovar

