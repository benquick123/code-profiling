import collections

def unikati(s):
    xs = []
    for i in s:
        for t in xs:
            if t == i:
                break
        else:
            xs.append(i)
    return xs

def avtor(tvit):
    k = tvit.find(":")
    return tvit[0:k:1]

def vsi_avtorji(tviti):
    pwn = []
    for i in tviti:
        p = avtor(i)
        pwn.append(p)
    return unikati(pwn)

def izloci_besedo (beseda):
    for i in range(len(beseda)):
        if beseda[i].isalnum():
            break
    for j in range(len(beseda), 0, -1):
        if beseda[j-1].isalnum():
            break
    return beseda[i:j]

def se_zacne_z(tvit, c):
    xs = []
    s = tvit.split()
    for i in s:
        if i.startswith(c):
            hash = izloci_besedo(i)
            xs.append(hash)
    return xs

def zberi_se_zacne_z(tviti,c):
    xs = []
    for tvit in tviti:
        for x in se_zacne_z(tvit,c):
            xs.append(x)
    return unikati(xs)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def besedilo(tvit):
    k = tvit.find(":")
    return tvit[k+2::1]

def zadnji_tvit(tviti):
    slovar = {}
    for i in tviti:
        slovar[avtor(i)] = besedilo(i)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for i in tviti:
        key = avtor(i)
        vrednost = besedilo(i)
        if key not in slovar:
            slovar[key] = vrednost
    return slovar

def prestej_tvite(tviti):
    avtorji = []
    for i in tviti:
        avtorji.append(avtor(i))
    return (collections.Counter(avtorji))

def omembe(tviti):
    slovar = {}
    for i in tviti:
        key = avtor(i)
        vrednost = se_zacne_z(i,"@")
        if key not in slovar:
            slovar[key] = vrednost
        else:
            for x in vrednost:
                slovar[key].append(x)
    return slovar

def neomembe (ime,omembe):
    avtorji = []
    seznam = []
    for i in omembe:
          avtorji.append(i)
    if ime in omembe:
        cveke = omembe[ime]
        for x in avtorji:
            if x not in cveke and x != ime:
                seznam.append(x)
    return seznam

