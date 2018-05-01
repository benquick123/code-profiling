#funkcije iz prejšnje naloge:
def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    imena = []
    for tvit in tviti:
        imena.append(avtor(tvit))
    return unikati(imena)

def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    besede = []
    for beseda in tvit.split():
        if beseda[0] == c:
            besede.append(izloci_besedo(beseda))
    return besede

def zberi_se_zacne_z(tviti, c):
    afne = []
    for tvit in tviti:
        afne += se_zacne_z(tvit, c)
    return unikati(afne)

def vse_afne(tviti):
    return unikati(zberi_se_zacne_z(tviti, "@"))

def vsi_hashtagi(tviti):
    return unikati(zberi_se_zacne_z(tviti, "#"))

def vse_osebe(tviti):
    osebe = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    osebe.sort()
    return osebe

#funkcije za to nalogo:
def besedilo(tvit):
    return tvit.split(": ", 1)[1]

def zadnji_tvit(tviti):
    zadnji = {}
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        zadnji[avtor_tvita] = besedilo(tvit)
    return zadnji

def prvi_tvit(tviti):
    prvi ={}
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        if avtor_tvita not in prvi:
            prvi[avtor_tvita] = besedilo(tvit)
    return prvi

def prestej_tvite(tviti):
    stevilo_tvitov = {}
    for tvit in tviti:
        stevilo_tvitov[avtor(tvit)] = 0
    for tvit in tviti:
        stevilo_tvitov[avtor(tvit)] += 1
    return stevilo_tvitov

def omembe(tviti):
    pregledani_avtorji = []
    omenjeni_avtorji = {}
    for tvit in tviti:
        if avtor(tvit) not in pregledani_avtorji:
            omenjeni_avtorji[avtor(tvit)] = vse_osebe(avtor(tvit), tviti)
        pregledani_avtorji.append(avtor(tvit))
    return omenjeni_avtorji


def neomembe(ime, omembe):
    omenjeni_avtorji = []
    neomenjeni_avtorji = []
    for avtor in omembe:
        omenjeni_avtorji.append(avtor)
    for pisec in omenjeni_avtorji:
        if pisec not in omembe[ime] and pisec != ime:
            neomenjeni_avtorji.append(pisec)
    return neomenjeni_avtorji




