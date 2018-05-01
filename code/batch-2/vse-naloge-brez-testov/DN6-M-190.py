
def unikati(s):
    t = []
    [t.append(i) for i in s if not t.count(i)]
    return t

def avtor(tvit):
    return tvit[:tvit.find(':')]

def vsi_avtorji(tviti):
    s = []
    for tvit in tviti:
        s.append(avtor(tvit))
    return s

def izloci_besedo(beseda):
    start = 0
    for crka in beseda:
        if crka.isalnum():
            break
        start += 1
    end = len(beseda)
    for crka in reversed(beseda):
        if crka.isalnum():
            break
        end -= 1
    return beseda[start:end]

def se_zacne_z(tvit, c):
    t = []
    s = tvit.split()
    for beseda in s:
        if beseda[0] == c:
            t.append(izloci_besedo(beseda))
    return t

def vsi_hashtagi(tviti):
    t = []
    for tvit in tviti:
        t += se_zacne_z(tvit, '#')
    return unikati(t)

#-------------------------------------------------------------------------------------------

import collections

def besedilo(tvit):
    return tvit[tvit.find(':') + 1:].lstrip()

def zadnji_tvit(tviti):
    s = collections.defaultdict(str)
    for tvit in tviti:
        s[avtor(tvit)] = besedilo(tvit)
    return s

def prvi_tvit(tviti):
    s = collections.defaultdict(str)
    for tvit in tviti:
        if avtor(tvit) not in s:
            s[avtor(tvit)] = besedilo(tvit)
    return s

def prestej_tvite(tviti):
    return collections.Counter(vsi_avtorji(tviti))

def omembe(tviti):
    s = collections.defaultdict(list)
    for tvit in tviti:
        s.setdefault(avtor(tvit),[])
        for e in se_zacne_z(tvit, '@'):
            s[avtor(tvit)].append(e)
    return s

def neomembe(ime, omembe):
    ime = ime.lower()
    t = set(omembe.keys()).difference(set(omembe.get(ime, '')))
    t = t - {ime}
    return list(t)

def se_poznata(ime1, ime2, omembe):
    if ime2 in omembe.get(ime1, ''):
        return True
    if ime1 in omembe.get(ime2, ''):
        return True
    return False

def hashtagi(tviti):
    s = collections.defaultdict(list)
    for tvit in tviti:
        for tag in se_zacne_z(tvit,'#'):
            s[tag].append(avtor(tvit))
    for e in s.values():
        e.sort()
    return s


#-------------------------------------------------------------------------------------------

