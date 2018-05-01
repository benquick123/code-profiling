tviti = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]


def unikati(s):
    novi = []
    for a in s:
        if a not in novi:
            novi.append(a)
    return novi


def avtor(tvit):
    return tvit[:tvit.find(":")]


def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)


def izloci_besedo(beseda):
    beseda_nova = beseda 
    
    for znak in beseda:
        if not znak.isalnum():
            beseda_nova = beseda_nova[1 : ]
        elif znak.isalnum():
            break
        
    beseda = beseda_nova
    for znak in beseda[::-1]:
        if not znak.isalnum():
            beseda_nova = beseda_nova[: -1]
        elif znak.isalnum():
            break

    return beseda_nova


def se_zacne_z(tvit, c):
    tabelca = tvit.split(" ")
    hashtagi = []

    for beseda in tabelca:
        if beseda[0] == c:
            hashtagi.append(izloci_besedo(beseda))
    return hashtagi

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        seznam += se_zacne_z(tvit, c)
    return unikati(seznam)

def vse_afne(tviti):
    seznam = zberi_se_zacne_z(tviti, "@")
    return unikati(seznam)

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")
    
def vse_osebe(tviti):
    osebe = vsi_avtorji(tviti)
    osebe += vse_afne(tviti)
    osebe = unikati(osebe)
    osebe.sort()
    return osebe



#dodatni del

def custva(tviti, hashtagi):
    seznam = []
    for tvit in tviti:
        for hash in hashtagi:
            if hash in tvit:
                seznam.append(avtor(tvit))
    seznam = unikati(seznam)
    seznam.sort()
    return seznam

def se_poznata(tviti, oseba1, oseba2):
    if pozna(tviti, oseba1, oseba2) or pozna(tviti, oseba2, oseba1):
        return True
    return False
    
    
def pozna(tviti, oseba1, oseba2):
    le_avtorjevi = []
    for tvit in tviti:
        if oseba1 == avtor(tvit):
            le_avtorjevi.append(tvit)
    if oseba2 in vse_afne(le_avtorjevi):
        return True
    return False


