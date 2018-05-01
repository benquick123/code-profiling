import re
from collections import Counter, OrderedDict, defaultdict
import operator

def besedilo(tvit):
    return tvit.split(": ", 1)[1]

def zadnji_tvit(tviti):
    a = {}
    for tvit in tviti:
        b = tvit.split(": ", 1)[0]
        c = tvit.split(": ", 1)[1]
        a.update({b : c})
    return a

def prvi_tvit(tviti):
    return zadnji_tvit(list(reversed(tviti)))


def prestej_tvite(tviti):
    a = [i.split()[0] for i in tviti]
    c = ([s.replace(':', '') for s in a])
    b = Counter()
    for word in c:
        b[word] += 1
    return dict(sorted(b.items(), key=operator.itemgetter(0)))

def omembe(tviti):
    a = defaultdict(list)
    for tvit in tviti:
        b = tvit.split(":")[0]
        for j in tvit.split():
            if "@" in j:
                j = ''.join(e for e in j if e.isalnum())
                a.setdefault(b, []).append(j)
            elif b not in a:
                a.update({b : []})
    return(a)

def neomembe(ime, omembe):
    a = []
    b = omembe.get(ime)
    for c in omembe.keys():
        if c == ime:
            continue
        if c not in b:
            a.append(c)
    return(a)

def se_poznata(ime1, ime2, omembe):
    if ime2 not in omembe.keys() or ime1 not in omembe.keys():
        return False
    else:
        a = omembe.get(ime1)
        b = omembe.get(ime2)
        if ime2 in a or ime1 in b:
            return True
        else:
            return False

def hashtagi(tviti):
    a = defaultdict(list)
    for tvit in tviti:
        b = tvit.split(":")[0]
        for j in tvit.split():
            if "#" in j:
                j = ''.join(e for e in j if e.isalnum())
                a.setdefault(j, []).append(b)
                for x in a:
                    a[x].sort()
    return (a)

