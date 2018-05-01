def unikati(s):
    novsez = []
    for element in s:
        if element not in novsez:
            novsez.append(element)
        else:
            continue
    return novsez

def avtor(tvit):
    a = tvit.split(":")
    return a[0]

def vsi_avtorji(tviti):
    sez = []
    for e in tviti:
        avt = avtor(e)
        if avt not in sez:
            sez.append(avt)

    return sez

def izloci_besedo(beseda):
    i = 0
    text = beseda
    nov = ""
    while i < len(text):
        crka = text[i]
        if text[i] == "-":
            nov += text[i]
        if text[i].isalnum() == True:
            nov += text[i]
        i += 1
    return nov


def se_zacne_z(tvit, c):
    sez = tvit.split()
    nov = []
    for beseda in sez:
        if beseda[0] == c:
            uredi = izloci_besedo(beseda)
            nov.append(uredi)
    return nov

def zberi_se_zacne_z(tviti, c):
    sez = []
    for tvit in tviti:
        urejen = tvit.split()
        for beseda in urejen:
            uredi = se_zacne_z(tvit,c)
            sez += uredi
    mno = unikati(sez)
    return mno

def vse_afne(tviti):
    poklici = zberi_se_zacne_z(tviti, "@")
    return poklici

def vsi_hashtagi(tviti):
    poklici = zberi_se_zacne_z(tviti, "#")
    return poklici

def vse_osebe(tviti):
    sez = vsi_avtorji(tviti)
    sez2 = vse_afne(tviti)
    sez3 = sorted((sez + sez2))
    sez4 = unikati(sez3)
    return sez4

def custva(tviti, hashtagi):
    sez = []
    for tvit in tviti:
        avt = avtor(tvit)
        razdeli = tvit.split()
        for element in razdeli:
            izloc = izloci_besedo(element)
            if izloc in hashtagi:
                sez.append(avt)
    novi = unikati(sez)
    urejen = sorted(novi)
    return urejen

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        kdo = avtor(tvit)
        afna = se_zacne_z(tvit,"@")
        if afna != []:
            for element in afna:
                if kdo == oseba1 and element == oseba2 or kdo == oseba2 and element == oseba1:
                    return True
    else:
        return False




