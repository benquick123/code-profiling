def unikati(s):
    c=[]
    for x in s:
        x=str(x)
        x=x.split()
        x=x[0]
        if len(x)<2:
            x = int(x)
        if x not in c:
            c.append(x)
    return c

def avtor(tvit):
    x = tvit.split()
    x = x[0]
    return x[:-1]

def vsi_avtorji(tviti):
    c = []
    for x in tviti:
        x = x.split()
        x = x[0]
        x = x[:-1]
        if x not in c:
            c.append(x)
    return c

def izloci_besedo(beseda):
    for x in beseda:
        if ord(x) >= 48 and ord(x) <= 57 or \
            ord(x) >= 65 and ord(x) <= 90 or \
            ord(x) >= 97 and ord(x) <= 122:
            break
        else:
            beseda = beseda[1:]

    for x in range(len(beseda)-1,0, -1):
        if ord(beseda[x]) >= 48 and ord(beseda[x]) <= 57 or \
                                ord(beseda[x]) >= 65 and ord(beseda[x]) <= 90 or \
                                ord(beseda[x]) >= 97 and ord(beseda[x]) <= 122:
            break
        else:
            beseda = beseda[:-1]

    return beseda

def se_zacne_z(tvit, c):
    t=[]
    tvit=tvit.split()
    for x in tvit:
        if x[0]==c:
            t+=(izloci_besedo(x),)
    return t

def zberi_se_zacne_z(tviti, c):
    t=[]
    for x in tviti:
        f=se_zacne_z(x,c)
        for s in f:
            if s not in t:
                t+=(s,)
    return t

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return (zberi_se_zacne_z(tviti, "#"))

def vse_osebe(tviti):
    o=[]
    for x in tviti:
        for y in range(0,len(x)):
            if x[y]==":":
                if x[:y] not in o:
                    o.append(x[:y])
    x=vse_afne(tviti)
    for z in x:
        if z not in o:
           o.append(z)

    o=sorted(o)
    return o

def custva(tviti, hashtagi):
    o=[]
    for x in tviti:
        for z in hashtagi:
            if "#"+z in x:
                for y in range(0, len(x)):
                    if x[y] == ":":
                        if x[:y] not in o:
                            o.append(x[:y])
    o = sorted(o)
    return o

def se_poznata(tviti, oseba1, oseba2):
    for x in tviti:
        if "#"+oseba1 not in x and "#"+oseba2 not in x:
            if oseba1 in x and oseba2 in x:
                return True
    else:
        return False

