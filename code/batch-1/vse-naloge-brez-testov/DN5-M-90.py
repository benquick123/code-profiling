tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]
def unikati(s):
    seznamUnikati=[]
    for el1 in s:
        if el1 not in seznamUnikati:
            seznamUnikati.append(el1)
    return seznamUnikati

#print(unikati([1, 3, 2, 1, 1, 3, 2]))

def avtor(tvit):
  avtor= tvit.split(":")
  return avtor[0]

#print(avtor( "ana: kdo so te @berta, @cilka, @dani? #krneki"))

def vsi_avtorji(tviti):
    avtorji=[]
    for el in tviti:
        avtorji.append(avtor(el))
    return unikati(avtorji)

#print(vsi_avtorji(tviti))
def izloci_besedo(beseda):
    i=0
    b=False
    word=[]
    while i<len(beseda):
        if beseda[i].isalnum() or beseda[i]=="-":
            if beseda[i]!="-":
                word.append(beseda[i])
            elif i>0 and i+1<len(beseda) and beseda[i-1].isalnum() and beseda[i+1].isalnum():
                word.append(beseda[i])
        i=i+1
    return "".join(word)


#print(izloci_besedo("!%$ana---"))
#print(izloci_besedo("@janez-nov-ak!!----!"))

def se_zacne_z(tvit, c):
    ustreza=[]
    vrni=[]
    for beseda in tvit.split():
        if beseda[0]==c:
            ustreza.append(beseda)
    for beseda in ustreza:
        vrni.append(izloci_besedo(beseda))
    return vrni

#print(se_zacne_z("sandra: @berta Ne maram #programiranje1 #krneki", "#"))

def zberi_se_zacne_z (tviti,c):
    afne=[]
    for tvit in tviti:
        tvit=tvit.split()
        for beseda in tvit:
            if c in beseda:
                afna=beseda.split(c)
                afna=izloci_besedo(afna[1])
                afne.append(afna)
    return unikati(afne)
#print(zberi_se_zacne_z(tviti,"@"))
def vse_afne(tviti):
    return  zberi_se_zacne_z(tviti,"@")

#print(vse_afne(tviti))

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

#print(vsi_hashtagi(tviti))

def vse_osebe(tviti):
    skupaj=vsi_avtorji(tviti)+zberi_se_zacne_z(tviti,"@")
    urejeno=unikati(skupaj)
    urejeno.sort()
    return urejeno
#print(vse_osebe(tviti))

def custva(tviti, hashtagi):
    avtorji=[]
    for tvit in tviti:
        for tag in hashtagi:
            if tag in tvit:
                avtorji.append(avtor(tvit))
    avtorji=unikati(avtorji)
    avtorji.sort()
    return avtorji
#print(custva(tviti, ["dougcajt", "krneki"]))

def se_poznata(tviti, oseba1, oseba2):
    vsebuje=[]
    for tvit in tviti:
        if oseba1 in tvit:
            vsebuje.append(tvit)
    for tvit in vsebuje:
        if oseba2 in tvit:
            return True
        else:
            return False


