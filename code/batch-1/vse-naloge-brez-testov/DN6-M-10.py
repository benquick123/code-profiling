#prejsna domaca naloga:
import collections

def unikati(s):
    novis=[]
    for st in s:
        if st not in novis:
            novis.append(st)
    return novis

def avtor(tvit):
    a=[]
    for i in tvit.split(":"):
        a.append(i)
    return a[0]

def vsi_avtorji(tviti):
    s=[]
    for tvit in tviti:
        ime=avtor(tvit)
        if ime not in s:
            s.append(ime)
    return s

def izloci_besedo(beseda):
    a = ""
    for i in beseda:
        if (i.isalnum() or i=='-'):
            a += i
    return(a)

def se_zacne_z(tvit, c):
    s = []
    for i in tvit.split():
        if (i[0] == c):
            s.append(izloci_besedo(i))
    return(s)

def zberi_se_zacne_z(tviti, c):
    a = []
    for i in tviti:
        for j in i.split():
            if (j[0] == c):
                beseda=izloci_besedo(j)
                if beseda not in a:
                 a.append(beseda)
    return(a)

def vse_afne(tviti):
    seznam=[]
    for i in tviti:
        for j in i.split():
            if (j[0]=='@'):
                beseda=izloci_besedo(j)
                if beseda not in seznam:
                    seznam.append(beseda)
    return seznam

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')


def vse_osebe(tviti):
    os=unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    return sorted(os)

#nova domaca naloga:

def besedilo(tvit):
    a=tvit.split(':')[1:]
    return ':'.join(a).strip()

def zadnji_tvit(tviti):
    s=collections.defaultdict()
    for tvit in tviti:
        s[avtor(tvit)]=besedilo(tvit)
    return s

def prvi_tvit(tviti):
    s=collections.defaultdict()
    oseba=[]
    for tvit in tviti:
        if avtor(tvit) not in oseba:
            s[avtor(tvit)] = besedilo(tvit)
            oseba.append(avtor(tvit))
    return s

def prestej_tvite(tviti):
    s=collections.defaultdict(int)
    for tvit in tviti:
        s[avtor(tvit)]+=1
    return s

def omembe(tviti):
    s = collections.defaultdict(list)
    for tvit in tviti:
        a = tvit.split()
        os = avtor(tvit)
        if os not in s:
            s[os] = []
        for b in a:
            if b[0] == '@':
                i = izloci_besedo(b)
                s[os].append(i)

    return s

def neomembe(ime, omembe):
    neom = []
    o = []
    for name in omembe:
        o.append(name)
    for oseba in o:
        if oseba not in omembe[ime] and oseba != ime:
            neom.append(oseba)
    return neom




