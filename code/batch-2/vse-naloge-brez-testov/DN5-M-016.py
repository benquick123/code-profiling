
tviti = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]



def unikati(s):
    str = []
    for i in s:
        if i not in str:
            str.append(i)
    return str


print(unikati([1, 3, 2, 1, 1, 3, 2]))

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

print(izloci_besedo("@breda"))


def se_zacne_z(tvit, c):
    besede = tvit.split()
    pravebesede = []

    for beseda in besede:
        if(beseda[0] == c):
            pravebesede.append(izloci_besedo(beseda))

    return pravebesede


print(se_zacne_z("maram #programiranje1 #krneki", "#"))


def zberi_se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        #TU NI APPENDA!!!
        besede = besede + se_zacne_z(tvit, c)
    return unikati(besede)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    osebe = vsi_avtorji(tviti) + vse_afne(tviti)
    return sorted(unikati(osebe))


def custva(tviti, hashtagi):
    osebe = []

    vsihashi = []
    for tvit in tviti:
        if bool(set(se_zacne_z(tvit, "#")) & set(hashtagi)) == True:
            osebe.append(avtor(tvit))
    return sorted(unikati(osebe))

print(custva(tviti, ["dougcajt", "krneki", "zalosten"]))


def se_poznata(tviti, oseba1, oseba2):

    avtortvita = ""
    for tvit in tviti:
        avtortvita = avtor(tvit)

        omenjena_oseba = se_zacne_z(tvit, "@")

        if omenjena_oseba != []:

            osebe = []
            osebe = osebe + omenjena_oseba
            osebe.append(avtortvita)
            unikatioseb = unikati(osebe)

            if (oseba1 in unikatioseb):
                if (oseba2 in unikatioseb):
                    return True
    else:
        return False


