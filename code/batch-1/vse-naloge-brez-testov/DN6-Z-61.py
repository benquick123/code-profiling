def avtor (tvit):
    return tvit.split(":")[0]

def besedilo (tvit):
    return tvit [tvit.find(":")+2:]

def zadnji_tvit (tviti):
     zt = dict()
     for tvit in tviti:
         zt[avtor(tvit)] = besedilo(tvit)
     return zt

def prvi_tvit (tviti):
    pt = dict()
    for tvit in tviti:
        if avtor(tvit) not in pt:
            pt[avtor(tvit)] = besedilo(tvit)
    return pt

def prestej_tvite (tviti):
    st = dict()
    for tvit in tviti:
        if avtor(tvit) not in st:
            st[avtor(tvit)] = 1
        else:
            st[avtor(tvit)] += 1
    return st

def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t

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

def vsi_avtorji(tviti):
    return unikati(avtor(tvit) for tvit in tviti)

def omembe (tviti):
    om = {}
    for tvit in tviti:
        if avtor(tvit) not in om:
            om[avtor(tvit)] = se_zacne_z(tvit, '@')
        else:
            om[avtor(tvit)] += se_zacne_z(tvit,'@')
    return om

def neomembe (ime, omembe):
    neom = []
    for a in list(omembe):
        if a not in omembe[ime]:
            neom.append(a)
    neom.remove(ime)
    return neom

def se_poznata(ime1, ime2, omembe):
    return ime2 in list(omembe[ime1]) or ime1 in list(omembe[ime2])

