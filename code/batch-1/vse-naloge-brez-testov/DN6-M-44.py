from collections import defaultdict


def besedilo(tvit):
    x = tvit.split(":")[0] + ": "
    return(tvit.replace(x, ""))


def zadnji_tvit(tviti):
    s = {}
    for e in tviti:
        x = e.split(":")[0]
        y = besedilo(e)
        s[x] = y

    return s


def prvi_tvit(tviti):
    s = {}
    for e in tviti:
        if e.split(":")[0] not in s:
            x = e.split(":")[0]
            y = besedilo(e)
            s[x] = y


    return s


def prestej_tvite(tviti):
    s = {}
    y = 1
    for e in tviti:
        if e.split(":")[0] in s:
            x = e.split(":")[0]
            s[x] += y
        else:
            x = e.split(":")[0]
            s[x] = y

    return s


def omembe(tviti):
    s = defaultdict(list)
    for e in tviti:
        x = e.split(":")[0]
        y = besedilo(e)
        for e1 in y.split(" "):
            if "@" in e1:
                e2 = e1.replace("@", "")
                if "?" in e2:
                    e2 = e2.replace("?", "")

                s[x].append(e2.replace(",", ""))
        if x not in s:
            s[x] = []

    return s


def neomembe(ime, omembe):
    s = []
#    for e in omembe:
#        x.append(e)
    x = omembe.keys()
    for e in omembe:
        if e == ime:
            for e1 in x:
                if e1 not in omembe[ime]:
                    s.append(e1)
    s.remove(ime)

    return s


def se_poznata(ime1, ime2, omembe):
    s = omembe.keys()
    x = neomembe(ime1, omembe)
    y = neomembe(ime2, omembe)
    if ime1 in y:
        return False
    elif ime2 in x:
        return False
    else:
        return True

def hashtagi(tviti):
    s = defaultdict(list)
    for e in tviti:
        for e1 in e.split(" "):
            if "#" in e1:
                e1 = e1.replace("#", "")
                s[e1].append(e.split(":")[0])



    return s






