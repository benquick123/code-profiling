def unikati(s):
    nov_seznam=[]
    for x in s:
        if x not in nov_seznam:
            nov_seznam.append(x)
    return nov_seznam

def avtor(tvit):
    return tvit[0:tvit.find(":")]

def vsi_avtorji(tviti):
    seznam = []
    for tvit in tviti:
        seznam.append(avtor(tvit))
    return unikati(seznam)

def izloci_besedo(beseda):
    while beseda[0].isalnum() == False:
        beseda = beseda.strip(beseda[0])
    while beseda[-1].isalnum() == False:
        beseda = beseda.rstrip(beseda[-1])
    return beseda

def se_zacne_z(tvit, c):
    nov_seznam = []
    seznam = tvit.split()
    for x in seznam:
        if x[0] == c:
            nov_seznam.append(izloci_besedo(x))
    return nov_seznam

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        seznam += se_zacne_z(tvit, c)
    return unikati(seznam)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) +
                  vse_afne(tviti)),
                  key=str.lower)




def besedilo(tvit):
    return tvit[tvit.find(":")+2 : len(tvit)]

def zadnji_tvit(tviti):
    s = {}
    for tvit in tviti:
        s[avtor(tvit)] = besedilo(tvit)
    return s

def prvi_tvit(tviti):
    s = {}
    for tvit in tviti:
        if avtor(tvit) not in s:
            s[avtor(tvit)] = besedilo(tvit)
    return s


def prestej_tvite(tviti):
    s = {}
    for tvit in tviti:
        if avtor(tvit) not in s:
            s[avtor(tvit)] = 0

        s[avtor(tvit)] += 1
    return s

def omembe(tviti):
    s = {}
    for tvit in tviti:
        if avtor(tvit) not in s:
            s[avtor(tvit)] = []
        s[avtor(tvit)].extend(se_zacne_z(tvit, "@"))
    return s

def neomembe(ime, omembe):
    s = {}
    list_kljucev = []
    seznam_neomenjenih = []
    for x in omembe:
        list_kljucev.append(x)
    for y in list_kljucev:
        if y not in omembe[ime] and y != ime:
            seznam_neomenjenih.append(y)
    return seznam_neomenjenih

def se_poznata(ime1, ime2, omembe):
    vsa_imena = []
    for x in omembe:
        vsa_imena.append(x)
    if ime1 and ime2 in vsa_imena:
        if ime1 in omembe[ime2] or \
            ime2 in omembe[ime1]:
            return True
    return False

def hashtagi(tviti):
    s = dict.fromkeys(vsi_hashtagi(tviti))
    for x in s:
        s[x]=[]
        for tvit in tviti:
            if x in tvit:
                s[x].append(avtor(tvit))
                s[x].sort()
    return s
