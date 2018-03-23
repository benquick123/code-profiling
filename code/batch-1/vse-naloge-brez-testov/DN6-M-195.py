def izloci_besedo(s):
    return s.strip("".join( [i for i in s if not i.isalnum()] ))


def besedilo(tvit):
    return tvit.partition(":")[2].lstrip()

def zadnji_tvit(tviti):
    return {t.split(sep=":")[0]: besedilo(t) for t in tviti}

def prvi_tvit(tviti):
    tviti2 = {}
    for t in tviti:
        avtor = t.split(sep = ":")[0]
        if avtor not in tviti2:
            tviti2[avtor] = besedilo(t)
    return tviti2

def prestej_tvite(tviti):
    a = {}
    for t in tviti:
        avtor = t.split(sep = ":")[0]
        if avtor in a:
            a[avtor] += 1
        else:
            a[avtor] = 1
    return a

def omembe(tviti):
    a = {}
    for t in tviti:
        avtor = t.split(sep = ":")[0]
        if avtor not in a:
            a[avtor] = []
        a[avtor] += [izloci_besedo(o) for o in t.split()
                            if o[0] == "@" 
                            and izloci_besedo(o) not in a[avtor]]
    return a

def neomembe(ime, omembe):
    return [i for i in omembe if i not in omembe[ime]
                             and i != ime]

def se_poznata(ime1, ime2, omembe):
    return ime1 in omembe.get(ime2,[]) or ime2 in omembe.get(ime1,[])

def hashtagi(tviti):
    tviti.sort()
    tagi = {}
    for t in tviti:
        for i in t.split():
            if i[0] == "#":
                i = i.strip("".join([j for j in i if not j.isalnum()]))
                tag = tagi.setdefault(i, [])
                avtor = t.split(sep=":").pop(0)
                if avtor not in tag:
                    tag.append(avtor) 
    return tagi







