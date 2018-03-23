def unikati(s):
    f = []
    for i in range(0, len(s)):
        if f.count(s[i]) == 0:
            f.append(s[i])
    return f

def avtor(tvit):
    s = tvit.split(':')
    return s[0]

def vsi_avtorji(tvits):
    f = []
    for s in tvits:
        if f.count(avtor(s)) == 0:
            f.append(avtor(s))
    return f

def izloci_besedo(beseda):
    while beseda[0].isalnum() == False:
        beseda = beseda[1:]
    while beseda[-1].isalnum() == False:
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    f = []
    tvit = tvit.split()
    for s in tvit:
        if s[0] == c:
            f.append(izloci_besedo(s))
    return f

def zberi_se_zacne_z(tvits, c):
    f = []
    for i in tvits:
        d = se_zacne_z(i, c)
        for z in d:
            if (z in f) == False:
                f.append(z)
    return f

def vse_afne(tvits):
    return zberi_se_zacne_z(tvits, '@')

def vsi_hashtagi(tvits):
    return zberi_se_zacne_z(tvits, '#')

def vse_osebe(tvits):
    d = vse_afne(tvits)
    f = vsi_avtorji(tvits)
    for i in f:
        if (i in d) == False:
            d.append(i)
    d.sort()
    return d

def custva(tvits, hashtagi):
    f = []
    for i in tvits:
        for h in hashtagi:
            if (h in i) == True:
                if (avtor(i) in j) == False:
                    f.append(avtor(i))
                    break
    f.sort()
    return f

def besedilo(tvit):
    i = 0
    while True:
        if tvit[i] == ":":
            break
        i += 1
    return tvit[i + 2:]

def zadnji_tvit(tviti):
    a = vsi_avtorji(tviti)
    d = dict.fromkeys(a)
    for i in tviti:
        s = i.split(':')
        d[s[0]] = besedilo(i)
    return d

def prvi_tvit(tviti):
    a = vsi_avtorji(tviti)
    d = dict.fromkeys(a, None)
    for i in tviti:
        s = i.split(':')
        if d[s[0]] == None:
            d[s[0]] = besedilo(i)
    return d

def prestej_tvite(tviti):
    a = vsi_avtorji(tviti)
    d = dict.fromkeys(a, 0)
    for i in tviti:
        s = i.split(':')
        d[s[0]] += 1
    return d


def omembe(tviti):
    a = vsi_avtorji(tviti)
    d = dict.fromkeys(a, None)
    for i in tviti:
        s = i.split(':')
        if d[s[0]] == None:
            d[s[0]] = se_zacne_z(i, '@')
        else:
            d[s[0]] += se_zacne_z(i, '@')
    return d

def neomembe(ime, omembe):
    avtors = list(omembe.keys())
    avtors.remove(ime)
    for i in omembe[ime]:
        if i in avtors:
            avtors.remove(i)
    return avtors

