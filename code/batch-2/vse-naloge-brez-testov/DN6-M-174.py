import collections
from collections import OrderedDict


def ime(os):
    i=""
    c=0
    for x in range(len(os)):
        c+=1
        if os[x]==":":
           break
    i=os[:c-1]
    return i

def besedilo(tvit):
    bes=()
    c=1
    for x in tvit.split():
       if c==1:
           if ":"in x:
               c=0
       else:
           bes+=(x,)

    return ' '.join(bes)

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

def zadnji_tvit(tviti):
    tv=collections.defaultdict(str)
    for x in tviti:
            tv[ime(x)]=besedilo(x)
    return tv

def prvi_tvit(tviti):
    tv = collections.defaultdict(str)
    for x in tviti:
        if ime(x) not in tv:
            tv[ime(x)] = besedilo(x)
    return tv

def prestej_tvite(tviti):
    tv=collections.defaultdict(int)
    for x in tviti:
        tv[ime(x)] +=1
    return tv

def omembe(tviti):
    tv = collections.defaultdict(list)
    for x in tviti:
        tv[ime(x)] +=se_zacne_z(x,"@")
    return tv

def neomembe(ime, omembe):
    n=[]
    om=(omembe[ime])
    for x in omembe:
        if x!=ime and x not in om:
            n+=(x,)
    return n

def se_poznata(ime1, ime2, omembe):
    if ime1 not in omembe or ime2 not in omembe:
        return False
    if ime2 in omembe[ime1] or ime1 in omembe[ime2]:
        return True
    else:
        return False

def hashtagi(tviti):
    avt=collections.defaultdict(list)
    for x in tviti:
        for y in x.split():
            if y[0]=="#":
                avt[izloci_besedo(y)]+=(ime(x),)
    avt= OrderedDict(sorted(avt.items(), key=lambda t: t[0]))
    for x in avt:
        avt[x].sort()
    return avt

