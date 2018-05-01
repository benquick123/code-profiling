def unikati(s):
    t = s[:]
    i = 0
    while i < len(t):
        if t[i] in t[:i]:
            del t[i]
        else:
            i += 1
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
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))



def besedilo(tvit):
    xx = tvit.split(avtor(tvit))[1]
    return xx.lstrip(": ")

def zadnji_tvit(tviti):
    slovar = {}
    for x in tviti:                          # za vsak tvit
        slovar[avtor(x)] = besedilo(x)              #avtorji = avtor(x)   # dobimo avtorja      #tvitek = besedilo(x)     #slovar[avtorji] = tvitek
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
    slovar = {}
    for x in tviti:
        if avtor(x) not in slovar:
            slovar[avtor(x)] = []
        slovar[avtor(x)].extend(se_zacne_z(x, "@"))
    return slovar

def neomembe(ime, omembe):
    seznam = []
    omem = omembe[ime]
    for avt in omembe:
        if avt != ime:
            seznam.append(avt)
    return [x for x in seznam if x not in omem]

def se_poznata(ime1, ime2, omembe):
    if ime1 not in omembe:
        omembe[ime1] = []
    if ime2 not in omembe:
        omembe[ime2] = []
    prvi = omembe[ime1]
    druzgi = omembe[ime2]
    if ime1 in druzgi or ime2 in prvi:
        return True
    return False

def hashtagi(tviti):
    slovar = {}
    for tvit in tviti:
        hash = vsi_hashtagi(tviti)
        avto = avtor(tvit)
        for ha in hash:
            if ha not in slovar:
                slovar[ha] = []
            if ha in tvit:
                slovar[ha].append(avto)
            slovar[ha] = sorted(slovar[ha])
    return slovar


