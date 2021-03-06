def unikati(s):
    s_unikati=[]
    for e in s:
        if e not in s_unikati:
            s_unikati.append(e)
    return s_unikati

def avtor(tvit):
    ime=tvit[0:tvit.find(":")]
    return ime

def vsi_avtorji(tviti):
    imena=[]
    for tvit in tviti:
        if avtor(tvit) not in imena:
            imena.append(avtor(tvit))
    return imena

def izloci_besedo(beseda):
    for e in beseda:
        if e.isalnum()==False:
            beseda=beseda.lstrip(e[0])
    for i in beseda[::-1]:
        if i.isalnum()==False:
            beseda = beseda.rstrip(i[-1])
    return beseda

def se_zacne_z(tvit, c):
    vsi=[]
    for beseda in tvit.split():
        for e in beseda:
            if e==c:
                najdena_beseda=izloci_besedo(beseda)
                vsi.append(najdena_beseda)
    return vsi

def zberi_se_zacne_z(tviti, c):
    ponovitve=[]
    for tvit in tviti:
        for beseda in tvit.split():
            for e in beseda:
                if e == c:
                    najdena_beseda = izloci_besedo(beseda)
                    if najdena_beseda not in ponovitve:
                        ponovitve.append(najdena_beseda)
    return ponovitve

def vse_afne(tviti):
    afne=zberi_se_zacne_z(tviti,"@")
    return afne

def vsi_hashtagi(tviti):
    hashtagi=zberi_se_zacne_z(tviti,"#")
    return hashtagi

def vse_osebe(tviti):
    osebe=[]
    for avtor in vsi_avtorji(tviti):
        osebe.append(avtor)
    for ime in vse_afne(tviti):
        if ime not in osebe:
            osebe.append(ime)
    osebe.sort()
    return osebe

################Dodatna naloga###############

def custva(tviti, hashtagi):
    avtorji=[]
    for hash in hashtagi:
        for tvit in tviti:
            for beseda in tvit.split():
                if hash==izloci_besedo(beseda):
                    ime=avtor(tvit)
                    if ime not in avtorji:
                        avtorji.append(ime)

    avtorji.sort()
    return avtorji


def se_poznata(tviti, oseba1, oseba2):
    s = []
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            for beseda in tvit.split():
                if izloci_besedo(beseda) == oseba2 and (izloci_besedo(beseda) in vse_afne(tviti)):
                    s.append(beseda)
        if avtor(tvit) == oseba2:
            for beseda in tvit.split():
                if izloci_besedo(beseda) == oseba1 and (izloci_besedo(beseda) in vse_afne(tviti)):
                    s.append(beseda)
    return bool(s)


###Obvezna#########
def besedilo(tvit):
    text=tvit[tvit.find(":"):]
    brez_dvopicja=text.lstrip(":")
    return brez_dvopicja.lstrip()

def zadnji_tvit(tviti):
    s={}
    for tvit in tviti:
        s[avtor(tvit)] = besedilo(tvit)
    return s

def prvi_tvit(tviti):
    s={}
    for tvit in tviti:
        if avtor(tvit) not in s:
            s[avtor(tvit)] = besedilo(tvit)
    return s


def avtorji(tviti):
    imena=[]
    for tvit in tviti:
        imena.append(avtor(tvit))
    return imena

def prestej_tvite(tviti):
    s={}
    c=0
    for ime in avtorji(tviti):
        if ime not in s:
            s[ime] = 1
        else:
            s[ime] +=1
    return s

def omembe(tviti):
    s={}
    for tvit in tviti:
        if avtor(tvit) not in s:
            s[avtor(tvit)] = se_zacne_z(tvit, "@")
        else:
            s[avtor(tvit)] += se_zacne_z(tvit, "@")
    return s


def neomembe(ime, omembe):
    neomenjeni = []
    omenjeni = []
    for par in omembe.items():
            if par[0] == ime:
                omenjeni=par[1]
                break
    for par in omembe.items():
            if (par[0] not in omenjeni) and (ime != par[0]):
                neomenjeni.append(par[0])
    return neomenjeni

######Dodatna#######
def se_poznata(ime1, ime2, omembe):
    for par in omembe.items():
        if ime1==par[0] and ime2 in par[1]\
                or ime2 == par[0] and ime1 in par[1]:
            return True
    return False

def hashtagi(tviti):
    s={}
    for hash in vsi_hashtagi(tviti):
        s[hash] = custva(tviti,[hash])
    return s

