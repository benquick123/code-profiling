import re
import itertools

def unikati(s):
    unikatno = []
    [unikatno.append(i) for i in s if not unikatno.count(i)]
    return unikatno

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    avtorji = []
    for i in range(len(tviti)):
        avtorji.append(avtor(tviti[i]))
    return unikati(avtorji)

def izloci_besedo(beseda):
    return re.sub('^[^a-zA-Z0-9]*|[^a-zA-Z0-9]*$','',beseda)

def se_zacne_z(tvit, c):
    besede = tvit.split(" ")
    izlocene_besede = []
    for ele in besede:
        if ele[0] == c:
            izlocene_besede.append(izloci_besedo(ele))
    return izlocene_besede

def zberi_se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        besede.append(se_zacne_z(tvit,c))
#        print(besede)
    return (unikati(list(itertools.chain.from_iterable(besede))))

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    osebe = vsi_avtorji(tviti) + vse_afne(tviti)
    return sorted(unikati(osebe))

def custva(tviti, hashtagi):
    posiljatelj = []
    for ele in tviti:
        avt = avtor(ele)
        tagi = se_zacne_z(ele, '#')
        if not set(tagi).isdisjoint(hashtagi):
            posiljatelj.append(avt)
    return sorted(unikati(posiljatelj))

def se_poznata(tviti, oseba1, oseba2):
    osebi = [oseba1, oseba2]
    for ele in tviti:
        avt = avtor(ele)
        poznanci = se_zacne_z(ele, '@')
        if (avt == oseba1 or avt == oseba2) and not set(poznanci).isdisjoint(osebi):
            return True
    return False

