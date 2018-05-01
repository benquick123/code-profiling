
import re
import collections


def avtor(tvit):
    return tvit[0:tvit.index(":")]

def izloci_besedo(beseda):
   a=re.sub('^[^\s\w]*|[^\s\w]*$','',beseda)
   return a


def unikati(s):
    a = []
    for x in s:
        if x not in a:
            a.append(x)
    return a

def vsi_avtorji(tviti):
    a = []
    for x in tviti:
        a.append(avtor(x))
    return a


def besedilo(tvit):
    return tvit[tvit.index(":")+2:]

def zadnji_tvit(tviti):
    slovar = {}
    for x in tviti:
        ime = avtor(x)
        slovar[ime] = besedilo(x)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for x in tviti:
            ime = avtor(x)
            if ime not in slovar:
                slovar[ime] = besedilo(x)
    return slovar

def prestej_tvite(tviti):
    seznam = unikati(vsi_avtorji(tviti))
    drugi_seznam = vsi_avtorji(tviti)
    slovar={}
    for x in seznam:
        slovar[x]=drugi_seznam.count(x)
    return slovar

def se_zacne_z(tvit):
    a=[]
    seznam = [t for t in tvit.split() if t.startswith("@")]
    for x in seznam:
        a.append(izloci_besedo(x))
    return a

def omembe(tviti):
    slovar = collections.defaultdict(list)
    for tvit in tviti:
        kdo = avtor(tvit)
        slovar[kdo].extend(se_zacne_z(tvit))
    return slovar

def neomembe(ime, omembe):
    slovar = []
    for kdo, kaj in omembe.items():
        if kdo not in omembe[ime] and kdo != ime:
            slovar.append(kdo)

    return slovar


