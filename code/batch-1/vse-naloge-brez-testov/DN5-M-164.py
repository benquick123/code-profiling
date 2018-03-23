def unikati(s):
    seznam = []
    for _ in s:
        if _ not in seznam:
            seznam.append(_)
    return seznam

def avtor(tvit):
    return tvit.split(':')[0]

def vsi_avtorji(tviti):
    return unikati(split[0] for split in (x.split(':') for x in tviti))

def izloci_besedo(beseda):
    '''
    for i, crka in enumerate(beseda):
        if crka.isalpha():
            index1 = i
            break
    for i, crka in enumerate(reversed(beseda)):
        if crka.isalpha():
            index2 = len(beseda) - i
            break
    return(beseda[int(index1):int(index2)])
    '''
    return ','.join(vrnjena for vrnjena in beseda if vrnjena.isalnum() != False or vrnjena == '-').replace(',', '')

def se_zacne_z(tvit, c):
    s = []
    seznam = list(word.strip(c) for word in tvit.split() if word.startswith(c))
    for _ in seznam:
        if _.isalnum() == False:
            s.append(izloci_besedo(_))
        else:
            s.append(_)
    return s  

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for beseda in tviti:
        temp = beseda.split()
        for _ in temp:
            if _.startswith(c):
                if _.isalnum() == False:
                    seznam.append(izloci_besedo(_))
                else:
                    seznam.append(_)
    return unikati(seznam)

def vse_afne(tviti):
    seznam = []
    for beseda in tviti:
        s = beseda.split()
        for _ in s:
            if _.startswith('@'):
                if _.isalnum() == False:
                    seznam.append(izloci_besedo(_))
                else:
                    seznam.append(_)
    return unikati(seznam)

def vsi_hashtagi(tviti):
    seznam = []
    for beseda in tviti:
        s = beseda.split()
        for _ in s:
            if _.startswith('#'):
                if _.isalnum() == False:
                    seznam.append(izloci_besedo(_))
                else:
                    seznam.append(_)
    return unikati(seznam)

def vse_osebe(tviti):
    seznam = vse_afne(tviti)
    s = vsi_avtorji(tviti)
    for ime in s:
        if ime not in seznam:
            seznam.append(ime)
    return sorted(seznam)    

def custva(tviti, hashtagi):
    s = []
    for hashtag in hashtagi:
        tempHashtag = hashtag
        for beseda in tviti:
            if tempHashtag in beseda:
                s.append(avtor(beseda))
    return unikati(sorted(s))

def se_poznata(tviti, oseba1, oseba2):
    s = vse_osebe(tviti)
    if oseba1 in s and oseba2 in s:
        for beseda in tviti:
            if oseba1 in beseda and oseba2 in beseda:
                return True
    else:
        return False

