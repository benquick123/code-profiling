import collections
import re
"""
def prvi_tvit(tviti):
    a = []
    konec = {}
    for i, tvit in enumerate(tviti):
        a.append(avtor(tvit))
        print(i,tvit)
        print(a)
        print(a.index(avtor(tvit)))
        if i == a.index(avtor(tvit)):
            konec[avtor(tvit)] = besedilo(tvit)
    return konec

def se_poznata(ime1, ime2, omembe):
    omenjeni = set(omembe.get(ime1,[]) + omembe.get(ime2,[]))
    return True if ime1 in omenjeni or ime2 in omenjeni else False
"""

def unikati(s):
    return [x for i , x in enumerate(s) if i == s.index(x)]
def avtor(tvit):
    return tvit.split()[0][:-1]
def vsi_avtorji(tviti): #se ponavljajo
    return [avtor(i) for i in tviti]
def besedilo(tvit):
    return " ".join(tvit.split()[1:])
def zadnji_tvit(tviti):
    return {avtor(tvit): besedilo(tvit) for tvit in tviti}
def prvi_tvit(tviti):
    return {avtor(tvit): besedilo(tvit) for i, tvit in enumerate(tviti) if i == vsi_avtorji(tviti).index(avtor(tvit))}
def prestej_tvite(tviti):
    return collections.Counter(vsi_avtorji(tviti))
def izloci_besedo(beseda):
    return re.search(r"([a-zA-Z\d]+.*[a-zA-Z\d])|([a-zA-Z\d])", beseda)[0]    
def se_zacne_z(tvit, c):
    return [izloci_besedo(x) for x in tvit.split() if x[0]==c]
def omembe(tviti):
    omembe = {}
    for tvit in tviti:
        if avtor(tvit) not in omembe:
            omembe[avtor(tvit)] = []
        omembe[avtor(tvit)] += se_zacne_z(tvit, "@")
    return omembe
def neomembe(ime, omembe):
    vsi = [i for i in omembe]
    vsi.remove(ime)
    for j in omembe[ime]:
        if j in vsi:
            vsi.remove(j)
    return vsi
def se_poznata(ime1, ime2, omembe):
    return True if ime1 in set(omembe.get(ime1,[]) + omembe.get(ime2,[])) or ime2 in set(omembe.get(ime1,[]) + omembe.get(ime2,[])) else False
def zberi_se_zacne_z(tviti, c):
    return unikati([elementi for lista in (se_zacne_z(x, c) for x in tviti) for elementi in lista])
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")
def hashtagi(tviti):
    neki = {}
    for hashtag in vsi_hashtagi(tviti):
        for tvit in tviti:
            if hashtag not in neki:
                neki[hashtag] = []
            if hashtag in tvit:
                neki[hashtag] += [avtor(tvit)]
    for key in neki:
        neki[key] = sorted(neki[key])
    return neki

