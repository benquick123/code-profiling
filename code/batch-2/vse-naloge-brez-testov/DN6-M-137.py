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

#domaca naloga

def besedilo(tvit):
    a = tvit.split(": ")
    c = ""
    for i in range(len(a)):
        if i > 1:
            c += ": "
        if i != 0:
            c += a[i]
    return c

def zadnji_tvit(tviti):
    a = {}
    for tvit in tviti:
        a[avtor(tvit)] = besedilo(tvit)
    return a


def prvi_tvit(tviti):
    a = {}
    for tvit in tviti:
        if avtor(tvit) not in a:
            a[avtor(tvit)] = besedilo(tvit)
    return a

import collections

def prestej_tvite(tviti):
    seznam = []
    for tvit in tviti:
        seznam.append(avtor(tvit))
    return collections.Counter(seznam)

def omembe(tviti):
    s = collections.defaultdict(list)
    for tvit in tviti:
        s[avtor(tvit)] += se_zacne_z(tvit, "@")

    return s

def neomembe(ime, omembe):
    s =[]
    for a in omembe:
        if ime == a:
            for c in omembe:
                if c not in omembe[a] and c != ime and c not in s:
                    s.append(c)
            break
    return s

#dodatna
def se_poznata(ime1, ime2, omembe):
    for a in omembe:
        if a == ime1:
            for b in omembe[a]:
                if ime2 == b:
                    return True
        if a == ime2:
            for b in omembe[a]:
                if ime1 == b:
                    return True
    return False

def hashtagi(tviti):
    s = collections.defaultdict(list)
    for tvit in tviti:
        s[se_zacne_z(tvit, "#")[0]] += [avtor(tvit)]
        if len(se_zacne_z(tvit, "#")) > 1:
            s[se_zacne_z(tvit, "#")[1]] += [avtor(tvit)]
    t = {x:sorted(s[x]) for x in s.keys()}
    return t

