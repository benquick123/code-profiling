def unikati(s):
    vrnjenSeznam = []
    for element in s:
        if element not in vrnjenSeznam:
            vrnjenSeznam.append(element)
    return vrnjenSeznam

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

def vsi_avtorji(tviti):
    seznamAvtorjev = []
    for tvit in tviti:
        seznamAvtorjev.append(avtor(tvit))
    return unikati(seznamAvtorjev)

def besedilo(tvit):
    avtor, tekst = tvit.split(": ",1)
    return tekst

def avtor(tvit):
    ime, tekst = tvit.split(": ",1)
    return ime

def zadnji_tvit(tviti):
    zadnjiTviti = {}
    for tvit in tviti:
        zadnjiTviti[avtor(tvit)] = besedilo(tvit)
    return zadnjiTviti

def prvi_tvit(tviti):
    prviTviti = {}
    for tvit in tviti:
        if avtor(tvit) not in prviTviti:
            prviTviti[avtor(tvit)] = besedilo(tvit)
    return prviTviti

def prestej_tvite(tviti):
    steviloTvitov = {}
    for tvit in tviti:
        if avtor(tvit) not in steviloTvitov:
            steviloTvitov[avtor(tvit)] = 1
        else:
            steviloTvitov[avtor(tvit)] += 1
    return steviloTvitov

def omembe(tviti):
    avtorji = vsi_avtorji(tviti)
    omenjeneOsebe = {}
    for ime in avtorji:
        for tvit in tviti:
            if avtor(tvit) == ime:
                if avtor(tvit) not in omenjeneOsebe:
                    omenjeneOsebe[avtor(tvit)] = se_zacne_z(tvit, "@")
                else:
                    omenjeneOsebe[avtor(tvit)] = omenjeneOsebe[avtor(tvit)] + se_zacne_z(tvit,"@")
    return omenjeneOsebe

def neomembe(ime, omembe):
    neomenjeneOsebe = []
    vsaImena = []
    for avtor in omembe:
        vsaImena.append(avtor)
    for naziv in vsaImena:
        if naziv != ime:
            if naziv not in omembe[ime]:
                neomenjeneOsebe.append(naziv)
    return neomenjeneOsebe


