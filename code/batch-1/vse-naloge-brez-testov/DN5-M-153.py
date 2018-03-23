def unikati(seznam):
    #vrne enoličen seznam brez ponovljenih elementov
    novSeznam = []
    for element in seznam:
        if element in novSeznam:
            continue
        else:
            novSeznam.append(element)
    return novSeznam

def avtor(tvit):
    #vrne avtorja tvita
    tvit = tvit.split(":")
    return tvit[0]

def vsi_avtorji(seznam):
    #vrne vse avotrje tvitov v nekem seznami tvitov
    seznamAvtorjev = []
    for element in seznam:
        seznamAvtorjev.append(avtor(element))
    seznamAvtorjev = unikati(seznamAvtorjev)
    return seznamAvtorjev

def izloci_besedo(beseda):
    #funkcija izloči vse ne alfanumerične znake pred in za podano besedo
    novaBeseda = beseda
    for i in range(len(beseda)):
        if beseda[i].isalnum():
            break
        else:
            novaBeseda = beseda[i+1:]
    for j in range(len(novaBeseda)-1,0,-1):
        if novaBeseda[j].isalnum():
            break
        else:
            novaBeseda = novaBeseda[:j]
    return novaBeseda

def se_zacne_z(tvit, znak):
    #vrne besede, ki se začnejo z znakom
    seznamBesed = []
    tvit = tvit.split()
    for element in tvit:
        if element[0] == znak:
            #izloci_besedo izloci vse ne alfanumerične znake na začetku alni na koncu
            seznamBesed.append(izloci_besedo(element))
    return seznamBesed

def zberi_se_zacne_z(seznamTvitov, znak):
    #funkcjia gre skozi seznam tvitov in izbere vse besede ki se začnejo na izbran znak
    seznamBesed = []
    for tvit in seznamTvitov:
        besede = se_zacne_z(tvit, znak)
        #funkcija se_zacne_z vrne seznam zato moramo skozi podani seznam in v nov seznam zapisati stringe in ne seznamov
        for element in besede:
                seznamBesed.append(element)
    seznamBesed = unikati(seznamBesed)
    return seznamBesed

def vse_afne(tviti):
    #poišče vse besede ki se začnejo z @
    seznamBesed = zberi_se_zacne_z(tviti, "@")
    #funkcija vrne seznam unikatnih besed(se ne ponovijo)
    return unikati(seznamBesed)

def vsi_hashtagi(tviti):
    #poišče vse besede ki se začnejo z #
    seznamBesed = zberi_se_zacne_z(tviti, "#")
    #funkcija vrne seznam unikatnih besed(se ne ponovijo)
    return unikati(seznamBesed)

def vse_osebe(tviti):
    #funkcija vrne po abecedi urejen seznam vseh oseb, ki nastopaj o v tvitih
    seznamOseb = []
    #poišče vse avtorji in jih doda v seznam
    seznamOseb = vsi_avtorji(tviti)
    #poišče vse osebe, ki so bile označene z @
    seznamOseb += vse_afne(tviti)
    #vsako oseba se pojavi v seznamu samo enkrat
    seznamOseb = unikati(seznamOseb)
    #urejanje po abecedi -> sorted
    return sorted(seznamOseb)

def custva(tviti, hashtagi):
    #funkcija vrne osebe, ki so oparabili podane hashtahe
    seznamOseb = []
    seznamTvitov = []
    #poišče vse tvite ki imajo naštete hashtage in jih shrani v seznam
    for hastag in hashtagi:
        for tvit in tviti:
            if tvit.find(hastag) >= 0:
                seznamTvitov.append(tvit)
    #iz seznama dobljenih tvitov dobimo vse avtorje
    seznamOseb = vsi_avtorji(seznamTvitov)
    #iz seznama avtorjev odstranimo duplikate
    seznamOseb = unikati(seznamOseb)
    #vrenmo seznam oseb, urejeno po abecedi
    return sorted(seznamOseb)

def se_poznata(tviti, oseba1, oseba2):
    #funkcija vrne true če je oseba1 imenila osebo2 v svojem tvitu drugače vrne false
    seznamTvitov = []
    #najdemo vse tvite, ki jih je napisala oseba1
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            seznamTvitov.append(tvit)
    #poiščemo ali je oseba2 omenjena v tvitih osebe 1
    for tvit in seznamTvitov:
        if tvit.find("@"+oseba2) >= 0:
            return True
    return False

####TESTI#####
