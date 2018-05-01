def unikati(s):
    seznam = []
    for x in s:
        if x not in seznam:
            seznam.append(x)
    return seznam


def avtor(tvit):
    x = tvit.find(":")
    return tvit[:x]


def vsi_avtorji(tviti):
    seznam = []
    for oseba in tviti:
        x = avtor(oseba)
        seznam.append(x)
    koncni_seznam = unikati(seznam)
    return koncni_seznam


def izloci_besedo(beseda):
    for x in beseda:
        if not x.isalnum():
            beseda=beseda[1:]
        else:
            break
    for x in beseda[::-1]:
        if not x.isalnum():
            beseda=beseda[:-1]
        else:
            break
    return beseda


def se_zacne_z(tvit, c):
    seznam = []
    tviti=tvit.split()
    for x in tviti:
        for y in x:
            if y==c:
                beseda=izloci_besedo(x)
                seznam.append(beseda)
    return seznam


def zberi_se_zacne_z(tviti, c):
    seznam = []
    for x in tviti:
        beseda=se_zacne_z(x,c)
        for x in beseda:
            seznam.append(x)
    seznam=unikati(seznam)
    return seznam


def vse_afne(tviti):
    seznam = []
    for x in tviti:
        beseda=se_zacne_z(x,"@")
        for x in beseda:
            seznam.append(x)
    seznam=unikati(seznam)
    return seznam


def vsi_hashtagi(tviti):
    seznam = []
    for x in tviti:
        beseda=se_zacne_z(x,"#")
        for x in beseda:
            seznam.append(x)
    seznam=unikati(seznam)
    return seznam


def vse_osebe(tviti):
    seznam=[]
    for tvit in tviti:
        ime=avtor(tvit)
        if ime:
            seznam.append(ime)
    afne=vse_afne(tviti)
    for ime in afne:
        seznam.append(ime)
    seznam=unikati(seznam)
    seznam.sort()
    return seznam


def custva(tviti, hashtagi):
    seznam=[]
    for x in tviti:
        for y in hashtagi:
            hashi=se_zacne_z(x,"#")
            for z in hashi:
                if z==y:
                    ime=avtor(x)
                    if ime!=[]:
                        seznam.append(ime)
    seznam=unikati(seznam)
    seznam.sort()
    return seznam


def se_poznata1(tviti, oseba1, oseba2):
    for tvit in tviti:
        ime=avtor(tvit)
        afna=se_zacne_z(tvit,"@")
        for x in afna:
            if ime == oseba1 and x == oseba2 or ime == oseba2 and x == oseba1:
                return True
    return False



import collections


def besedilo(tvit):
    x=tvit.find(":")
    nov_tvit=tvit[x+2:]
    return nov_tvit


def zadnji_tvit(tviti):
    seznam_tvitov={}
    for tvit in tviti:
        ime=avtor(tvit)
        sporocilo=besedilo(tvit)
        seznam_tvitov[ime]=sporocilo
    return seznam_tvitov


def prvi_tvit(tviti):
    seznam_tvitov={}
    for tvit in tviti:
        ime = avtor(tvit)
        sporocilo = besedilo(tvit)
        if ime not in seznam_tvitov:
            seznam_tvitov[ime] = sporocilo
    return seznam_tvitov


def prestej_tvite(tviti):
    seznam_tvitov={}
    for tvit in tviti:
        ime = avtor(tvit)
        if ime not in seznam_tvitov:
            seznam_tvitov[ime]=1
        else:
            seznam_tvitov[ime] += 1
    return seznam_tvitov


def omembe(tviti):
    seznam_tvitov=collections.defaultdict(list)
    for tvit in tviti:
        ime = avtor(tvit)
        afna = se_zacne_z(tvit,"@")
        for i in afna:
            seznam_tvitov[ime].append(i)
        if afna == []:
            seznam_tvitov[ime] = []
    return seznam_tvitov


def neomembe(ime, omembe):
    seznam=[]
    print (ime)
    s=set(omembe[ime])
    print(s)
    if "sandra" not in s:
        if "sandra" != ime:
            seznam.append("sandra")
    if "ana" not in s:
        if "ana" != ime:
            seznam.append("ana")
    if "cilka" not in s:
        if "cilka" != ime:
            seznam.append("cilka")
    if "berta" not in s:
        if "berta" != ime:
            seznam.append("berta")
    if "benjamin" not in s:
        if "benjamin" != ime:
            seznam.append("benjamin")
    print(seznam)
    return seznam



def se_poznata(ime1, ime2, omembe):
    for x in omembe:
        if ime1==x or ime2==x:
            s=set(omembe[x])
            if ime1 in s or ime2 in s:
                return True
    return False


def hashtagi(tviti):
    seznam=collections.defaultdict(list)
    for tvit in tviti:
        tag=se_zacne_z(tvit,"#")
        ime=avtor(tvit)
        for i in tag:
            seznam[i].append(ime)
    for i in seznam:
        seznam[i]=sorted(seznam[i])
    return seznam











