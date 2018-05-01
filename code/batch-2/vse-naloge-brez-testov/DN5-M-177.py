def unikati(s):
    seznam = []
    for x in s:
        if x in seznam:
            pass
        else:
            seznam.append(x)
    return seznam

def avtor(tvit):
    seznam = tvit.split()
    for x in seznam:
        if x.endswith(":"):
            x = x.replace(":", "")
            return x

def vsi_avtorji(tviti):
    avtorji = []
    for x in tviti:
        avtor1 = avtor(x)
        if avtor1 in avtorji:
            pass
        else:
            avtorji.append(avtor1)
    return avtorji

def izloci_besedo(beseda):          #popravljena = re.sub('[^0-9a-zA-Z\-]+', '', beseda)
    while beseda[0].isalnum() == False:
        sprednji = beseda.replace(beseda[0], "")
        beseda = sprednji
    zadnji = beseda[::-1]
    while zadnji[0].isalnum() == False:
        zadnji = zadnji.replace(zadnji[0], "")
    rezultat = zadnji[::-1]
    return rezultat


def se_zacne_z(tvit, c):
    sezn = []
    tvt = tvit.split()
    for x in tvt:
        if x.startswith(c):
            besede = izloci_besedo(x)
            sezn.append(besede)
    return sezn

def zberi_se_zacne_z(tviti, c):
    seznam2 = []
    for x in tviti:
        bg = se_zacne_z(x, c)
        seznam2.extend(bg)
    sez = unikati(seznam2)
    return sez

def vse_afne(tviti):
    g = zberi_se_zacne_z(tviti, "@")
    return g

def vsi_hashtagi(tviti):
    gg = zberi_se_zacne_z(tviti, "#")
    return gg

def vse_osebe(tviti):
    seznam = []
    x = vsi_avtorji(tviti)
    seznam.extend(x)
    xx = vse_afne(tviti)
    seznam.extend(xx)
    gg = unikati(seznam)
    gg.sort()
    return gg

def custva(tviti, hashtagi):
    pogoj = []
    for i in tviti:
        tagi = se_zacne_z(i, "#")
        for ii in hashtagi:
            for gg in tagi:
                if ii == gg:
                    c = avtor(i)
                    pogoj.append(c)
    pogoj.sort()
    return unikati(pogoj)

def se_poznata(tviti, oseba1, oseba2):
    afne = []
    bafne = []
    for i in tviti:
        if avtor(i) == oseba1:
            afne = se_zacne_z(i, "@")
        if avtor(i) == oseba2:
            bafne = se_zacne_z(i, "@")
    if oseba1 in bafne:
        return True
    elif oseba2 in afne:
        return True
    else:
        return False






