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



