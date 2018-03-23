def unikati(s):
    a = []
    for x in s:
        if x not in a:
            a.append(x)
    return a

def avtor(s):
    a = s.split()
    for b in a:
        if b.count(":") > 0:
            return b[:-1]

def vsi_avtorji(s):
    x = []
    for a in s:
        b = avtor(a)
        if b not in x:
            x.append(b)
    return x

def izloci_besedo(beseda):
    beseda = list(beseda)
    while not beseda[0].isalnum():
        beseda.pop(0)
    while not beseda[-1].isalnum():
        beseda.pop(-1)
    return "".join(beseda)

def se_zacne_z(tvit,c):
    x = []
    tvit = tvit.split()
    for z in tvit:
        if c in z:
            x.append(izloci_besedo(z))
    return x

def zberi_se_zacne_z(tviti,c):
    z = []
    for x in tviti:
        y = se_zacne_z(x,c)
        z.extend(y)
    q = unikati(z)
    return q

def vse_afne(tviti):
    z = []
    for x in tviti:
        y = se_zacne_z(x,"@")
        z.extend(y)
    q = unikati(z)
    return q

def vsi_hashtagi(tviti):
    z = []
    for x in tviti:
        y = se_zacne_z(x,"#")
        z.extend(y)
    q = unikati(z)
    return q

def vse_osebe(tviti):
    x = []
    a = vse_afne(tviti)
    b = vsi_avtorji(tviti)
    x.extend(a)
    x.extend(b)
    x = unikati(x)
    while None in x:
        x.remove(none)
    x.sort()
    return x

def besedilo(tvit):
    seznam = []
    tvit = tvit.split()
    a = tvit.pop(0)
    seznam = dict(seznam)
    seznam[a] = " ".join(tvit)
    return seznam[a]


def zadnji_tvit(tviti):
    rezultat = []
    rezultat = dict(rezultat)
    for x in tviti:
        rezultat[avtor(x)] = besedilo(x)
    return rezultat

def prvi_tvit(tviti):
    rezultat = []
    rezultat = dict(rezultat)
    for x in tviti:
        y = avtor(x)
        if y not in rezultat:
            rezultat[y] = besedilo(x)
    return rezultat

def prestej_tvite(tviti):
    rezultat = []
    rezultat = dict(rezultat)
    for x in tviti:
        y = avtor(x)
        if y not in rezultat:
            rezultat[y] = 1
        else:
            rezultat[y] = rezultat[y] + 1
    return rezultat

def omembe(tviti):
    rezultat = []
    rezultat = dict(rezultat)
    for x in tviti:
        y = avtor(x)
        if y not in rezultat:
            rezultat[y] = []
        rezultat[y].extend(se_zacne_z(x,"@"))
    return rezultat

def neomembe(ime,omembe):
    ljudje = list(omembe.keys())
    ljudje.remove(ime)
    for x in omembe[ime]:
        if x in ljudje:
            ljudje.remove(x)
    return ljudje


def se_poznata(ime1, ime2, omembe):
    if ime1 not in omembe or ime2 not in omembe:
        return False
    elif ime1 in omembe[ime2] or ime2 in omembe[ime1]:
        return True
    else:
        return False

def hashtagi(tviti):
    rezultat = []
    rezultat = dict(rezultat)
    for x in tviti:
        h = se_zacne_z(x, "#")
        print(avtor(x), h)
        for y in h:
            if y not in rezultat:
                rezultat[y] = []
            rezultat[y].append(avtor(x))
    for x in rezultat:
        b = rezultat[x]
        b = sorted(b)
        rezultat[x] = b
    return rezultat



