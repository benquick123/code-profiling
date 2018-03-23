from collections import Counter

def besedilo(tvit):
    b = tvit.split(': ', 1)[1]
    return b

def zadnji_tvit(tviti):
    ztweet = {}
    for tvit in tviti:
        ztweet[avtor(tvit)]= besedilo(tvit)
    return ztweet

def prvi_tvit(tviti):
    ptweet = {}
    for tvit in tviti:
        if avtor(tvit)not in ptweet:
            ptweet[avtor(tvit)] = besedilo(tvit)
    return ptweet

def prestej_tvite(tviti):
    sestweet = {}
    for tvit in tviti:
        if avtor(tvit)not in sestweet:
            sestweet[avtor(tvit)] = 1
        else:
            sestweet[avtor(tvit)] += 1
    return sestweet


def omembe(tviti):
    omtweet = {}
    for tvit in tviti:
        if avtor(tvit) not in omtweet:
            omtweet[avtor(tvit)] = []
        omtweet[avtor(tvit)] += alfaosebe(tvit)
    return omtweet

def neomembe(ime, omembe):
    netweet = []
    for avtorcek, ljudeki in omembe.items():
        if ime == avtorcek:
            for avtor2 in omembe.keys():
                if avtor2 not in ljudeki and avtor2 != ime and avtor2 not in netweet:
                    netweet.append(avtor2)
    return netweet

def se_poznata(ime1, ime2, omembe):
    for avtorcek, ljudeki in omembe.items():
        if avtorcek == ime1 and ime2 in ljudeki:
            return True
        elif avtorcek == ime2 and ime1 in ljudeki:
            return True
    return False

def hashtagi(tviti):
    hashtaggi = {}
    for tvit in tviti:
        for hash in tagg(tvit):
            if hash not in hashtaggi:
                hashtaggi[hash] = []
            hashtaggi[hash].append(avtor(tvit))
    for taggs in hashtaggi.values():
        taggs.sort()
    return hashtaggi

#######PREJŠNI TEDEN FUNKCIJE #######################
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
            if e not in zbrani:  ###kle bi lah sam dal Unikati
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

def alfaosebe(tvit):
    return se_zacne_z(tvit, '@')

def tagg(tvit):
    return se_zacne_z(tvit, '#')




#################################################################################
