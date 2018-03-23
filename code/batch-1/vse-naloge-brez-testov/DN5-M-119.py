#Sergei Burykin

tviti = ["sandra: Spet ta dež. #dougcajt",
         "berta: @sandra Delaj domačo za #programiranje1",
         "sandra: @berta Ne maram #programiranje1 #krneki",
         "ana: kdo so te @berta, @cilka, @dani? #krneki",
         "cilka: jst sm pa #luft",
         "benjamin: pogrešam ano #zalosten",
         "ema: @benjamin @ana #split? po dvopičju, za začetek?"]

def unikati(s):
    d = []
    for i in range(0, len(s)):
        if d.count(s[i]) == 0:
            d.append(s[i])
    return d

def avtor(tvit):
    s = tvit.split(':')
    return s[0]

def vsi_avtorji(tviti):
    d = []
    for i in tviti:
        if d.count(avtor(i)) == 0:
            d.append(avtor(i))
    return d

def izloci_besedo(beseda):
    while beseda[0].isalnum() == False:
        beseda = beseda[1:]
    while beseda[-1].isalnum() == False:
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    tvit = tvit.split()
    d = []
    for i in tvit:
        if i[0] == c:
            d.append(izloci_besedo(i))
    return d

def zberi_se_zacne_z(tviti, c):
    d = []
    for i in tviti:
        s = se_zacne_z(i, c)
        for j in s:
            if (j in d) == False:
                d.append(j)
    return d

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    d = vse_afne(tviti)
    s = vsi_avtorji(tviti)
    for i in s:
        if (i in d) == False:
            d.append(i)
    d.sort()
    return d

def custva(tviti, hashtagi):
    d = []
    for i in tviti:
        for j in hashtagi:
            if (j in i) == True:
                if (avtor(i) in d) == False:
                    d.append(avtor(i))
                    break
    d.sort()
    return d

def se_poznata(tvits, oseba1, oseba2):
    for i in tvits:
        if avtor(i) == oseba1:
            d = vse_afne(i.split())
            if (oseba2 in d) == True:
                return True
    return False



