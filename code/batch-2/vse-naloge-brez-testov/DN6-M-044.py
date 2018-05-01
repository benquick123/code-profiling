def besedilo(tvit):
    return tvit.split(': ', 1)[1]

def zadnji_tvit(tviti):
    s = {}
    for e in tviti:
        a = e.split (': ', 1)
        if a[0] not in s:
            s[a[0]] = a[1]
        else:
            del s[a[0]]
            s[a[0]] = a[1]
    return s

def prvi_tvit(tviti):
    s = {}
    for e in tviti:
        a = e.split (': ', 1)
        if a[0] not in s:
            s[a[0]] = a[1]
    return s

def prestej_tvite(tviti):
    s = {}
    for e in tviti:
        a = e.split (': ', 1)
        if a[0] not in s:
            s[a[0]] = 1
        else:
            s[a[0]] += 1
    return s

def omembe(tviti):
    s = {}
    for e in tviti:
        avtor_tvit = e.split (': ', 1)
        besede = avtor_tvit[1].split (" ")
        if avtor_tvit[0] not in s:
            s[avtor_tvit[0]] = []
            for beseda in besede:
                if beseda[0] == "@":
                    beseda = beseda[1:]
                    if beseda[-1].isalnum () == False:
                        beseda = beseda[:-1]
                        s[avtor_tvit[0]].append (beseda)
                    else:
                        s[avtor_tvit[0]].append (beseda)
        else:
            for beseda in besede:
                if beseda[0] == "@":
                    beseda = beseda[1:]
                    if beseda[-1].isalnum () == False:
                        beseda = beseda[:-1]
                        s[avtor_tvit[0]].append (beseda)
                    else:
                        s[avtor_tvit[0]].append (beseda)
    return s

def neomembe(ime, omembe):
    omenjeni = []
    avtorji = []
    neomenjeni = []
    for e in omembe.items ():
        avtor, oznaceni = e
        if avtor == ime:
            for oznacen in oznaceni:
                omenjeni.append (oznacen)
        else:
            avtorji.append (avtor)
    for osebe in avtorji:
        if osebe not in omenjeni:
            neomenjeni.append (osebe)
    return neomenjeni







