tviti = ["sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te: @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]

def unikati(s):
    k = []
    for x in s:
        if x not in k:
            k.append(x)
    return k

def avtor(tvit):
    return tvit.split(':')[0]
    # return tvit[:tvit.index(":")]

def vsi_avtorji(tviti):
    i = []
    for x in tviti:
        a = avtor(x)
        i.append(a)
    return unikati(i)

def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    k = []
    i = tvit.split(" ")
    for a in i:
        if a[0] == c:
            k.append(izloci_besedo(a))
    return k

def zberi_se_zacne_z(tviti, c):
    k = []
    for a in tviti:
        k.extend(se_zacne_z(a, c))
    return unikati(k)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    i = vsi_avtorji(tviti)
    k = vse_afne(tviti)
    i.extend(k)
    i.sort()
    return unikati(i)

# ______________________________________________________ NALOGA 6 _____________________________________________________


def besedilo(tvit):
    i =tvit.index(":")
    return tvit[i+2:]


def zadnji_tvit(tviti):
    s = {}
    for tvit in tviti:
        s[avtor(tvit)] = besedilo(tvit)
    return s

def prvi_tvit(tviti):
    glej = []
    s = {}
    for tvit in tviti:
        if not glej.__contains__(avtor(tvit)):
            s[avtor(tvit)] = besedilo(tvit)
            glej.append(avtor(tvit))
    return s

from collections import Counter

def prestej_tvite(tviti):
    i = []
    for x in tviti:
        i.append(avtor(x))
    s = {}
    c = Counter(i)
    for tvit in tviti:
        s[avtor(tvit)] = c[avtor(tvit)]
    return s

prestej_tvite(tviti)


def omembe(tviti):
    a = []
    s = {}
    for tvit in tviti:
        avt = avtor(tvit)
        omenjeni = se_zacne_z(tvit, "@")
        if avtor(tvit) in a:
            s[avt].extend(omenjeni)
        else:
            a.append(avt)
            s[avt] = omenjeni
    return s


def neomembe(ime, omembe):
    vsi = list(omembe.keys())
    vsi.remove(ime)
    for s in omembe[ime]:
        if s in vsi:
            vsi.remove(s)
    return vsi


def se_poznata(ime1, ime2, omembe):
    if ime1 and ime2 in list(omembe.keys()):
        if ime1 in omembe[ime2] or ime2 in omembe[ime1]:
            return True
        else:
            False

def hashtagi(tviti):
    hashi = vsi_hashtagi(tviti)
    s = {}
    for hash in hashi:
        b = []
        for tvit in tviti:
            avt = avtor(tvit)
            if besedilo(tvit).__contains__(hash):
                b.append(avt)
        s[hash] = sorted(b)
    return s

# _______________________________________________________ TESTI _______________________________________________________

