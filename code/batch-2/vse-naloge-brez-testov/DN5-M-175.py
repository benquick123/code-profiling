
def unikati(s):
    nov_seznam = []
    for element in s:
        if element not in nov_seznam:
            nov_seznam.append(element)
    return nov_seznam

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    seznam_avtorjev = []
    for tvit in tviti:
        seznam_avtorjev.append(tvit.split(":")[0])
    return unikati(seznam_avtorjev)

def izloci_besedo(beseda):
    print(beseda)
    for i in range(len(beseda)):
        if beseda[i].isalnum():
            beseda = beseda[i:]
            break
    for i in range(len(beseda)-1, 0, -1):
        if beseda[i].isalnum():
            beseda = beseda[:i+1]
            break
    return beseda

def se_zacne_z(tvit, c):
    seznam = []
    besede = tvit.split()
    for beseda in besede:
        if beseda.startswith(c):
            seznam.append(izloci_besedo(beseda))
    return seznam

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        besede = se_zacne_z(tvit, c)
        for beseda in besede:
            seznam.append(beseda)
    return unikati(seznam)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    osebe_omenjene_v_afnah = vse_afne(tviti)
    avtorji_tvitov = vsi_avtorji(tviti)
    seznam_oseb = osebe_omenjene_v_afnah + avtorji_tvitov
    return sorted(unikati(seznam_oseb))

def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        seznam_hashtagov = se_zacne_z(tvit, "#")
        for hashtag in seznam_hashtagov:
            if hashtag in hashtagi:
                avtorji.append(avtor(tvit))
    return sorted(unikati(avtorji))

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        avtor_ = avtor(tvit)
        omenjene_osebe = se_zacne_z(tvit, "@")
        if (avtor_ == oseba1 and oseba2 in omenjene_osebe) or (avtor_ == oseba2 and oseba1 in omenjene_osebe):
            return True
    return False




