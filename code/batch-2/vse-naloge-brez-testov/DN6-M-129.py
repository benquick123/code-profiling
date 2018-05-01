from collections import Counter



def unikati(s):
    t=" "
    for e in s:
        if e in t:
            continue
        t.append(e)
    return t


def avtor(tvit):
    t1=tvit.split()
    return t1[0][:-1]


def vsi_avtorji(tviti):
    z=[]
    for e in tviti:
        a = avtor(e)
        z.append(a)
    return unikati(z)


def izloci_besedo(beseda):
    t=""
    for e in beseda:
        if e.isalnum() or e == "-":
            t+=e
    return t


def se_zacne_z(tvit,c):
    z=[]
    t=tvit.split()
    for e in t:
        if e[0]==c:
            z.append(izloci_besedo(e[1:]))
    return z


def zberi_se_zacne_z(tviti,c):
    u=[]
    for tvit in tviti:
        z=se_zacne_z(tvit,c)
        for e in z:
            u.append(e)
    return unikati(u)


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")


def vse_osebe(tviti):
    u=vsi_avtorji(tviti)
    t=vse_afne(tviti)
    z=u+t
    o=unikati(z)
    r=o.sort()
    return o


def custva(tviti, hashtagi):
    t=[]
    for tvit in tviti:
        for e in hashtagi:
            if e in tvit:
                z=avtor(tvit)
                t.append(z)
    t=unikati(t)
    t.sort()
    return t


"""def se_poznata(tviti,oseba1,oseba2):
    if oseba1 and oseba2 not in vsi_avtorji(tviti):
        return False
    for tvit in tviti:
        if oseba1 in tvit:
            if oseba2 in tvit:
                return True
    else:
        return False"""

def besedilo(tvit):
    t=tvit.split()[1:]
    return " ".join(t)

def zadnji_tvit(tviti):
    slovar={}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)]=[]
        slovar[avtor(tvit)]=(besedilo(tvit))
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = []
            slovar[avtor(tvit)] = (besedilo(tvit))
    return slovar

def prestej_tvite(tviti):
    slovar={}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)]=0
        slovar[avtor(tvit)] +=1
    return slovar

def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = []
        t=tvit.split()
        for e in t:
            if "@" in e:
                e=izloci_besedo(e)
                slovar[avtor(tvit)].append(e)
    return slovar

def neomembe(ime, omembe):
    s=[]
    for e in omembe:
        if e not in omembe[ime] and e != ime:
            s.append(e)
    return s

def se_poznata(ime1, ime2, omembe):
    if ime1 not in omembe or ime2 not in omembe:
        return False
    t=neomembe(ime1, omembe)
    r=neomembe(ime2,omembe)
    if ime1 in r and ime2 in t:
        return False
    return True

def hashtagi(tviti):
    s={}
    for tvit in tviti:
        a=avtor(tvit)
        for e in tvit.split():
            if "#" in e:
                e=izloci_besedo(e)
                if e not in s:
                    s[e]=[]
                s[e].append(a)
    for r in s:
        s[r].sort()
    return s



