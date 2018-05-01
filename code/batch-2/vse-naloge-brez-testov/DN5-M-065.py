tviti = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]

def unikati(s):
    kuku = []
    for element in s:
        if element not in kuku:
            kuku.append(element)
    return kuku

def avtor(tvit):
    fuku = tvit.split(":")
    return fuku [0]


def vsi_avtorji(tviti):    
    tutu = []
    for element in tviti:
        dudu = element.split(":")
        lulu = dudu [0]
        if lulu not in tutu:
            tutu.append(lulu)
    return tutu

def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
 
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
 
    return beseda


def se_zacne_z(tvit, c):
    return unikati([izloci_besedo(beseda) for beseda in tvit.split(" ") if beseda.startswith(c)])

def zberi_se_zacne_z(tviti, c):
    sumlivc2 = []
    for besedinja in tviti:
        for drekojed in besedinja.split():    
            if c in drekojed[0]:
                sumlivc2.append(izloci_besedo(drekojed))
    return unikati(sumlivc2)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    zdruzen_seznam = vse_afne(tviti) + vsi_avtorji(tviti)
    zdruzen_seznam.sort()    
    return unikati(zdruzen_seznam)

def custva(tviti, hashtagi):
    najjaci_seznam = []
    
    for tvit in tviti:
        for hashtag in hashtagi:
            if hashtag in tvit:
                najjaci_seznam.append((avtor(tvit)))
    najjaci_seznam.sort()
    return unikati(najjaci_seznam)

def custva(tviti, hashtagi):
    avtorji = []

    for tvit in tviti:
        for hashtag in hashtagi:
            if hashtag in tvit:
                avtorji.append(avtor(tvit))
                continue

    avtorji.sort()

    return unikati(avtorji)


oseba1 = "ema"
oseba2 = "berta"


def se_poznata(tviti, oseba1, oseba2):
    oseba1_omenjene_osebe = []
    oseba2_omenjene_osebe = []
 
    for tvit in tviti:
        tvit_avtor = avtor(tvit)
 
        if tvit_avtor == oseba1:
            oseba1_omenjene_osebe.extend(se_zacne_z(tvit, "@"))
        elif tvit_avtor == oseba2:
            oseba2_omenjene_osebe.extend(se_zacne_z(tvit, "@"))
 
    return oseba1 in oseba2_omenjene_osebe or oseba2 in oseba1_omenjene_osebe

