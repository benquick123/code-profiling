tviti = {"berta": "@sandra Delaj domačo za #programiranje1",
 "sandra": "@berta Ne maram #programiranje1 #krneki",
 "ana": "kdo so te: @berta, @cilka, @dani? #krneki"}

from collections import Counter
def unikati(s):
    str = []
    for i in s:
        if i not in str:
            str.append(i)
    return str


def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)


def izloci_besedo(beseda):

    zac = ""
    n = 0
    while n < len(beseda) - 1:
        if beseda[n].isalnum() == False:
            zac = zac + beseda[n]
        else:
            break
        n += 1

    m = len(beseda) - 1
    kon = ""
    while m > 0:
        if beseda[m].isalnum() == False:
            kon = kon + beseda[m]
        else:
            break
        m -= 1

    return beseda.replace(zac, "").replace(kon, "")


def se_zacne_z(tvit, c):
    besede = tvit.split()
    pravebesede = []

    for beseda in besede:
        if(beseda[0] == c):
            pravebesede.append(izloci_besedo(beseda))

    return pravebesede


def besedilo(tvit):
    return  tvit.split(": ", 1)[1]


def zadnji_tvit(tviti):
    zadnji_tviti = {}
    for tvit in tviti:
        avtor = tvit.split(": ")[0]
        besedilo_tvita = besedilo(tvit)
        zadnji_tviti[avtor] = besedilo_tvita
    return zadnji_tviti

def prvi_tvit(tviti):
    prvi_tviti = {}
    for tvit in tviti:
        avtor = tvit.split(": ")[0]
        besedilo_tvita = besedilo(tvit)
        if avtor not in prvi_tviti:
            prvi_tviti[avtor] = besedilo_tvita
    return prvi_tviti

def prestej_tvite(tviti):
    presteti_tviti = {}
    for tvit in tviti:
        avtor = tvit.split(": ")[0]
        presteti_tviti[avtor] = presteti_tviti.get(avtor, 0)+1

    return presteti_tviti

def omembe(tviti):
    omembe = {}
    for tvit in tviti:
        avtor = tvit.split(": ")[0]
        omemba = se_zacne_z(tvit, "@")
        if(omemba != []):
            if(avtor not in omembe):
                omembe[avtor] = omemba
            else:
                for tvit in omemba:
                    omembe[avtor].append(tvit)
        else:
            omembe[avtor] = []

    return omembe


def neomembe(ime, omembe):
    neomembe = omembe
    omenjene_osebe = []
    neomenjene_osebe = []

    for oseba in neomembe[ime]:
        omenjene_osebe.append(oseba)

    for oseba in omembe.keys():
        if(oseba == ime):
            continue
        if(oseba not in omenjene_osebe):
            neomenjene_osebe.append(oseba)

    return neomenjene_osebe

def se_poznata(ime1, ime2, omembe):
    omenjene_osebe = omembe

    if(ime1 in omenjene_osebe):
        for oseba in omenjene_osebe[ime1]:
            if(oseba == ime2):
                return True
        else:
            if(ime2 in omenjene_osebe):
                for oseba_2 in omenjene_osebe[ime2]:
                    if oseba_2 == ime1:
                        return True
    else:
        if(ime2 in omenjene_osebe):
            for oseba_2 in omenjene_osebe[ime2]:
                if(oseba_2 == ime1):
                    return True
    return False

def hashtagi(tviti):
    hashtagi = {}
    for tvit in tviti:
        avtor = avtor(tvit)
        hashtag_collection = se_zacne_z(tvit, "#")


        for single_hashtag in hashtag_collection:
            if (single_hashtag not in hashtagi):
                hashtagi[single_hashtag] = avtor.split()
            else:
                hashtagi[single_hashtag].append(avtor)
        for hash in hashtagi:
            x = hashtagi[hash]
            x = sorted(x)
            hashtagi[hash] = x
    return hashtagi






