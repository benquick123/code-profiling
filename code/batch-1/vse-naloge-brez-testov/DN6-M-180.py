
def unikati(s):
    nov_s = []
    for i in s:
        if i not in nov_s:
            nov_s.append(i)
    return nov_s

def avtor(tvit):
    return tvit.split(":")[0]


def vsi_avtorji(tviti):
    sez_avtorjev = []
    for s in tviti:
        if avtor(s) not in sez_avtorjev:
            sez_avtorjev.append(avtor(s))
    return sez_avtorjev


def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    c_zacne = []
    sz = tvit.split()
    for i in sz:
        if i[0] == c:
            c_zacne.append(izloci_besedo(i))
    return c_zacne


def zberi_se_zacne_z(tviti, c):
    se_zacne = []
    for i in tviti:
        se_zacne.extend(se_zacne_z(i, c))
        nov_s = unikati(se_zacne)
    return nov_s


def vse_afne(tviti):
    c = '@'
    return zberi_se_zacne_z(tviti, c)


def vsi_hashtagi(tviti):
    c = '#'
    return zberi_se_zacne_z(tviti, c)


def vse_osebe(tviti):
    abc = []
    abc.extend(vsi_avtorji(tviti))
    abc.extend(vse_afne(tviti))
    i = unikati(abc)
    i.sort()
    return i

#############





def besedilo(tvit):
    sp = tvit.split(': ', 1)
    value = sp[1]
    return value

def zadnji_tvit(tviti):
    tweets = {}
    for tvit in tviti:
        sp = tvit.split(': ', 1)
        key = sp[0]
        value = sp[1]
        tweets[key] = value
    return tweets

def prvi_tvit(tviti):
    tweets = {}
    for tvit in tviti:
        sp = tvit.split(': ', 1)
        key = sp[0]
        value = sp[1]
        if key not in tweets:
            tweets[key] = value
        else:
            None
    return tweets

def prestej_tvite(tviti):
    list_t = []
    for tvit in tviti:
        sp = tvit.split(':', 1)
        key = sp[0]
        list_t.append(key)
    return {x: list_t.count(x) for x in list_t}


def omembe(tviti):
    tweets = {}
    for tvit in tviti:
        key = avtor(tvit)
        value = se_zacne_z(tvit, '@')
        if key not in tweets:
            tweets[key] = value
        else:
            tweets[key].extend(value)
    return tweets

def neomembe(ime, omembe):
    neo = []
    for key in omembe:
        if key != ime:
            neo.append(key)
        ni_omenil = [x for x in neo if x not in omembe[ime]]
    return ni_omenil





