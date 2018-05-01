
def unikati(s):
    t = []
    [t.append(i) for i in s if not t.count(i)]
    return t

def avtor(tvit):
    return tvit[:tvit.find(':')]

def vsi_avtorji(tviti):
    s = []
    for tvit in tviti:
        s.append(avtor(tvit))
    return unikati(s)

def izloci_besedo(beseda):
    start = 0
    for crka in beseda:
        if crka.isalnum():
            break
        start += 1
    end = len(beseda)
    for crka in reversed(beseda):
        if crka.isalnum():
            break
        end -= 1
    return beseda[start:end]

def se_zacne_z(tvit, c):
    t = []
    s = tvit.split()
    for beseda in s:
        if beseda[0] == c:
            t.append(izloci_besedo(beseda))
    return t

def zberi_se_zacne_z(tviti, c):
    t = []
    for tvit in tviti:
        t += se_zacne_z(tvit,c)
    return unikati(t)

def vse_afne(tviti):
    t = []
    for tvit in tviti:
        t += se_zacne_z(tvit, '@')
    return unikati(t)

def vsi_hashtagi(tviti):
    t = []
    for tvit in tviti:
        t += se_zacne_z(tvit, '#')
    return unikati(t)

def vse_osebe(tviti):
    t = []
    t += vsi_avtorji(tviti)
    t += vse_afne(tviti)
    t = unikati(t)
    t.sort()
    return t

def custva(tviti, hashtagi):
    t = []
    for tvit in tviti:
        for hashtag in hashtagi:
            if hashtag in tvit:
                t.append(avtor(tvit))
    t = unikati(t)
    t.sort()
    return t

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if oseba1 == avtor(tvit):
            if oseba2 in se_zacne_z(tvit, '@'):
                return True
    return False



# -------------------------------------------------------------------------------------------------------------

