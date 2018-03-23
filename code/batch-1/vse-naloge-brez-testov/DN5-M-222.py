
#1
def unikati(s):
    nov_seznam = []
    for x in s:
        if x not in nov_seznam:
            nov_seznam.append(x)
    return nov_seznam



#2
def avtor(tviti):
    tviti = tviti.split(' ')
    return tviti[0][:-1]



#3
def vsi_avtorji(tviti):
    imena = []
    for x in tviti:
        if (avtor(x) not in imena):
            imena.append(avtor(x))
    return imena


#4
def izloci_besedo(beseda):
    x = 0
    y = 0
    while (x == 0) & (y == 0):
        leng = len(beseda)
        if(beseda[0].isalnum() == False):
            beseda = beseda.strip(beseda[0])
            leng = len(beseda)
        else:
            x = 1
        if (beseda[leng-1].isalnum() == False):
            beseda = beseda.strip(beseda[leng-1])
            leng = len(beseda)
        else:
            y = 1
    return beseda


#5
def se_zacne_z(tvit, c):
    i = 0
    s = []
    tvit = tvit.split(' ')
    for x in tvit:
        bes = x
        if bes[0] == c:
            s.append(izloci_besedo(bes))
    return s


#6
def zberi_se_zacne_z(tviti, c):
    s = []
    for x in tviti:
        for y in se_zacne_z(x, c):
            if y not in s:
                s.append(y)
    return s


#7
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


#8
def vsi_hashtagi(tviti):
    return  zberi_se_zacne_z(tviti, "#")


#9
def vse_osebe(tviti):
    a = []
    for x in tviti:
        if avtor(x) not in a:
            a.append(avtor(x))
    for afne in vse_afne(tviti):
        if afne not in a:
            a.append(afne)
    return sorted(a)

print(vse_osebe(["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]))

