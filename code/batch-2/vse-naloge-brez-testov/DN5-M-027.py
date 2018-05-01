def unikati(s):
    t=[]
    for a in s:
        if a not in t:
            t.append(a)
    #print(t)
    return t

def avtor(tvit):
    a = tvit.split(":")
    b = a[0]
    return b

def vsi_avtorji(tviti):
    a=[]
    for n in tviti:
        a.append(avtor(n))
    a = unikati(a)
    return(a)

def izloci_besedo(beseda):
    t = beseda
    t = klic(t)
    t = t[::-1]
    t = klic(t)
    t = t[::-1]
    return t

def klic(t):
    for a in t:
        if a.isalnum() == False:
            t = t.replace(a, "")
        else:
            break
    return t

def se_zacne_z(tvit, c):
    k = tvit.split(" ")
    b=[]
    for a in k:
        #print(a)
        if c in a:
            b.append(izloci_besedo(a))
           # print(b)
    return b

def zberi_se_zacne_z(tviti, c):
    b = []
    for a in tviti:
        #print(a)
        if c in a:
            #print(a)
            b.extend(se_zacne_z(a, c))
           # print(b)
    b = unikati(b)
    #print(b)
    return b

def vse_afne(tviti):
    b = []
    for a in tviti:
        b.extend(se_zacne_z(a, "@"))
    b = unikati(b)
    return b

def vsi_hashtagi(tviti):
    b = []
    for a in tviti:
        b.extend(se_zacne_z(a, "#"))
    b = unikati(b)
    #print(b)
    return b

def vse_osebe(tviti):
     a = vsi_avtorji(tviti)
     a.extend(vse_afne(tviti))
     a = unikati(a)
     a.sort()
     return a

def custva(tviti, hashtagi):
    k  =[]
    for a in hashtagi:
        for b in tviti:
            if a in b:
                k.append(avtor(b))
    k = unikati(k)
    k.sort()
    return k

def se_poznata(tviti, oseba1, oseba2):
    for a in tviti:
        if avtor(a) == oseba1:
            if oseba2 in a and oseba2 in vse_osebe(tviti):
                k = avtor(a)
                print(oseba2, oseba1)
                return True
            else:
                return False











