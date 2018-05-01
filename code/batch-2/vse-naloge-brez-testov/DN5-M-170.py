def unikati(s):
    seznam_unikatov = list()
    for element in s:
        if element not in seznam_unikatov:
            seznam_unikatov.append(element)
    return seznam_unikatov


def avtor(tvit):
    ime = ""
    for znak in tvit:
        if znak == ':':
            break
        ime += znak
    return ime

def vsi_avtorji(tviti):
    seznam_avtorjev = list()
    for en_tvit in tviti:
        seznam_avtorjev.append(avtor(en_tvit))
    return unikati(seznam_avtorjev)

def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
        if len(beseda) == 0:
            return ''
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
        if len(beseda) == 0:
            return ''
    return beseda

def se_zacne_z(tvit, c):
    seznam_besed = list()
    besede_v_tvitu = str.split(tvit)
    for beseda in besede_v_tvitu:
        if(beseda[0] == c):
            seznam_besed.append(izloci_besedo(beseda))
    return seznam_besed

def zberi_se_zacne_z(tviti, c):
    seznam_unikatnih_besed = list()
    for tvit in tviti:
        seznam_unikatnih_besed += se_zacne_z(tvit, c)
    return unikati(seznam_unikatnih_besed)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))

def custva(tviti, hashtagi):
    seznam_avtorjev = list()
    for tvit in tviti:
        for hashtag in se_zacne_z(tvit, '#'):
            if hashtag in hashtagi:
                seznam_avtorjev.append(avtor(tvit))
    return sorted(unikati(seznam_avtorjev))

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1 and oseba2 in se_zacne_z(tvit, '@'):
            return True
        if avtor(tvit) == oseba2 and oseba1 in se_zacne_z(tvit, '@'):
            return True
    return False


