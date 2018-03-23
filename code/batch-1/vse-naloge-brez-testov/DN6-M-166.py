def unikati(s):
    s2 = []
    for e in s:
        if e not in s2:
            s2.append(e)
    return s2

def avtor(tvit):
    x = tvit.split(":")
    return x [0]

def vsi_avtorji(tviti):
    seznam_a = []
    for tvit in tviti:
        y = avtor(tvit)
        seznam_a.append(y)
    z = unikati(seznam_a)
    return z

def avtorji_brez_unikatov(tviti):
    seznam_a = []
    for tvit in tviti:
        y = avtor(tvit)
        seznam_a.append(y)
    return seznam_a

def izloci_besedo(beseda):
    while str.isalnum(beseda [0]) == False:
     beseda = beseda[1:]
    while str.isalnum(beseda [-1]) == False:
     beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    s = tvit.split()
    z = []
    for e in s:
        if e [0] == c:
            z.append(e)
    a = []
    for i in z:
        b = izloci_besedo(i)
        a.append(b)
    return a

def zberi_se_zacne_z (tviti,c):
    a =". ".join(tviti)
    b = se_zacne_z(a,c)
    return unikati(b)


def vse_afne(tviti):
    return zberi_se_zacne_z (tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z (tviti, "#")

def vse_osebe(tviti):
    s = vsi_avtorji(tviti) + vse_afne(tviti)
    return sorted(unikati(s))

def custva (tviti, hashtagi):
    b = []
    for e in hashtagi:
        b.append(izloci_besedo(e))
    c = []
    for tvit in tviti:
        a = se_zacne_z(tvit,"#")
        if len (set(b).intersection(a)) > 0:
            c.append(avtor(tvit))
    return sorted(unikati(c))


def besedilo(tvit):
    x = tvit.split(":")
    if len (x) < 3:
        a = x [1]
        return a.strip()
    else:
        c = x [1:]
        a = ":".join(c)
        return a.strip()


def zadnji_tvit(tviti):
    slovar_tvitov = {}
    for tvit in tviti:
        slovar_tvitov[avtor(tvit)] = besedilo(tvit)
    return slovar_tvitov

def prvi_tvit(tviti):
    obrnjen_slovar = {}
    for tvit in reversed(tviti):
        obrnjen_slovar[avtor(tvit)] = besedilo(tvit)
    return obrnjen_slovar

def prestej_tvite(tviti):
    pogostosti = {}
    for ime in avtorji_brez_unikatov(tviti):
        if ime not in pogostosti:
         pogostosti[ime] = 0
        pogostosti[ime] += 1
    return pogostosti


def omembe(tviti):
    omembe1 = {}
    for tvit in tviti:
         if avtor(tvit) not in omembe1:
            omembe1[avtor(tvit)]= se_zacne_z(tvit, "@")
         else:
            omembe1[avtor(tvit)].extend(se_zacne_z(tvit,"@"))
    return omembe1

def neomembe(ime, omembe):
        s = []
        for oseba in omembe:
            if oseba not in omembe[ime] and oseba != ime:
                s.append(oseba)
        return s

def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe.get(ime2, []) \
        or ime2 in omembe.get(ime1, []):
        return True
    return False



def hashtagi(tviti):
    sh = {}
    for hash in vsi_hashtagi(tviti):
        s = []
        for tvit in tviti:
            if hash in besedilo(tvit):
                s.append(avtor(tvit))
        sh[hash] = sorted(s)
    return sh













