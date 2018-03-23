def unikati(s):

    a = []
    for i in s:
        if i in a:
            pass
        else:
            a.append (i)
    return a

def avtor(tvit):

    b = tvit.split()
    for i in b:
        if i.find(":") > 0:
            i = i.replace(":","")
            return i

def vsi_avtorji(tviti):
    a = []
    for i in tviti:
        b = avtor(i)
        a.append(b)
    c = unikati(a)
    return c

def izloci_besedo(beseda):
    #beseda = "!#$%\"=%/%()/Ben-jamin'"
    b = 0
    while beseda[b].isalnum() == False:
        a = beseda.replace(beseda[b],"")
        beseda = a

    besedilo = beseda[::-1]
    while besedilo[b].isalnum() == False:
        besedilo = besedilo.replace(besedilo[b],"")

    c = besedilo[::-1]
    return c

def se_zacne_z(tvit, c):
    a = []
    tvit = tvit.split()
    for i in tvit:
        for x in i:
            if x == c:
                i = i.replace(c, "")
                i = izloci_besedo(i)
                a.append(i)
    return a

def zberi_se_zacne_z(tviti, c):
    a = []

    for i in tviti:
        i = i.split()
        for x in i:
            if c in x:
                d = x.replace(c, "")
                d = izloci_besedo(d)
                if d in a:
                    pass
                else:
                    a.append(d)
    return a

def vse_afne(tviti):
    b = zberi_se_zacne_z(tviti,"@")
    return b

def vsi_hashtagi(tviti):
     a = zberi_se_zacne_z(tviti,"@" and "#")
     return a

def vse_osebe(tviti):
    a = []

    b = vsi_avtorji(tviti)
    if b not in a:
        a.extend(b)

    c = vse_afne(tviti)
    for i in c:
        if i in a:
            pass
        else:
            a.append(i)

    a.sort()
    print(a)
    return a

def custva(tviti, hashtagi):
    a = []
    for i in tviti:
        for e in hashtagi:
            if e in i:
                if i.find(e) > 0:
                    h = i.replace(":", "")
                    c = h.split()
                    if c[0] not in a:
                        a.append(c[0])
    a.sort()
    return a

def se_poznata(tviti, oseba1, oseba2):
    b = []
    f = "@"
    for i in tviti:
        i  = i.split()
        for a in i:

            if a.find(":") > 0:
                a = a.replace(":", "")
                b.append(a)

            if "@" in a:
                a = a.replace(f, "")
                b.append(a)
            if "," in a:
                a = a.replace(",", "")
                b.append(a)
            if oseba1 in b:
                print(b, "true")
                if oseba2 in b:
                    print (b, "lul")
                    return True

        del b[:]
    return False


#-------------------------------------------------------------

