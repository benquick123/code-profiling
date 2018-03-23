def unikati(s):
    vrnjenSeznam = []
    for element in s:
        if element not in vrnjenSeznam:
            vrnjenSeznam.append(element)
    return vrnjenSeznam

def avtor(tvit):
    ime, besedilo = tvit.split(":",1)
    return ime

def vsi_avtorji(tviti):
    seznamAvtorjev = []
    for tvit in tviti:
        seznamAvtorjev.append(avtor(tvit))
    return unikati(seznamAvtorjev)

def izloci_besedo(beseda):
    for i in range(0,len(beseda)-1):
        if beseda[i].isalnum() == True:
            for j in range(len(beseda),i,-1):
                if beseda[j-1].isalnum() == True:
                    beseda = beseda[i:j]
                    break
            break
    return beseda

def se_zacne_z(tvit, c):
    seznam = tvit.split()
    seznamSeZacne = []
    for element in seznam:
        if element[0] == c:
            seznamSeZacne.append(izloci_besedo(element))
    return seznamSeZacne

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        seznam += se_zacne_z(tvit,c)
    return unikati(seznam)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    osebe = []
    osebe += vsi_avtorji(tviti) + vse_afne(tviti)
    return sorted(unikati(osebe))

def custva(tviti, hashtagi):
    osebe = []
    for tvit in tviti:
        if any(i in hashtagi for i in se_zacne_z(tvit,"#")):
            osebe.append(avtor(tvit))
    return sorted(unikati(osebe))

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            if oseba2 in se_zacne_z(tvit, "@"):
                return True
        elif avtor(tvit) == oseba2:
            if oseba1 in se_zacne_z(tvit, "@"):
                return True
    return False

