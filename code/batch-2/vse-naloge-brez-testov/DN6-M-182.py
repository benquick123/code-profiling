def unikati(s):
    u = []
    for i in s:
        if i not in u:
            u.append(i)
    return u


def avtor(tvit):
    t = tvit.split(":")
    for i in t:
        return i


def vsi_avtorji(tviti):
    avtorji = []
    t = ":".join(tviti)
    u = t.split(":")
    i = u[0]
    for i in u[::2]:
        if i not in avtorji:
            avtorji.append(i)
    return avtorji

def izloci_besedo(beseda):
    b = beseda
    while b:
        if b[0].isalnum():
            break
        b = b[1:]
    while True:
            if not b[-1].isalnum():
                b = b[:-1]
            else:
                break
    return b

def se_zacne_z(tvit, c):
    l = []
    tvit_c = tvit.split()
    for i in tvit_c:
        if c == i[0]:
            niz = izloci_besedo(i)
            l.append(niz)
    return l

def zberi_se_zacne_z(tviti, c):
    l = []
    tvit_1 = " ".join(tviti)
    tvit_c = tvit_1.split()
    for i in tvit_c:
        if c in i[0]:
            niz = izloci_besedo(i)
            if niz not in l:
                l.append(niz)
    return l

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    c = "#"
    return zberi_se_zacne_z(tviti, c)

def vse_osebe(tviti):
    avtorji = vsi_avtorji(tviti)
    afna = vse_afne(tviti)
    seznam_nov = unikati(avtorji + afna)
    seznam_nov.sort()
    return seznam_nov


#########################################


def besedilo(tvit):
    b = tvit.find(':')
    return tvit[b+2:]

#kljuc = avtor, vrednost = tvit
def zadnji_tvit(tviti):
    s = {}
    for tvit in tviti:
        a = avtor(tvit)
        s[a] = besedilo(tvit)
    return s

#Obdrži prvi tvit osebe
def prvi_tvit(tviti):
    s = {}
    for tvit in tviti:
        a = avtor(tvit)
        if a not in s:
            s[a] = besedilo(tvit)
    return s

#Prešteje število tvitov
import collections

def prestej_tvite(tviti):
    s = collections.defaultdict(int)
    for tvit in tviti:
        a = avtor(tvit)
        s[a] += 1
    return s

def omembe(tviti):
    s = collections.defaultdict(list)
    for tvit in tviti:
        a = avtor(tvit)
        c = vse_afne([tvit])
        s[a] += c
    return s

def neomembe(ime, omembe):
     a = []
     for clovek in omembe:
         if clovek not in omembe[ime] and clovek != ime:
             a.append(clovek)
     return a

