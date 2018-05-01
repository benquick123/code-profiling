random_tviti = ["sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "ema: @benjamin @ana #split? po dvopičju, za začetek?"]


# 1
def unikati(s):
    lista_unikatov = []
    for vrednost in s:
        if not vrednost in lista_unikatov:
            lista_unikatov.append(vrednost)
    return lista_unikatov;


# 2
def avtor(tvit):
    razdeli_tvit = tvit.split(':')
    return razdeli_tvit[0];


print
avtor("ana: kdo so te @berta, @cilka, @dani? #krneki")


# 3
def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        razdeli_tvit = tvit.split(':')
        avtor = razdeli_tvit[0]
        if not avtor in avtorji:
            avtorji.append(avtor)
    return avtorji;


print
vsi_avtorji(random_tviti)


# 4
def izloci_besedo(beseda):
    chrke = []
    ii = 0
    for chrka in beseda:
        if chrka.isalnum():
            chrke.append(ii)
        ii += 1
    beseda = beseda[min(chrke):max(chrke)+1] # bil napačen pogoj
    return beseda


# 5
def se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        besede = ""
        zapisuj = False
        for chrka in tvit:
            if chrka == c:
                zapisuj = True
            elif not chrka.isalnum() and beseda:
                if not beseda in besede:
                    besede.append(beseda)
                beseda = ""
                zapisuj = False
            elif zapisuj:
                beseda += chrka
        if beseda and not beseda in besede:
            besede.append(beseda)
        return besede;


# 6
def zberi_se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        beseda = ""
        zapisuj = False
        for chrka in tvit:
            if chrka == c:
                zapisuj = True
            elif not chrka.isalnum() and beseda:
                if not beseda in besede:
                    besede.append(beseda)
                beseda = ""
                zapisuj = False
            elif zapisuj:
                beseda += chrka
        if beseda and not beseda in besede:
            besede.append(beseda)
    return besede;


print
zberi_se_zacne_z(random_tviti, "@")


# 7
def vse_afne(tviti):
    besede = []
    for tvit in tviti:
        beseda = ""
        zapisuj = False
        for chrka in tvit:
            if chrka == "@":
                zapisuj = True
            elif not chrka.isalnum() and beseda:
                if not beseda in besede:
                    besede.append(beseda)
                beseda = ""
                zapisuj = False
            elif zapisuj:
                beseda += chrka
        if beseda and not beseda in besede:
            besede.append(beseda)
    return besede;


# 8
def vsi_hashtagi(tviti):
    besede = []
    for tvit in tviti:
        beseda = ""
        zapisuj = False
        for chrka in tvit:
            if chrka == "#":
                zapisuj = True
            elif not chrka.isalnum() and beseda:
                if not beseda in besede:
                    besede.append(beseda)
                beseda = ""
                zapisuj = False
            elif zapisuj:
                beseda += chrka
        if beseda and not beseda in besede:
            besede.append(beseda)
    return besede;


print
vsi_hashtagi(random_tviti)


# 9
def vse_osebe(tviti):
    besede = []
    for tvit in tviti:
        beseda = ""
        zapisuj = False
        avtor = False
        for chrka in tvit:
            if not avtor:
                avtor = True
                zapisuj = True
            if chrka == "@":
                zapisuj = True
                continue
            elif not chrka.isalnum() and beseda:
                if not beseda in besede:
                    besede.append(beseda)
                beseda = ""
                zapisuj = False
            if zapisuj:
                beseda += chrka
        if beseda and not beseda in besede:
            besede.append(beseda)
    besede.sort()
    return besede;


print
vse_osebe(random_tviti)


# 1*
def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        beseda = ""
        zapisuj = False
        razdeli_tvit = tvit.split(':')
        avtor = razdeli_tvit[0]
        for chrka in tvit:
            if chrka == "#":
                zapisuj = True
            elif not chrka.isalnum() and beseda:
                if beseda in hashtagi and avtor not in avtorji:
                    avtorji.append(avtor)
                beseda = ""
                zapisuj = False
            elif zapisuj:
                beseda += chrka
        if beseda and beseda in hashtagi and avtor not in avtorji:
            avtorji.append(avtor)
        avtorji.sort()
    return avtorji;


print
custva(random_tviti, ["dougcajt", "krneki"])


# 2*
def se_poznata(tviti, oseba1, oseba2):
    osebi = [oseba1, oseba2]
    znanca = False
    for tvit in tviti:
        beseda = ""
        zapisuj = False
        razdeli_tvit = tvit.split(':')
        avtor = razdeli_tvit[0]
        for chrka in tvit:
            if chrka == "@":
                zapisuj = True
            elif not chrka.isalnum() and beseda:
                if not beseda == avtor and beseda in osebi and avtor in osebi:
                    znanca = True
                    return znanca
                beseda = ""
                zapisuj = False
            elif zapisuj:
                beseda += chrka
        if beseda and not beseda == avtor and beseda in osebi and avtor in osebi:
            znanca = True
    return znanca;


print
se_poznata(random_tviti, "benjamin", "cilka")
print
se_poznata(random_tviti, "berta", "sandra")

