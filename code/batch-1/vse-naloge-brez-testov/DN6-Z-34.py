#funkcije iz prejšnje domače naloge

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


#obvezna domača naloga:

import collections

def besedilo (tvit):
    tekst = tvit.split(":")[1:]
    return ":".join(tekst).strip()

def zadnji_tvit(tviti):
    sl = collections.defaultdict()
    for e in tviti:
        sl[avtor(e)] = besedilo(e)
    return sl

def prvi_tvit(tviti):
    prvi = []
    sl = collections.defaultdict()
    for e in tviti:
        if avtor(e) not in prvi:
            sl[avtor(e)] = besedilo(e)
            prvi.append(avtor(e))
    return sl

def prestej_tvite(tviti):
    sl = collections.defaultdict(int)
    for e in tviti:
        sl[avtor(e)] +=1
    return sl

def omembe (tviti):
    sl = collections.defaultdict(list)
    for e in tviti:
        tekst = e.split()
        a = avtor(e)
        if a not in sl:
            sl[a]= []
        for i in tekst:
            if i[0]=="@":
                ime=izloci_besedo(i)
                sl[a].append(ime)
    return sl

def neomembe(ime, omembe):
    s = []
    ne = []
    for e in omembe:
        s.append(e)
    for i in s:
        if i not in omembe[ime] and ime != i:
            ne.append(i)
    return ne




