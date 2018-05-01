tviti = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]

# OBVEZNI DEL:

def unikati(s):
    k = []
    for x in s:
        if x not in k:
            k.append(x)
    return k

unikati([1, 3, 2, 1, 1, 3, 2])


def avtor(tvit):
    return tvit.split(':')[0]
    # return tvit[:tvit.index(":")]


avtor("ana: kdo so te @berta, @cilka, @dani? #krneki")


def vsi_avtorji(tviti):
    i = []
    for x in tviti:
        a = avtor(x)
        i.append(a)
    return unikati(i)

vsi_avtorji(tviti)


def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

izloci_besedo("@janez-novak!!!")


def se_zacne_z(tvit, c):
    k = []
    i = tvit.split(" ")
    for a in i:
        if a[0] == c:
            k.append(izloci_besedo(a))
    return k

se_zacne_z("sandra: @berta Ne maram #programiranje1 #krneki", "#")

def zberi_se_zacne_z(tviti, c):
    k = []
    for a in tviti:
        k.extend(se_zacne_z(a,c))
    return unikati(k)

zberi_se_zacne_z(tviti, "@")


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

vse_afne(tviti)

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

vsi_hashtagi(tviti)

def vse_osebe(tviti):
    i = vsi_avtorji(tviti)
    k = vse_afne(tviti)
    i.extend(k)
    i.sort()
    return unikati(i)

vse_osebe(tviti)



# DODATNA NALOGA:

def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        for hash in hashtagi:
            if tvit.__contains__(hash):
                avtorji.append(avtor(tvit))
    return sorted(unikati(avtorji))

custva(tviti, ["dougcajt", "krneki"])


def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if se_zacne_z(tvit, "@").__contains__(oseba2):
            if oseba1 == avtor(tvit):
                return True
            False

print(se_poznata(tviti, "ana", "berta"))


#_______________________________________________________ TESTI _______________________________________________________

