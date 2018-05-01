def unikati(s):
    u = []
    for e in s:
        if e not in u:
            u.append(e)
    return u

def avtor(tvit):
    a = tvit.split(':')
    return a[0]

def vsi_avtorji(tviti):
    a = []
    for tvit in tviti:
        a.append(avtor(tvit))
    va = unikati(a)
    return va

def izloci_besedo(beseda):
    b = beseda
    while b[0].isalnum() == False:
        b =  b[1:]
    while b[len(b)- 1].isalnum() == False:
        b = b[:len(b) - 1]
    return b

def se_zacne_z(tvit, c):
    zacnez = []
    for e in tvit.split():
        if e[0] == c:
            i = izloci_besedo(e)
            zacnez.append(i)
    return zacnez


def zberi_se_zacne_z(tviti, c):
    zbrani = []
    for tvit in tviti:
        for e in se_zacne_z(tvit, c):
            if e not in zbrani:
                zbrani.append(e)
    return zbrani

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    people = vsi_avtorji(tviti) + unikati(vse_afne(tviti))
    people.sort()
    return unikati(people)

#######DODATNE NALOGE#########

def custva(tviti, hashtagi):
    taggi = []
    for tvit in tviti:
        for tag in hashtagi:
            if '#' + tag in tvit:
                taggi.append(avtor(tvit))
    taggi.sort()
    return unikati(taggi)

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        t = [avtor(tvit)] + alfaosebe(tvit)
        if oseba1 in t and oseba2 in t:
            return True
    return False

def alfaosebe(tvit):
    return se_zacne_z(tvit, '@')


















########################TESTI########################################################
