# Funkcije iz prejšnje naloge

def unikati(s):
    seznam = []
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    seznam = []
    for i in tviti:
        a = avtor(i)
        seznam.append(a)
    return unikati(seznam)

def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    besede = tvit.split()
    seznam_besed = []
    for b in besede:
        if b[0] == c:
            seznam_besed.append(izloci_besedo(b))
    return seznam_besed

def zberi_se_zacne_z(tviti, c):
    s = []
    for i in tviti:
        s = s + se_zacne_z(i, c)
    return unikati(s)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    seznam_oseb = vsi_avtorji(tviti) + vse_afne(tviti)
    return sorted(unikati(seznam_oseb))

# Obvezna naloga

def besedilo(tvit):
    a = tvit.split(": ")
    rezultat = ""
    for i in range(len(a)):
        if i > 1:
            rezultat += ": "
        if i != 0:
            rezultat += a[i]
    return rezultat

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

import collections

def prestej_tvite(tviti):
    seznam_avtorjev = []
    for tvit in tviti:
        seznam_avtorjev.append(avtor(tvit))

    return collections.Counter(seznam_avtorjev)


def omembe(tviti):
    slovar = collections.defaultdict(list)
    for tvit in tviti:
        slovar[avtor(tvit)] += (se_zacne_z(tvit, "@"))
    return slovar

def neomembe(ime, omembe):
    seznam_neomenjenih = []
    for avtor in omembe:
        if ime == avtor:
            for omenjen in omembe:
                if omenjen not in omembe[avtor] and omenjen != ime and omenjen not in seznam_neomenjenih:
                    seznam_neomenjenih.append(omenjen)
            break
    return seznam_neomenjenih

# Dodatni del

def se_poznata(ime1, ime2, omembe):
    for prvi in omembe:
        if prvi == ime1:
            for drugi in omembe[prvi]:
                if drugi == ime2:
                    return True
        if prvi == ime2:
            for drugi in omembe[prvi]:
                if drugi == ime1:
                    return True
    return False

def hashtagi(tviti):
    slovar = collections.defaultdict(list)
    for tvit in tviti:
        slovar[se_zacne_z(tvit, "#")[0]] += [avtor(tvit)]
        if len(se_zacne_z(tvit, "#")) > 1:
            slovar[se_zacne_z(tvit, "#")[1]] += [avtor(tvit)]
        urejeni_slovar = {i: sorted(slovar[i]) for i in slovar.keys()}
    return urejeni_slovar

