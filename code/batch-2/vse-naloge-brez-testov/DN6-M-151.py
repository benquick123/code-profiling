def unikati(s):
    new = []
    for a in s:
        if a not in new:
            new.append(a)
    return new

def avtor(tvit):
    if isinstance(tvit, str):
        for avt in tvit.split():
            if ":" in avt and "@" not in avt:
               return avt.strip(":")
    else:
        lis = ', '
        sus = []
        new = lis.join(map(str, tvit))
        for avt in new.split():
            if ":" in avt and "@" not in avt:
                sus.append(avt)
        return [i.split(':', 1)[0] for i in sus]



def vsi_avtorji(tviti):
    imena = []
    for tvit in tviti:
        imena.append(avtor(tvit))
    return unikati(imena)



def izloci_besedo(beseda):
    for beginning, a in enumerate(beseda):
        if a.isalnum():
            break
    for end, a in enumerate(beseda[::-1]):
        if a.isalnum():
            break
    return beseda[beginning:len(beseda) - end]


def se_zacne_z(tvit, c):
    new = []
    for a in tvit.split():
        if c in a:
            cra = izloci_besedo(a)
            new.append(cra)
    return new


def zberi_se_zacne_z(tviti, c):
    vsi_avtorji(se_zacne_z(tviti, c))

def zberi_se_zacne_z(tviti, c):
    lis = []
    for a in tviti:
        cra = (se_zacne_z(a, c))
        lis += cra
    return unikati(lis)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    return unikati(sorted(vse_afne(tviti) + avtor(tviti)))

def custva(tviti, hashtagi):
    new = []
    for a in tviti:
        for b in a.split():
            for c in hashtagi:
                if c in b:
                    lok = avtor(a)
                    new.append(lok)
    return unikati(sorted(new))


def se_poznata(tviti, oseba1, oseba2):
    for a in tviti:
        if oseba2 in vsi_avtorji(tviti):
            if oseba1 in a and oseba2 in a:
                return True
    return False


def ves_tvit(diktionary):
    new = {}
    for a in diktionary:
        key = a.split(' ', 1)[0].strip(":")
        value = a.split(' ', 1)[1]
        if key in new:
            new[key].append(value)
        else:
            new[key] = [value]
    return new



def besedilo(tvit):

    if isinstance(tvit, str):
        bes = tvit.split(" ")
        del bes[0]

        lis = ' '
        new = lis.join(map(str, bes))

        return new

    else:
        mom = []
        for a in tvit:
            shaco = a.split(' ', 1)[1]
            mom.append(shaco)
        return mom

import collections

def avtor_tvitov(tv):
    mom = []
    for a in tv:
        shaco = a.split(' ', 1)[0]
        mom.append(shaco)
    key = [i.split(':', 1)[0] for i in mom]
    return key

def zadnji_tvit(tviti):
    value = besedilo(tviti)
    key = avtor_tvitov(tviti)
    di = dict(zip(key, value))
    return di

def prvi_tvit(tviti):
    val = besedilo(tviti)
    key = avtor_tvitov(tviti)
    di = dict(zip(reversed(key), reversed(val)))

    return di

def prestej_tvite(tviti):
    pos = collections.defaultdict(int)

    for key in avtor_tvitov(tviti):
        pos[key] += 1
    return pos

from collections import defaultdict

def omembe(tviti):
    a = vsi_avtorji(tviti)
    don = dict.fromkeys(a, None)
    for ol in tviti:
        at = ol.split(":")[0]
        if don[at] == None:
            don[at] = se_zacne_z(ol, "@")
        else:
            don[at] = don[at]+se_zacne_z(ol, "@")
    return don


def neomembe(ime, omembe):
    avtors = list(omembe.keys())
    kok = [item for item in avtors if item not in ime]
    for i in omembe[ime]:
        if i in kok:
            kok.remove(i)
    return kok



