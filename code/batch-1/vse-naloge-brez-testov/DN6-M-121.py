def unikati(s):
    a = []
    for x in s:
        if x in a:
            continue
        else:
            a.append(x)
    return a

def avtor(tvit):
    a = tvit.split()
    for b in a:
        if b.find(":") > 0:
            b = b.replace(":","")
            return b

def vsi_avtorji(tviti):
    a = []
    for b in tviti:
        c = avtor(b)
        a.append(c)
    d = unikati(a)
    return d

def izloci_besedo(beseda):
    a = 0
    while beseda[a].isalnum() == False:
        b =  beseda.replace(beseda[a],"")
        beseda = b
    cec = beseda[::-1]
    while cec[a].isalnum() == False:
        cec = cec.replace(cec[a],"")
    d = cec[::-1]
    return d

def se_zacne_z(tvit, c):
    s = []
    lol = tvit.split()
    for a in lol:
        if a.startswith(c):
            x = izloci_besedo(a)
            beseda = x
            s.append(beseda)

    return s

def zberi_se_zacne_z(tviti, c):
    zum = []
    for b in tviti:
        b = b.split()
        for lul in b:
            if c in lul:
                zam = lul.replace(c, "")
                zam = izloci_besedo(zam)
                if zam in zum:
                    continue
                else:
                    zum.append(zam)
    return zum

def vse_afne(tviti):
    a = zberi_se_zacne_z(tviti, "@" )
    return a

def vsi_hashtagi(tviti):
    a = zberi_se_zacne_z(tviti, "#" )
    return a

def vse_osebe(tviti):
    zac = []
    avt = vsi_avtorji(tviti)
    if avt not in zac:
        zac.extend(avt)
    afn = vse_afne(tviti)
    for rac in afn:
        if rac in zac:
            continue
        else:
            zac.append(rac)
    zac.sort()
    print(zac)
    return zac

#________________________________________________________________________________________________

def besedilo(tvit):
    avto = avtor(tvit)
    a = tvit.split(avto)[1]
    return a.lstrip(": ")

def zadnji_tvit(tviti):
    slovar = {}
    for a in tviti:
        c = avtor(a)
        d = besedilo(a)
        slovar[c] = d
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for x in tviti:
        if avtor(x) not in slovar:
            c = avtor(x)
            d = besedilo(x)
            slovar[c] = d
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    for x in tviti:
        a = avtor(x)
        if a not in slovar:
            slovar[a] = 0
        slovar[a] += 1
    return slovar

def omembe(tviti):
    slovar = {}
    for x in tviti:
        kljuc = avtor(x)
        a = se_zacne_z(x, "@")
        if kljuc in slovar:
            slovar[kljuc].extend(a)
        else:
            slovar[kljuc] = a
    return slovar

def neomembe(ime, omembe):
    s = []
    a = omembe.get(ime)
    for x in omembe.keys():
        if x == ime:
            continue
        if x not in a:
            s.append(x)
    return s

