import collections
import re

def avtor(tvit):
    return tvit.split(":")[0]

def besedilo(tvit):
    return ' '.join(tvit.split()[1:])


def zadnji_tvit(tviti):
    avtorji = {}
    for tvit in tviti:
        if avtor(tvit) not in avtorji:
            avtorji[avtor(tvit)] = besedilo(tvit)
        else:
            del avtorji[avtor(tvit)]
            avtorji[avtor(tvit)] = besedilo(tvit)
    return avtorji

def prvi_tvit(tviti):
    avtorji = {}
    for tvit in tviti:
        if avtor(tvit) not in avtorji:
            avtorji[avtor(tvit)] = besedilo(tvit)
    return avtorji


def prestej_tvite(tviti):
    presteto = collections.defaultdict(int)
    for tvit in tviti:
        presteto[avtor(tvit)] += 1
    return presteto

def izloci_besedo(beseda):
    return re.search('^[^A-Za-z0-9]*(.*?)[^A-Za-z0-9]*$', beseda).group(1)

def se_zacne_z(tvit, c):
    return [izloci_besedo(beseda) for beseda in tvit.split() if beseda[0] == c]

def omembe(tviti):
    omenjeni = collections.defaultdict(list)
    for tvit in tviti:
        omenjeni[avtor(tvit)] += se_zacne_z(tvit, '@')
    return omenjeni

def neomembe(ime, omembe):
    return list(set(omembe) - set(omembe[ime]) - {ime})

def se_poznata(ime1, ime2, omembe):
    return ime1 in omembe.get(ime2, '') or ime2 in omembe.get(ime1, '')

def unikati(s):
    unikat = []
    for i in s:
        if i in unikat:
            continue
        else:
            unikat.append(i)
    return unikat

def zberi_se_zacne_z(tviti, c):
    afne = []
    for tvit in tviti:
        afne += se_zacne_z(tvit, c)
    return unikati(afne)

def vsi_hashtagi(tviti):
    return unikati(zberi_se_zacne_z(tviti, "#"))

def hashtagi(tviti):
    slovar = collections.defaultdict(list)
    for hashtag in vsi_hashtagi(tviti):
        for tvit in tviti:
            if hashtag in tvit:
                slovar[hashtag] += [avtor(tvit)]
        slovar[hashtag] = sorted(slovar[hashtag])
    return slovar



