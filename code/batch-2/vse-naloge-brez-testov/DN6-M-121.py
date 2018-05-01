def besedilo(tvit):
    novi = tvit.split(" ")
    del(novi[0])
    return " ".join(novi)

def zadnji_tvit(tviti):
    d = {}
    for tvit in tviti:
        d[avtor(tvit)]=besedilo(tvit)
    return d

def avtor(tvit):
    avtorcek = ''
    for i in tvit:
        if i == ":":
            break
        else:
            avtorcek += i
    return avtorcek

def prvi_tvit(tviti):
    d = {}
    for tvit in tviti:
        if avtor(tvit) not in d:
            d[avtor(tvit)] = besedilo(tvit)
    return d

def prestej_tvite(tviti):
    d = {}
    for tvit in tviti:
        if (avtor(tvit)) not in d:
            d[avtor(tvit)] = 1
        else:
            d[avtor(tvit)]+=1
    return d

def izloci_besedo(beseda):
    prazn=''
    b = list(beseda)
    while True:
        if not b[0].isalnum():
            del (b[0])
        else:
            break
    while True:
        if not b[-1].isalnum():
            del (b[-1])
        else:
            break
    for c in b:
        prazn +=c
    return prazn

def se_zacne_z(tvit, c):
    d=''
    seznam = []
    tweet = tvit.split(" ")
    for beseda in tweet:
        if beseda[0]==c:
            d=izloci_besedo(beseda)
            seznam.append(d)
    return seznam


def omembe(tviti):
    d={}
    for tvit in tviti:
        d[avtor(tvit)] = []
    for tvit in tviti:
        seznam_o = se_zacne_z(tvit, '@')
        for o in seznam_o:
            d[avtor(tvit)].append(o)

    return d

def neomembe(ime, omembe):
    vsi = []
    omenjeni=[]
    neomenjeni=[]
    for a, o in omembe.items():
        vsi.append(a)
        if a == ime:
            omenjeni = o
    for n in vsi:
        if n not in omenjeni and n != ime:
            neomenjeni.append(n)
    return neomenjeni



