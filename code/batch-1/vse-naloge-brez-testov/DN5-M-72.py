#FUNKCIJE

def unikati(s):
    nov_seznam = []
    for i in s:
        if i not in nov_seznam:
            nov_seznam.append(i)
    return nov_seznam

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    nov_seznam = []
    for i in tviti:
        ime = i.split(":")[0]
        if ime not in nov_seznam:
            nov_seznam.append(ime)
    return nov_seznam

def izloci_besedo(beseda):
    crke = []
    prejsnja = beseda[0]
    dodajPrejsnjo = False
    for c in beseda:
        if not c.isalnum():
            if prejsnja.isalnum() and c == '-':
                dodajPrejsnjo = True
        else:
            if dodajPrejsnjo:
                crke.append(prejsnja)
                dodajPrejsnjo = False
            crke.append(c)
        prejsnja = c
    return ''.join(crke)

def se_zacne_z(tvit, c):
    split_seznam = tvit.split(" ")
    seznam = []
    for i in split_seznam:
        for element in i:
            if element[0] == c:
                seznam.append(izloci_besedo(i))
    return seznam

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for i in tviti:
        split_seznam = i.split(" ")
        for element in split_seznam:
                if element[0] == c:
                    izlocen_del = izloci_besedo(element)
                    if izlocen_del not in seznam:
                        seznam.append(izlocen_del)
    return seznam

def vse_afne(tviti):
    seznam = []
    for i in tviti:
        split_seznam = i.split(" ")
        for element in split_seznam:
                if element[0] == "@":
                    izlocen_del = izloci_besedo(element)
                    if izlocen_del not in seznam:
                        seznam.append(izlocen_del)
    return seznam

def vsi_hashtagi(tviti):
    seznam = []
    for i in tviti:
        split_seznam = i.split(" ")
        for element in split_seznam:
                if element[0] == "#":
                    izlocen_del = izloci_besedo(element)
                    if izlocen_del not in seznam:
                        seznam.append(izlocen_del)
    return seznam

def vse_osebe(tviti):
    seznam = []
    avtorji = vsi_avtorji(tviti)
    afne = vse_afne(tviti)
    for i in avtorji:
        if i not in seznam:
            seznam.append(i)
        for j in afne:
            if j not in seznam:
                seznam.append(j)
            else:
                continue
    return sorted(seznam)

#IZPISI

tviti = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]


s = [1, 2, 1, 1, 3, 2]
print(unikati(s))

tvit = "ana: kdo so te @berta, @cilka, @dani? #krneki"
print(avtor(tvit))

print(vsi_avtorji(tviti))

beseda = "@janez-novak!!!"
print(izloci_besedo(beseda))

tvit = "Benjamin $je $skocil! Visoko!"
c = "$"
print(se_zacne_z(tvit, c))

c = "@"
print(zberi_se_zacne_z(tviti, c))

print(vse_afne(tviti))

print(vsi_hashtagi(tviti))

print(vse_osebe(tviti))


#TESTI

