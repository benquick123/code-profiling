import collections

def se_zacne_z(tvit, c):
    tvit = tvit.split()
    re = []
    for i in tvit:
        if i[0] == c:
            re.append(izloci_besedo(i))
    return re

def unikati(s):
    r = []
    for i in s:
        if i not in r:
            r.append(i)
    return r

def izloci_besedo(bes):
    f = True
    while f:
        if (not bes[0].isalnum()):
            bes = bes[1:]
        else:
            f = False
    b = True
    while b:
        if (not bes[-1].isalnum()):
            bes = bes[:-1]
        else:
            b = False
    return bes

def besedilo(tvit):
    return tvit.split(" ", 1)[1]

def ime(i):
    return i.split(":")[0]

def zadnji_tvit(tviti):
    s = {}
    for i in tviti:
        s[ime(i)] = besedilo(i)
    return s

def prvi_tvit(tviti):
    s = {}
    for i in reversed(tviti):
        s[ime(i)] = besedilo(i)
    return s

def prestej_tvite(tviti):
    s = {}
    l = []
    for i in tviti:
        l.append(ime(i))
    s= collections.Counter(l)
    return s

def omembe(tviti):
    s = {}
    for i in tviti:
        for j in i.split(" "):
            if(j[0] == "@"):
                s.setdefault(ime(i), []).append(izloci_besedo(j))
            else:
                s.setdefault(ime(i), [])
    return s

def neomembe(ime, omemb):
    l = list(omemb.keys())
    s = []
    for i in l:
        if i not in omemb[ime] and i != ime:
            s.append(i)
    return s

def se_poznata(ime1, ime2, ome):
    if ime2 in ome.get(ime1, []) or ime1 in ome.get(ime2, []):
        return True
    return False

def hashtagi(tviti):
    s = {}
    for i in tviti:
        for j in se_zacne_z(i,"#"):
            s.setdefault(j, []).append(ime(i))
    for i in s.keys():
        s[i].sort()
    return s

