def unikati(s):
    u = []
    for a in s:
        if a not in u:
            u.append(a)
    return u

def avtor(tvit):
    avtor = []
    for a in tvit:
        if a == ":" :
            break
        avtor.append(a)
    return ''.join(avtor)

def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)

def izloci_besedo(beseda):
    besedaList = list(beseda)
    while not besedaList[0].isalnum():
        del besedaList[0]
    i = len(besedaList) - 1
    while not besedaList[i].isalnum():
        del besedaList[i]
        i -= 1
    return ''.join(besedaList)

def se_zacne_z(tvit, c):
    beseda = []
    tvitBesede = []
    i=0
    while i < len(tvit):
        if i == 0:
            if tvit[i] == c:
                j = i
                while tvit[j] != " ":
                    beseda.append(tvit[j])
                    j += 1
                tvitBesede.append(izloci_besedo(beseda))
                i = j-1
        elif tvit[i] == " ":
            if tvit[i+1] == c:
                j = i+1
                while j != len(tvit) and tvit[j] != " ":
                    beseda.append(tvit[j])
                    j += 1
                tvitBesede.append(izloci_besedo(beseda))
                i = j -1
        del beseda[:]
        i += 1
    return tvitBesede

def zberi_se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        besede.extend(se_zacne_z(tvit, c))
    return unikati(besede)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    osebe = []
    osebe.extend(vsi_avtorji(tviti))
    osebe.extend(vse_afne(tviti))
    osebe.sort
    osebe = unikati(osebe)
    osebe.sort()
    return osebe

def custva(tviti, hashtagi):
    besede = []
    avtorji = []
    for i, tvit in enumerate(tviti):
        besede = se_zacne_z(tvit,"#")
        for a in besede:
            if a in hashtagi:
                avtorji.append(avtor(tvit))
    avtorji = unikati(avtorji)
    avtorji.sort()
    return avtorji

def se_poznata(tviti, oseba1, oseba2):
    tvitList = []
    for i, tvit in enumerate(tviti):
        tvitList.append(tvit)
        if avtor(tvit) == oseba1:
            if oseba2 in vse_afne(tvitList):
                return True
        if avtor(tvit) == oseba2:
            if oseba1 in vse_afne(tvitList):
                return True
        del tvitList[:]
    return False

