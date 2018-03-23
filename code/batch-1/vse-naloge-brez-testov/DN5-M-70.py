#koda:
def unikati(s):
    t=[]
    for vsak in s:
        if vsak not in t:
            t.append(vsak)
    return t

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    tviti2=[]
    for tvit in tviti:tviti2.append(avtor(tvit))
    return unikati(tviti2)

def izloci_besedo(beseda):
    ok=False
    while not ok:
        if not beseda[0].isalnum():
            beseda=beseda[1:]
        elif not beseda[len(beseda)-1].isalnum():
            beseda=beseda[:-1]
        else:
            ok=True
    return beseda

def se_zacne_z(tvit,c):
    besede=[]
    for beseda in tvit.split():
        if beseda.startswith(c):
            besede.append(izloci_besedo(beseda))
    return besede

def zberi_se_zacne_z(tviti, c):
    besede=[]
    for tvit in tviti:
        besede.extend(se_zacne_z(tvit,c))
    return unikati(besede)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    osebe1=zberi_se_zacne_z(tviti,"@")
    osebe1.extend(vsi_avtorji(tviti))
    return sorted(unikati(osebe1))


#Dodatne
def custva(tviti, hashtagi):
    osebe=[]
    for tvit in tviti:
        for beseda in tvit.split():
            for hashtag in hashtagi:
                if izloci_besedo(beseda)==hashtag:
                    osebe.append(avtor(tvit))
    return sorted(unikati(osebe))

def se_poznata(tviti,oseba1,oseba2):
    t=[]
    for tvit in tviti:
        for bes in tvit.split():
            if se_zacne_z(bes,"@"):
                t.append(izloci_besedo(bes))
        if avtor(tvit) == oseba1:
            if oseba2 in t:
                print("Avtor: ",oseba1,"Prijatelj: ",oseba2)
                return True
        elif avtor(tvit) == oseba2:
            if oseba1 in t:
                print("Avtor: ",oseba2,"Prijatelj: ",oseba1)
                return True
        t=[]
    return False
    


tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]
    







