def unikati(s):
    ss = []
    for a in s:
        if a not in ss:
            ss.append(a)

    return ss


def avtor(tvit):
    return tvit.split()[0][:-1]

def vsi_avtorji(tviti):
    avt=[]
    for stavki in tviti:
        avt.append(avtor(stavki))

    return unikati(avt)

def izloci_besedo(beseda):
    # preveri[ ali je prva ;rka ;rka ;e ni jo odstranis
    while not beseda[0].isalnum() :
        beseda = beseda[1:]
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    vrne =[]
    for beseda in tvit.split():
        if beseda[0] == c :
            vrne.append(izloci_besedo(beseda))
    return vrne
def zberi_se_zacne_z(tviti, c):
    vrne =[]
    for tvit in tviti:
        vrne += (se_zacne_z(tvit, c))
    return unikati(vrne)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):

    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti))) #uredi po vrstnem redu sorted

def custva(tviti, hashtagi):
    skano=[]
    for tvit in tviti:
        for has in se_zacne_z(tvit, "#"):

            if has in hashtagi:
                skano.append(avtor(tvit))
    return unikati(sorted(skano))

def unisorted(x):
    return unikati(sorted(x))

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1 and oseba2 in se_zacne_z(tvit, "@"):
            return True




