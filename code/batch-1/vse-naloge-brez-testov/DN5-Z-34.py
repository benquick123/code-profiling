#obvezna domača naloga

def unikati(s):
    xs = []
    for e in s:
        if e not in xs:
            xs.append(e)
    return xs

def avtor(tvit):
    a = tvit.find(":")
    return tvit[:a]

def vsi_avtorji(tviti):
    s1 = []
    for e in tviti:
        s1.append(avtor(e))
    return unikati(s1)

def izloci_besedo(beseda):
    m =0
    while beseda[m].isalnum() == False:
        m = m+1
    n = -1
    while beseda[n].isalnum()== False:
        n = n-1
    if n == -1:
        n = len(beseda)
    else:
        n = n+1
    return beseda[m:n]

def se_zacne_z(tvit, c):
    s =[]
    s1 = tvit.split()
    for e in s1:
        if e[0]==c:
            s.append(izloci_besedo(e))
    return s

def zberi_se_zacne_z(tviti, c):
    s2 = []
    for e in tviti:
        s2 = s2 + se_zacne_z(e,c)
    return unikati(s2)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    os = []
    os.extend(vsi_avtorji(tviti) + vse_afne(tviti))
    return sorted(unikati(os))


