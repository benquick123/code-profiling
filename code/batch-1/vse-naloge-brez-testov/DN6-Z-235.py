# Obvezna naloga

# 1.
def besedilo(tvit):
    return tvit[tvit.find(":")+2:]

# 2.
def zadnji_tvit(tviti):
    d = {}
    for e in tviti[::-1]:
        kljuc = e[:e.find(":")]
        vrednost = besedilo(e)
        if kljuc not in d:
            d[kljuc]=vrednost
    return d

# 3.
def prvi_tvit(tviti):
    d = {}
    for e in tviti:
        kljuc = e[:e.find(":")]
        vrednost = besedilo(e)
        if kljuc not in d:
            d[kljuc]=vrednost
    return d

# 4.
import collections
def avtor(tvit):
    return tvit.split(":")[0]

def prestej_tvite(tviti):
    slovar = collections.Counter()
    for tvit in tviti:
        ime = avtor(tvit)
        if ime not in slovar:
            slovar[ime] = 0
        slovar[ime] += 1
    return slovar

# 5.
def izloci_besedo(beseda):
    for e in beseda[::1]:
        if not e.isalnum():
            beseda = beseda[1:]
        else:
            break
    for e in beseda[::-1]:
        if not e.isalnum():
            beseda = beseda[:-1]
        else:
            break
    return beseda

def se_zacne_z(tvit, c):
    d = []
    for e in tvit.split():
        if c == e[0]:
            d.append(izloci_besedo(e))
    return d


def omembe(tviti):
    slovar={}
    for tvit in tviti:
        ime = avtor(tvit)
        oseba = se_zacne_z(tvit, "@")
        if ime not in slovar:
            slovar[ime] = []
        for b in oseba:
            slovar[ime].append(b)
    return slovar

# 6.
def neomembe(ime, omembe):
    seznam =[]
    vsi_avtorji = omembe.keys()
    for ime2 in vsi_avtorji:
        x = omembe[ime]
        if (ime2 != ime) and (ime2 not in x):
            seznam.append(ime2)
    return seznam

# Dodatna naloga

# 1.
def se_poznata(ime1, ime2, omembe):
    x = omembe.get(ime1,[])
    y = omembe.get(ime2,[])
    if (ime2 in x) or (ime1 in y):
        return True
    return False

# 2.
def hashtagi(tviti):
    slovar = {}
    for tvit in tviti:
        hastagi = se_zacne_z(tvit, "#")
        ime = avtor(tvit)
        for hastag in hastagi:
            if hastag not in slovar:
                slovar[hastag] = []
            slovar[hastag].append(ime)
            slovar[hastag].sort()
    return slovar

