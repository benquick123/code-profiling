#mi functions
def ime(tvit):
    return tvit[:tvit.index(':'):]

def izloci_besedo(beseda):
    nekaj = ""
    for a in beseda:
        if a.isalnum():
            nekaj += a
        if a == "-":
            nekaj += a
    return nekaj

def mentions(besedilo):

    return list


def besedilo(tvit):
    return tvit[tvit.index(':') + 2::]

def zadnji_tvit(tviti):
    slovar = {}
    for a in tviti:
        slovar[ime(a)] = besedilo(a)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for a in tviti:
        if ime(a) not in slovar:
            slovar[ime(a)] = besedilo(a)
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    for a in tviti:
        if ime(a) not in slovar:
            slovar[ime(a)] = 1
        else:
            slovar[ime(a)] += 1
    return slovar

#TO DELA

def omembe(tviti):
    slovar = {}
    for a in tviti:
        if ime(a) not in slovar:
            slovar[ime(a)] = []
        for n in a.split():
            if "@" in n:
                slovar[ime(a)].append(izloci_besedo(n))
    return slovar

def neomembe(ime, omembe):
    list = []
    for a in omembe:
        list.append(a)
    a = omembe[ime]
    ret = []
    a.append(ime)
    for n in list:
        if n not in a:
            ret.append(n)
    return ret

