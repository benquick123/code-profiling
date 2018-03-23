import collections
def unikati(s):
    l = []
    for a in s:
        if not l.__contains__(a):
            l.append(a)
    return l

def avtor(tvit):
    return tvit.split()[0][:-1]

def vsi_avtorji(tviti):
    l = []
    for t in tviti:
        l.append(avtor(t))
    return unikati(l)

def izloci_besedo(beseda):
    a = 0
    b = len(beseda) - 1
    while not beseda[a].isalnum():
            a += 1
    while not beseda[b].isalnum():
            b -= 1
    return beseda[a:b + 1]

def se_zacne_z(tvit, c):
    l = []
    for t in tvit.split():
        if t[0] == c:
            l.append(izloci_besedo(t))
    return l

def zberi_se_zacne_z(tviti, c):
    w = []
    for tvit in tviti:
        for t in se_zacne_z(tvit, c):
            w.append(izloci_besedo(t))
    return unikati(w)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))

def custva(tviti, hashtagi):
    l = []
    for tvit in tviti:
        q = tvit.split()
        for h in hashtagi:
            if q.__contains__("#" + h):
                l.append(avtor(tvit))
    return sorted(unikati(l))

def se_poznata(tviti, oseba1, oseba2):
    l = []
    for tvit in tviti:
        l.append(avtor(tvit))
        l += se_zacne_z(tvit, "@")
        if l.__contains__(oseba1) and l.__contains__(oseba2):
            return True
        else:
            l.clear()
    return Fals



def besedilo(tvit):
    for i in range(len(tvit)):
        if tvit[i] == ':':
            return tvit[i+2:]

def zadnji_tvit(tviti):
    s = {}
    for tvit in tviti:
        s[avtor(tvit)] = besedilo(tvit)
    return s

def prvi_tvit(tviti):
    s = {}
    for tvit in tviti:
        if s.__contains__(avtor(tvit)):
            continue
        s[avtor(tvit)] = besedilo(tvit)
    return s

def prestej_tvite(tviti):
    s = collections.defaultdict(int)
    for tvit in tviti:
        s[avtor(tvit)] += 1
    return s

def omembe(tviti):
    s = collections.defaultdict(list)
    for tvit in tviti:
        s[avtor(tvit)] += se_zacne_z(tvit, "@")
    return s
tviti = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]
o = omembe(tviti)

def neomembe(ime, o):
    l = []
    omeneni = o[ime]
    for v in list(o.keys()):
        if not omeneni.__contains__(v) and v != ime:
            l.append(v)
    return l

def se_poznata(ime1, ime2, o):
    for k, v in o.items():
        if k == ime1 and v.__contains__(ime2) or k == ime2 and v.__contains__(ime1):
            return True
    return False

def hashtagi(tviti):
    s = collections.defaultdict(list)
    for h in vsi_hashtagi(tviti):
        s[h] += sorted([avtor(tvit) for tvit in tviti if h in [izloci_besedo(bes) for bes in tvit.split()]])
    return s



print(hashtagi(tviti))



