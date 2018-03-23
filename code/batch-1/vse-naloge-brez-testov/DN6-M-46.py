def besedilo(tvit):
    i=0
    while i < len(tvit):
        if (tvit[i]==':'):
            i = i + 2
            tvit=tvit[i:]
            break
        i=i+1
    return tvit

def avtor(tvit):
    i=-1
    for posamezen in tvit:
        i = i + 1
        if posamezen == ':':
            return(tvit[:i])


def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        if (avtor(tvit) not in slovar):
            slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = 0
        slovar[avtor(tvit)] += 1
    return slovar

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        vsaka = tvit.split()
        for posebi in vsaka:
            if (posebi[0] == c):
                if izloci_besedo(posebi) not in seznam:
                    seznam.append(izloci_besedo(posebi))
    return (seznam)

def izloci_besedo(beseda):
    for crka in beseda:
        if crka.isalnum() == False:
            beseda = beseda[1:]
        else:
            break
    while (1):
        if beseda[-1].isalnum() == False:
            beseda = beseda[:-1]
        else:
            break
    return(beseda)

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            vsaka = tvit.split()
            for posebi in vsaka:
                if izloci_besedo(posebi) == oseba2 and posebi[0] == '@':
                    return True
    return False


def vsi_avtorji(tviti):
    seznam = []
    for tvit in tviti:
        if avtor(tvit) not in seznam:
            seznam.append(avtor(tvit))
    return seznam

def vse_osebe(tviti):
    seznam = vsi_avtorji(tviti)
    seznam1 = vse_afne(tviti)
    for element in seznam1:
        if element not in seznam:
            seznam.append(element)
    return sorted(seznam)

def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = []
        for posebi in tvit.split():
            if (posebi[0] == '@'):
                if izloci_besedo(posebi) not in slovar[avtor(tvit)]:
                    slovar[avtor(tvit)].append(izloci_besedo(posebi))
    return slovar

def neomembe(ime, omembe):
    seznam = []
    for imena in omembe.keys():
        if imena not in omembe[ime] and imena != ime:
            seznam.append(imena)
    return(seznam)

def se_poznata(ime1, ime2, omembe):

    if ime1 not in omembe and ime2 not in omembe:
        return False

    if ime1 not in omembe and ime2 in omembe:
        if ime1 in omembe[ime2]:
             return True
        return False

    if ime1 in omembe and ime2 not in omembe:
        if ime2 in omembe[ime1]:
             return True
        return False

    if ime1 in omembe[ime2]:
        return True
    if ime2 in omembe[ime1]:
        return True
    return False

def hashtagi(tviti):
    seznam = {}
    for tvit in tviti:
        for vsaka in tvit.split():
            if vsaka[0] == '#':
                seznam[izloci_besedo(vsaka)] = []   #vsakmu dodelim seznam
    for tvit in tviti:
        for vsaka in tvit.split():
            if izloci_besedo(vsaka) in seznam:
                for znak in seznam.keys():
                    if izloci_besedo(vsaka) == znak:
                        seznam[znak].append(avtor(tvit))
                        seznam[znak] = sorted(seznam[znak])
    return seznam









