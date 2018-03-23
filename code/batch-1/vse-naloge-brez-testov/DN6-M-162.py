def unikati(s):
    r = 0
    tab = []
    while r < len(s):
        if s[r] not in tab:
            tab.append(s[r])
        r = r+1
    return tab

def avtor(tvit):
    i = 0
    tab1 = []
    tab2 = list(tvit)
    while i < len(tab2):
        if tab2[i] != ":":
            tab1.append(tab2[i])
        else:
            break
        i=i+1
    ime = "".join(tab1)
    return ime

def vsi_avtorji(tviti):
    tab = []
    for ime in tviti:
        avt = avtor(ime)
        if avt not in tab:
            tab.append(avt)
    return tab

def izloci_besedo(beseda):
    a=False
    b=False
    bes = list(beseda)
    while a == False:
        if bes[0].isalnum() == False:
            bes = bes[1:]
        else:
            a=True
    while b==False:
        i = len(bes)-1
        if bes[i].isalnum() == False:
            bes = bes[:-1]
        else:
            b=True
    bess = "".join(bes)
    return bess

def se_zacne_z(tvit, c):
    tab = []
    tab1= []
    i=0
    besede = tvit.split(" ")
    while i < len(besede):
        bes = list(besede[i])
        if bes[0] == c:
            tab.append(besede[i])
        i=i+1
    for x in tab:
        bese = izloci_besedo(x)
        tab1.append(bese)
    return tab1

def zberi_se_zacne_z(tviti, c):
    abc = []
    for a in tviti:
        abc = abc + se_zacne_z(a, c)
    d = unikati(abc)
    return d

def vse_afne(tviti):
    abc = []
    for a in tviti:
        abc = abc + se_zacne_z(a, "@")
    d = unikati(abc)
    return d


def besedilo(tvit):
    i = 0
    tab1 = []
    tab2 = list(tvit)
    while i < len(tab2):
        if tab2[i] == ":":
            i=i+2
            while i < len(tab2):
                tab1.append(tab2[i])
                i=i+1
        i=i+1
    besedilo = "".join(tab1)
    return besedilo



def zadnji_tvit(tviti):
    s = {}
    for a in tviti:
        s[avtor(a)] = besedilo(a)
    return s

def prvi_tvit(tviti):
    s = {}
    for a in tviti:
        if avtor(a) not in s:
            s[avtor(a)] = besedilo(a)
    return s

from collections import Counter

def prestej_tvite(tviti):
    tab = []
    s = {}
    for x in tviti:
        tab.append(avtor(x))
    a = Counter(tab)
    for tvit in tviti:
        s[avtor(tvit)] = a[avtor(tvit)]
    return s

def vse_omembe_od_osebe(tviti, oseba):
    tab=[]
    i=0
    while i < len(tviti):
        if avtor(tviti[i]) == oseba:
            tab.append(besedilo(tviti[i]))
        i=i+1
    return vse_afne(tab)

def omembe(tviti):
    s={}
    i=0
    while i < len(tviti):
        if avtor(tviti[i]) not in s:
            s[avtor(tviti[i])] = vse_omembe_od_osebe(tviti, avtor(tviti[i]))
        i=i+1
    return s


def avtorji_omemb(s):
    aa = list(s.keys())
    return aa

def neomembe(ime, omembe):
    tab1 = omembe[ime]
    tab1.append(ime)
    tab2 = avtorji_omemb(omembe)
    tab3 = []
    for a in tab2:
        if a not in tab1:
            tab3.append(a)
    return tab3


