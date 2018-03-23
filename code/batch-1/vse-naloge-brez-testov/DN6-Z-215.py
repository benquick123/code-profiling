def besedilo(tvit):
    besedilo = tvit.split(":", 1)[1]
    besedilo2 = besedilo.lstrip()
    return besedilo2

def zadnji_tvit(tviti):
    t = {}
    for tvit in tviti:
        avtor = tvit.split(":", 1)[0]
        besedilot = besedilo(tvit)
        t[avtor] = besedilot
    return t

def prvi_tvit(tviti):
    t = {}
    for tvit in tviti:
        avtor = tvit.split(":", 1)[0]
        besedilot = besedilo(tvit)
        if avtor not in t:
            t[avtor] = besedilot
    return t

def prestej_tvite(tviti):
    t = {}
    for tvit in tviti:
        avtor = tvit.split(":", 1)[0]
        if avtor not in t:
            t[avtor] = 0
        t[avtor] += 1
    return t






def unikati(s):  #1,3
    u = []
    for e in s:
        if e not in u:
            u.append(e)
    return u

def izloci_besedo(beseda): #1,1
    for znak in beseda:
        if znak.isalnum():
            break
        else:
            beseda = beseda.lstrip(znak[0])
    for znak in beseda[::-1]:
        if znak.isalnum():
            break
        else:
            beseda = beseda.rstrip(znak[-1])
    return beseda


def zberi_se_zacne_z(tvit, c): #1,2
    a = []
    vrni = []
    besede = tvit.split()
    for beseda in besede:
        if beseda[0] == c:
            beseda = izloci_besedo(beseda)
            a.append(beseda)
            vrni = unikati(a)
    return vrni

def vse_afne(tviti):  #1,4
    c = "@"
    b = zberi_se_zacne_z(tviti, c)
    return b

def omembe(tviti): #1
    t = {}
    for tvit in tviti:
        avtor = tvit.split(":", 1)[0]
        besedilo = tvit.split(":", 1)[1]
        besedilot = vse_afne(besedilo)
        if avtor not in t:
            t[avtor] = []
        t[avtor] += besedilot
    return t

def neomembe(name, mention): #2
    s = []
    for avtor in mention:
        if name != avtor:
            if avtor not in mention[name]:
                s.append(avtor)
    return s

