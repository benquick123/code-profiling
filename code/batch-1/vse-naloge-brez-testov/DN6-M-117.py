def unikati(s):
    seznam = []
    for el in s:
        if el not in seznam:
            seznam.append(el)
    return seznam

def avtor(tvit):
    ime = tvit.split(':')[0]
    return ime

def vsi_avtorji(tviti):
    s = []
    for el in tviti:
        if avtor(el) not in s:
            s.append(avtor(el))
    return s


def izloci_besedo(beseda):
    str1 = beseda
    while not str1[0].isalnum():
        str1 = str1[1:]
    str2 = str1[::-1]
    while not str2[0].isalnum():
        str2 = str2[1:]
    return str2[::-1]


def izloci_prvo_besedo(beseda):
    str1 = beseda
    while not str1[0].isalnum():
        str1 = str1[1:]
    i = 0
    while i < len(str1):
        if str1[i].isalnum():
            i = i + 1
        else:
            break
    return str1[:i]


def se_zacne_z(tvit, c):
    s = []
    for i in range(0, len(tvit)):
        if tvit[i] == c:
            s.append(izloci_prvo_besedo(tvit[i:]))
    return s


def zberi_se_zacne_z(tviti, c):
    s = []
    for el in tviti:
        for i in range(0, len(se_zacne_z(el, c))):
            if se_zacne_z(el, c)[i] not in s:
                s.append(se_zacne_z(el, c)[i])
    return s


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')


def vse_osebe(tviti):
    s = []
    for el in vsi_avtorji(tviti):
        if el not in s:
            s.append(el)
    for el in tviti:
        for i in range(0, len(se_zacne_z(el, '@'))):
            if se_zacne_z(el, '@')[i] not in s:
                s.append(se_zacne_z(el, '@')[i])
    return sorted(s)




def besedilo(tvit):
    return ' '.join(tvit.split()[1:])


def zadnji_tvit(tviti):
    d = {}
    for tvit in tviti:
        d.update({avtor(tvit):besedilo(tvit)})
    return d


def prvi_tvit(tviti):
    d = {}
    for tvit in tviti:
        if avtor(tvit) not in d:
            d.update({avtor(tvit): besedilo(tvit)})
    return d


def prestej_tvite(tviti):
    d = {}
    for tvit in tviti:
        if avtor(tvit) not in d:
            d.update({avtor(tvit): 0})
    for tvit in tviti:
        d[avtor(tvit)] = d[avtor(tvit)]+1
    return d


def omembe(tviti):
    d = {}
    for tvit in tviti:
        if avtor(tvit) not in d:
            d.update({avtor(tvit): []})
    for tvit in tviti:
        for el in se_zacne_z(tvit, '@'):
            d[avtor(tvit)].append(el)
    return d


def neomembe(ime, omembe):
    pomozni_s = []
    s = []
    for el in omembe:
        pomozni_s.append(el)
    for el in pomozni_s:
        if el not in omembe[ime] and el != ime:
            s.append(el)
    return s


def se_poznata(ime1, ime2, omembe):
    try:
        if ime2 in omembe[ime1] or ime1 in omembe[ime2]:
            return True
        else:
            return False
    except:
        return False


def hashtagi(tviti):
    s = vsi_hashtagi(tviti)
    d = {}
    for el in s:
        d.update({el: []})
    for el in s:
        for tvit in tviti:
            if el in se_zacne_z(tvit, '#'):
                d[el].append(avtor(tvit))
                d[el].sort()
    return d




