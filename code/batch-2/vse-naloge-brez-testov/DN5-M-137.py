def unikati(s):
    seznam = []
    for i in s:
        if i in seznam:
            continue
        else:
            seznam.append(i)
    return seznam

def avtor(tvit):
    a = tvit.split()
    b = a[0]
    c = b[:-1]
    return c

def vsi_avtorji(tviti):
    s = []
    for i in tviti:
        a = avtor(i)
        if a not in s:
            s.append(a)
    return s

def izloci_besedo(beseda):
    for i in range(len(beseda) - 1):
        if beseda[i].isalnum():
            break

    for j in range(len(beseda)-1,0,-1):
        if beseda[j].isalnum():
            break
    beseda = beseda[i:j + 1]
    return beseda

def se_zacne_z(tvit, c):
    s = []
    a = tvit.split()
    beseda = ""
    for bes in a:
        if c in bes:
            for crka in bes:
                if crka.isalnum() == False:
                    continue
                else:
                    beseda = beseda + crka
            s.append(beseda)
            beseda = ""
        else:
            continue
    return s

def zberi_se_zacne_z(tviti, c):
    s = []
    for tvit in tviti:
        for beseda in tvit:
            a = se_zacne_z(tvit, c)
            for b in a:
                if b not in s and b!=[]:
                    s.append(b)

    return s

def vse_afne(tviti):
    s = []
    a = zberi_se_zacne_z(tviti, "@")
    b = vsi_avtorji(tviti)
    for i in a:
        for j in b:
            if j not in a:
                s.append(j)

    return a

def vsi_hashtagi(tviti):
    a = zberi_se_zacne_z(tviti, "#")
    return a

def vse_osebe(tviti):
    a = zberi_se_zacne_z(tviti, "@")
    b = vsi_avtorji(tviti)

    for i in a:
        for j in b:
            if j not in a:
                a.append(j)
    a = sorted(a)
    return a

#dodatna
def custva(tviti, hashtagi):
    s = []
    for b in hashtagi:
        for tvit in tviti:
            a = tvit.split()
            for c in a:
                if b == c[1:]:
                    if avtor(tvit) not in s:
                        s.append(avtor(tvit))
    return sorted(s)

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        a = tvit.split()
        g = a[1:]
        for b in g:
            if avtor(tvit) == oseba1:
                if oseba2 == izloci_besedo(b) and izloci_besedo(b) in vse_osebe(tviti):
                    return True
            elif avtor(tvit) == oseba2 and izloci_besedo(b) in vse_osebe(tviti):
                if oseba1 == izloci_besedo(b):
                    return True
    return False







