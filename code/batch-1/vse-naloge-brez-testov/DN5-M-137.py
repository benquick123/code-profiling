def unikati(s):
    nov = []
    for x in s:
        if not x in nov:
            nov.append(x)
    return nov

def avtor(tvit):
    ime = ""
    for x in tvit:
        if x == ":":
            break
        ime += x
    return ime

def vsi_avtorji(tviti):
    seznam = []
    for x in tviti:
        ime = avtor(x)
        if not ime in seznam:
            seznam.append(ime)
    return seznam

def izloci_besedo(beseda):
    nova = ""
    i = 0
    while i < len(beseda) - 1:
        if beseda[i].isalnum():
            levi = i
            break
        i += 1
    #print(levi)
    j = len(beseda) - 1
    while j > 0:
        if beseda[j].isalnum():
            desni = j
            break
        j -= 1
    #print(desni)
    return beseda[levi : desni + 1]

#print(izloci_besedo("@ana"))

def se_zacne_z(tvit,c):
    besede = []
    for x in tvit.split(" "):
        if x[0] == c:
            besede.append(izloci_besedo(x))
    return besede
#print(se_zacne_z("sandra: @berta Ne maram #programiranje1 #krneki", "#"))

def zberi_se_zacne_z(tviti,c):
    vse = []
    for tvit in tviti:
        rez = se_zacne_z(tvit,c)
        for x in rez:
            if not x in vse:
                vse.append(x)
    return vse

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    imena = []
    for x in tviti:
        for parce in x.split(" "):
            if ":" in parce or "@" in parce:
                beseda = izloci_besedo(parce)
                if not beseda in imena:
                    imena.append(beseda)
    return sorted(imena)

def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        besede = tvit.split(" ")
        nov = []
        for parce in besede:
            beseda = izloci_besedo(parce)
            nov.append(beseda)
        for x in hashtagi:
            if x in nov:
                if not avtor(tvit) in avtorji:
                    avtorji.append(avtor(tvit))
    return sorted(avtorji)

def se_poznata(tviti,oseba1,oseba2):
    avtorji = vsi_avtorji(tviti)
    if oseba1 in avtorji and oseba2 in avtorji:
        for tvit in tviti:
            besede = []
            for x in tvit.split(" "):
                besede.append(izloci_besedo(x))
            if (besede[0] == oseba1 and oseba2 in besede
                and oseba1) or (besede[0] == oseba2 and oseba1 in besede):
                return True
    return False


