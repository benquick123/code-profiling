import collections

def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t

def avtor(tvit):
    ime = ""
    i=0
    while tvit[i] != ":":
        ime += tvit[i]
        i+=1
    return ime

def vse_afne(tviti):
    a = []
    for e in tviti:
        beseda = se_zacne_z(e, "@")
        for e in beseda:
            a.append(e)
            a = unikati(a)
    return a

def se_zacne_z(tvit, c):
    besede_a =[]
    tvit = tvit.split()
    for a in tvit:
        for b in a:
            if b ==c:
                beseda =izloci_besedo(a)
                besede_a.append(beseda)
    return  besede_a

def izloci_besedo(beseda):
    for beseda_n in beseda:
        if beseda_n.isalnum():
            break
        else:
            beseda = beseda.lstrip(beseda_n[0])
    for beseda_n in beseda[::-1]:
        if beseda_n.isalnum():
            break
        else:
            beseda = beseda.rstrip(beseda_n[-1])
    return beseda

######

def besedilo(tvit):
    mesto = tvit.find(":")
    tekst = tvit[mesto+2:]
    return tekst

def zadnji_tvit(tviti):
    s =collections.defaultdict(list)
    for tvit in tviti:
        ime = avtor(tvit)
        vsebina = besedilo(tvit)
        s[ime] = vsebina
    return (s)

def prvi_tvit(tviti):
    s =collections.defaultdict(list)
    for tvit in tviti:
        ime = avtor(tvit)
        vsebina = besedilo(tvit)
        if ime not in s:
            s[ime] = vsebina
    return s

def prestej_tvite(tviti):
    s = collections.defaultdict(list)
    for tvit in tviti:
        ime = avtor(tvit)
        if ime not in s:
            s[ime] = 1
        else:
            s[ime] +=1
    return s

def omembe(tviti):
    s = collections.defaultdict(list)
    for tvit in tviti:
        ime = avtor(tvit)
        imena = se_zacne_z(tvit, "@")
        for omenjen in imena:
            s[ime].append(omenjen)
        if imena == []:
            s[ime] =[]
    return s

def neomembe(ime, omembe):
    s = []
    b = set(omembe[ime])
    for neomenjen in omembe:
        if ime not in neomenjen:
            if neomenjen not in b:
                s.append(neomenjen)
    return s


