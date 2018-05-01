def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t

def avtor(tvit):
    return tvit.split(":")[0]

def se_zacne_z(tvit, c):
    besede = []
    for beseda in tvit.split():
        if beseda[0] == "@":
            besede.append(izloci_besedo(beseda))
    return besede

def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def zberi_se_zacne_z(tviti, c):
    afne = []
    for tvit in tviti:
        afne += se_zacne_z(tvit, "@")
    return unikati(afne)

def vse_afne(tviti):
    afne = []
    for tvit in tviti:
        afne += se_zacne_z(tvit, "@")

    return (zberi_se_zacne_z(tviti, "@"))



def besedilo(tvit):
    a = tvit.split()
    for w in a:
        a = a[1:]
        s = ' '.join(a)
        return s

def zadnji_tvit(tviti):
    seznam = {}
    for tvit in tviti:
        a = avtor(tvit)
        b = besedilo(tvit)
        if b not in seznam:
            seznam[a] = ""
            seznam[a] = b
        else:
            seznam[a] = b
    return seznam

def prvi_tvit(tviti):
    seznam = {}
    for tvit in tviti:
        a = avtor(tvit)
        b = besedilo(tvit)
        if a not in seznam:
            seznam[a] = ""
            seznam[a] = b
    return seznam

def prestej_tvite(tviti):
    norek = {}
    for text in tviti:
        a = text.split()
        c = text.split(":")[0]
        if c not in norek:
            norek[c] = 0
        norek[c] += 1
    return norek


def omembe(tviti):
    avtorji = {}
    for tvit in tviti:
        a = avtor(tvit)
        b = besedilo(tvit)
        c = vse_afne(tvit)
        d = se_zacne_z(tvit, "@")
        if a not in avtorji:
            avtorji[a] = []
        avtorji[a] += se_zacne_z(tvit, "@")

    return avtorji

def neomembe(ime, omembe):
    seznam = []
    omenjeni = []
    pisatelji = []
    for pisatelj, oznacen in omembe.items():
        if pisatelj not in pisatelji:
            pisatelji.append(pisatelj)
        if pisatelj == ime:
            omenjeni += omembe[ime]
    for p in pisatelji:
        if p not in omenjeni:
            seznam.append(p)
        if ime in seznam:
            seznam.remove(ime)
    return seznam


