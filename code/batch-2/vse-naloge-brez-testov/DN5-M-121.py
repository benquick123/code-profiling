def unikati(s):
    seznam=[]
    for i in s:
        if (i in seznam)== False:
            seznam.append(i)

    return seznam

def avtor(tvit):
    avtorcek=''
    for i in tvit:
        if i == ":":
            break
        else:
            avtorcek+=i
    return avtorcek

def vsi_avtorji(tviti):
    av=''
    seznam = []
    for i in tviti:
        av = avtor(i)
        seznam.append(av)

    return unikati(seznam)

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

def zberi_se_zacne_z(tviti, c):
    d = ''
    seznam = []
    for tvit in tviti:
        tvit = tvit.split(" ")
        for b in tvit:
            if b[0]==c:
                d=izloci_besedo(b)
                if d not in seznam:
                    seznam.append(d)
    return seznam

def vse_afne(tviti):
    c='@'
    return zberi_se_zacne_z(tviti, c)

def vsi_hashtagi(tviti):
    c='#'
    return zberi_se_zacne_z(tviti, c)

def vse_osebe(tviti):
    seznam = []
    seznam = vse_afne(tviti)
    for tvit in tviti:
        seznam.append(avtor(tvit))
    seznam = unikati(seznam)
    seznam.sort()
    return seznam





